import predacons
import os
from rich import print
from rich.prompt import Prompt
import json
import logging
import time
from rich.table import Table
from rich.markdown import Markdown
from rich.console import Console
try:
    from .rag import VectorStore
    from .rag import WebScraper
except:
    print("Importing from .rag failed trying to import from rag usually happens when running from source")
    from rag import VectorStore
    from rag import WebScraper


console = Console()

logging.getLogger("transformers").setLevel(logging.ERROR)


class Cli:
    def __init__(self):
        self.predacons = predacons
        self.config_file_path = os.path.join(os.path.expanduser("~"), ".predacons_cli", "predacon_cli_config.json")
        self.ensure_config_directory_exists()
        # try:
        #     os.environ['CUDA_VISIBLE_DEVICES'] ='0'
        #     import torch
        #     if torch.cuda.is_available():
        #         torch.set_default_device('cuda')
        #         print("Using GPU")
        #     else:
        #         print("No GPU available")
        # except:
        #     print("No GPU available")

    def ensure_config_directory_exists(self):
        config_dir = os.path.dirname(self.config_file_path)
        if not os.path.exists(config_dir):
            os.makedirs(config_dir)

    def launch(self,logs=False):
        """
        Launch the Predacons CLI application.

        This function sets up the argument parser, processes command-line arguments,
        and invokes the appropriate CLI commands based on the provided arguments.
        If no arguments are provided, it launches the default CLI interface.
        """
        print("[i]Welcome to the Predacons CLI![/i]")
        # check if the predacon_cli_config.json file exists
        config = Cli.check_config_file(self)
        if not config:
            print("[yellow]No config file found. Creating one now...[/yellow]")
            config = Cli.create_config_file(self)
        # print(config)
        
        model,tokenizer = Cli.load_model(self,config["model_path"],
                                         config["trust_remote_code"],
                                         config["use_fast_generation"],
                                         config["draft_model_name"],
                                         config["gguf_file"],
                                         config["auto_quantize"])
        
        chat  = []
        vector_db = None
        print("[yellow]Checking for data sources for the chat[/yellow]")
        if config.get("scrap_web", False):
            print("[yellow]Web scraping enabled iitializing web scraper[/yellow]")
            try:
                web_scraper = WebScraper()
                print("[green]Web scraper initialized![/green]")
            except:
                print("[red]Web scraper initialization failed![/red]")
                print("[yellow]Continueing with simple chat[/yellow]")
        
        if config.get("chat_with_data", False):
            print("[yellow]Chat with data enabled looking for vector db[/yellow]")
            if not os.path.exists(config.get("vector_db_path", False)):
                print("[red]Vector DB not found![/red]")
                print("[yellow]Continueing with simple chat[/yellow]")
            else:
                print("[green]Vector DB found![/green]")
                print("[yellow]Loading data from vector DB[/yellow]")
                # load data from vector db

                vector_store = VectorStore(config["vector_db_path"], config["document_path"], config.get("embedding_model", None))
                vector_db = vector_store.load_db()
                print("[yellow]Data loaded successfully![/yellow]")
            
        if logs == False:
            print("[yellow]Model loaded poperly Clearing logs in 1 sec to keep the logs start predacons with --logs [/yellow]")
            for i in range(1, 0, -1):
                time.sleep(1)
            os.system('clear')  # Clear the screen
        
        print("[i]Welcome to the Predacons CLI![/i] [green]Model: [orange1]"+config["model_path"]+"[/orange1] loaded successfully![/green]")
        print("[yellow]You can start chatting with Predacons now.Type 'clear' to clear history, Type 'exit' to quit, Type 'help' for more options, Type 'update' to update the load documents[/yellow]")
        while True:
            user_input = Prompt.ask("[green]User[/green]")
            
            if user_input == "exit":
                return
            elif user_input == "clear":
                chat = []
                print("[yellow]Chat history cleared![/yellow]")
            elif user_input == "clear-config":
                Cli.clear_config(self)
            elif user_input == "settings":
                Cli.settings(self)
            elif user_input == "version":
                Cli.version(self)
            elif user_input == "help":
                print("[yellow]Type 'clear' to clear history, Type 'exit' to quit, Type 'help' for more options, Type 'update' to update the load documents[/yellow]")
            elif user_input == "update":
                print("[yellow]Updating documents...[/yellow]")
                # check and update the vector store
                vector_store.load_and_update_db()
                print("[yellow]Documents updated successfully![/yellow]")
            else:
                if config.get("chat_with_data", False) and vector_db:
                    # get response from vector store
                    context_text,similarity_score = vector_store.get_similar(user_input, db=vector_db, top_n=5, similarity_threshold=0.1)
                    # extract page_details from response
                    print("Similarity score: ", similarity_score)
                    if config.get("scrap_web", False) and similarity_score < 0.4:
                        web_text = web_scraper.get_web_data(user_input,3)
                        PROMPT_TEMPLATE = """
                        Answer the question based only on the following context:

                        {db_context}

                        
                        Here are additianl infor from web search this context is google search results and web scraped data on the same topic :

                        {web_context}

                        ---

                        Answer the question based on the above context: {question}
                        """

                        user_input = PROMPT_TEMPLATE.format(db_context=context_text,web_context=web_text, question=user_input)
                    
                    PROMPT_TEMPLATE = """
                    Answer the question based only on the following context:

                    {context}

                    ---

                    Answer the question based on the above context: {question}
                    """

                    user_input = PROMPT_TEMPLATE.format(context=context_text, question=user_input)
                elif config.get("scrap_web", False) :
                    # scrap the web and
                    web_text = web_scraper.get_web_data(user_input,3)
                    PROMPT_TEMPLATE = """
                    Answer the question based only on the following context this context is google search results and web scraped data:

                    {context}

                    ---

                    Answer the question based on the above context: {question}
                    """

                    user_input = PROMPT_TEMPLATE.format(context=web_text, question=user_input)
                user_body = {"role": "user", "content": user_input} 
                chat.append(user_body)
                response = Cli.generate_response(self, chat, model, tokenizer, config)
                response_body = {"role": "assistant", "content": response}
                chat.append(response_body)
                if config["print_as_markdown"]:
                    markdown = Markdown(response)
                    print("[orange1]Predacons: [/orange1]")
                    console.print(markdown)
                else:
                    console.print("[orange1]Predacons: [/orange1] [sky_blue1]" + response+"[/sky_blue1]")

    
    def load_model(self, model_path,trust_remote_code=False,use_fast_generation=False, draft_model_name=None,gguf_file=None,auto_quantize=None):
        model = self.predacons.load_model(model_path,trust_remote_code=trust_remote_code,use_fast_generation=use_fast_generation, draft_model_name=draft_model_name,gguf_file=gguf_file,auto_quantize=auto_quantize)
        tokenizer = self.predacons.load_tokenizer(model_path,gguf_file=gguf_file)
        return model, tokenizer
        
    def clear_config(self):
        file_path = self.config_file_path
        if os.path.exists(file_path):
            os.remove(file_path)
            print("[green]Configuration file cleared successfully![/green]")
        else:
            print("[red]Configuration file not found![/red]")
    
    def print_config_data(self, config_data):
        table = Table(title="Config Data", row_styles=["none", "dim"])

        # Add columns for keys and values with padding
        table.add_column("Key", justify="left", style="cyan", no_wrap=True)
        table.add_column("Value", justify="left", style="magenta", no_wrap=True)

        # Add rows for each key-value pair with padding
        for key, value in config_data.items():
            table.add_row(f"[bold cyan]{key}[/bold cyan]", f"[bold magenta]{value}[/bold magenta]")

        print(table)
    
    def settings(self):
        file_path = self.config_file_path

        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                config_data = json.load(file)
        self.print_config_data(config_data)
        update = Prompt.ask("Do you want to update settings?", choices=["y", "n"],default="n")
        if update == "y":
            config_data = Cli.create_config_file(self)
            self.print_config_data(config_data)

    def version(self):
        print("[blue]Predacons CLI version 0.0.101[blue]")
        print("[blue]Predacons version 0.0.126[blue]")
    
    def help(self):
        print("[yellow]Type 'clear' to clear history, Type 'exit' to quit, Type 'help' for more options,[/yellow]")
        print("[yellow]--clear-config: Clear the current configuration[/yellow]")
        print("[yellow]--settings: Show settings[/yellow]")
        print("[yellow]--version: Show version[/yellow]")
        print("[yellow]--help: Show help[/yellow]")
        print("[yellow]--logs: Prints all logs[/yellow]")

    def check_config_file(self):
        file_path = self.config_file_path

        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                config_data = json.load(file)
                # print(config_data)
                if 'model_path' not in config_data:
                    return False
            return config_data
            
        else:
            return False
    
    def create_config_file(self):
        config = Cli.check_config_file(self)
        file_path = self.config_file_path
        default_config = {
            "model_path": "Precacons/Pico-Lamma-3.2-1B-Reasoning-Instruct",
            "trust_remote_code": False,
            "use_fast_generation": False,
            "draft_model_name": None,
            "gguf_file": None,
            "auto_quantize": False,
            "temperature": 0.3,
            "max_length": 1000,
            "top_k": 50,
            "top_p": 0.9,
            "repetition_penalty": 1.0,
            "num_return_sequences": 1,
            "print_as_markdown": False,
            "chat_with_data": False,
            "vector_db_path": None,
            "document_path": None,
            "embedding_model" : None,
            "scrap_web": False
        }

        # If no config file is found, use the default configuration
        if not config:
            config = default_config
        else:
            # Ensure all default keys are present in the loaded config
            for key, value in default_config.items():
                if key not in config:
                    config[key] = value
        print("[green]Creating a new configuration file...[/green]")
        
        print("[yellow]Please enter the following details to create a new configuration file[/yellow]")
        # first ask for thype of model: 1: normal local or hugging face safetensor or pytorch model OR 2: gguf model 3 : other type of model
        print("[yellow]Select the type of model:[/yellow]")
        print("[blue]1:[/blue] [yellow]Normal local or Hugging Face safetensor or PyTorch model[/yellow]")
        print("[blue]2:[/blue] [yellow]GGUF model[/yellow]")
        print("[blue]3:[/blue] [yellow]Other type of model[/yellow]")
        model_type = Prompt.ask("Enter the model type (1/2/3)", default="1")
        draft_model_name = None
        gguf_file = None
        use_fast_generation = False
        if model_type == '1':
            model_path = Prompt.ask("Enter the model path or hugging face model name",default= config["model_path"])
            trust_remote_code = Prompt.ask("Trust remote code? (true/false)", default=str(config["trust_remote_code"]))
            use_fast_generation = Prompt.ask("Use fast generation? (true/false)", default=str(config["use_fast_generation"]))
            if use_fast_generation.lower() == 'true':
                draft_model_name = Prompt.ask("Enter the draft model name (optional)", default=config["draft_model_name"])
            auto_quantize = Prompt.ask("Enable auto quantize? (true/false)", default=str(config["auto_quantize"]))
        
        elif model_type == '2':
            model_path = Prompt.ask("Enter the model path or hugging face model name")
            gguf_file = Prompt.ask("Enter the GGUF file path/name", default=config["gguf_file"])
            trust_remote_code = Prompt.ask("Trust remote code? (true/false)", default=str(config["trust_remote_code"]))
            auto_quantize = Prompt.ask("Enable auto quantize? (true/false)", default=str(config["auto_quantize"]))

        elif model_type == '3':
            print("[yellow]Not supported yet adding soon... for now try default model[/yellow]")
            model_path = Prompt.ask("Enter the model path or hugging face model name")
            trust_remote_code = Prompt.ask("Trust remote code? (true/false)", default=str(config["trust_remote_code"]))
            use_fast_generation = Prompt.ask("Use fast generation? (true/false)", default=str(config["use_fast_generation"]))
            if use_fast_generation.lower() == 'true':
                draft_model_name = Prompt.ask("Enter the draft model name (optional)", default=config["draft_model_name"])
            auto_quantize = Prompt.ask("Enable auto quantize? (true/false)", default=str(config["auto_quantize"]))
        else :
            print("[red]Invalid model type selected![/red]")
            return
        
        temperature = Prompt.ask("Enter the temperature", default=str(config["temperature"]))
        max_length = Prompt.ask("Enter the max length for each response", default=str(config["max_length"]))
        top_k = Prompt.ask("Enter the top k value", default=str(config["top_k"]))
        top_p = Prompt.ask("Enter the top p value", default=str(config["top_p"]))
        repetition_penalty = Prompt.ask("Enter the repetition penalty value", default=str(config["repetition_penalty"]))
        num_return_sequences = Prompt.ask("Enter the number of return sequences", default=str(config["num_return_sequences"]))
        print_as_markdown = Prompt.ask("Print response as markdown? this looks cool but may not print propelry (true/false)", default=str(config["print_as_markdown"]))
        vector_db = Prompt.ask("Chat with data? (true/false)", default=str(config["chat_with_data"]))
        vector_db_path = Prompt.ask("Enter the vector DB path", default=config["vector_db_path"])
        document_path = Prompt.ask("Enter the document path", default=config["document_path"])
        embedding_model = Prompt.ask("Enter the embedding model", default=config["embedding_model"])
        scrap_web = Prompt.ask("Scrap the web for data? (true/false)", default=str(config["scrap_web"]))


        config_data = {
            "model_path": model_path,
            "trust_remote_code": trust_remote_code.lower() == 'true',
            "use_fast_generation": use_fast_generation.lower() == 'true',
            "draft_model_name": draft_model_name if draft_model_name else None,
            "gguf_file": gguf_file if gguf_file else None,
            "auto_quantize": auto_quantize.lower() == 'true',
            "temperature": float(temperature),
            "max_length": int(max_length),
            "top_k": int(top_k),
            "top_p": float(top_p),
            "repetition_penalty": float(repetition_penalty),
            "num_return_sequences": int(num_return_sequences),
            "print_as_markdown": print_as_markdown.lower() == 'true',
            "chat_with_data": vector_db.lower() == 'true',
            "vector_db_path": vector_db_path if vector_db_path else None,
            "document_path": document_path if document_path else None,
            "embedding_model": embedding_model if embedding_model else None,
            "scrap_web": scrap_web.lower() == 'true'
        }
        
        with open(file_path, 'w') as f:
            json.dump(config_data, f, indent=4)
        
        print("[green]Configuration file created successfully![/green]")
        return config_data

    def load_config_file(self):
        file_path = self.config_file_path
        with open(file_path, 'r') as f:
            config = f.read()
        return config

    def generate_response(self, chat, model, tokenizer, config):
        response = self.predacons.chat_generate(model = model,
            sequence = chat,
            max_length = config["max_length"],
            tokenizer = tokenizer,
            trust_remote_code = config["trust_remote_code"],
            do_sample=True,   
            temperature = config["temperature"],
            dont_print_output = True,
            )
        return response
    
# cli = Cli()
# cli.launch()


