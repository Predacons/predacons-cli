import predacons
import os
from rich import print
from rich.prompt import Prompt
import json
import logging
import time
from rich.table import Table


logging.getLogger("transformers").setLevel(logging.ERROR)


class Cli:
    def __init__(self):
        self.predacons = predacons

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
        if logs == False:
            print("[yellow]Model loaded poperly Clearing logs in 3 sec to keep the logs start predacons with --logs [/yellow]")
            for i in range(3, 0, -1):
                time.sleep(1)
            os.system('clear')  # Clear the screen
        
        print("[i]Welcome to the Predacons CLI![/i] [green]Model: [orange1]"+config["model_path"]+"[/orange1] loaded successfully![/green]")
        print("[yellow]You can start chatting with Predacons now.Type 'clear' to clear history, Type 'exit' to quit, Type 'help' for more options,[/yellow]")
        while True:
            user_input = Prompt.ask("[green]User[/green]")
            user_body = {"role": "user", "content": user_input} 

            chat.append(user_body)
            if user_input == "exit":
                break
            elif user_input == "clear":
                chat = []
                print("[yellow]Chat history cleared![/yellow]")
            elif user_input == "help":
                print("[yellow]Type 'clear' to clear history, Type 'exit' to quit, Type 'help' for more options,[/yellow]")
            else:
                response = Cli.generate_response(self, chat, model, tokenizer, config)
                response_body = {"role": "assistant", "content": response}
                chat.append(response_body)
                print("[orange1]Predacons: [/orange1] [blue]" + response+"[/blue]")

    
    def load_model(self, model_path,trust_remote_code=False,use_fast_generation=False, draft_model_name=None,gguf_file=None,auto_quantize=None):
        model = self.predacons.load_model(model_path,trust_remote_code=trust_remote_code,use_fast_generation=use_fast_generation, draft_model_name=draft_model_name,gguf_file=gguf_file,auto_quantize=auto_quantize)
        tokenizer = self.predacons.load_tokenizer(model_path,gguf_file=gguf_file)
        return model, tokenizer
        
    def clear_config(self):
        file_path = 'predacon_cli_config.json'
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
        file_path = 'predacon_cli_config.json'

        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                config_data = json.load(file)
        self.print_config_data(config_data)
        update = Prompt.ask("Do you want to update settings?", choices=["y", "n"],default="n")
        if update == "y":
            config_data = Cli.create_config_file(self)
            self.print_config_data(config_data)

    def version(self):
        print("[blue]Predacons CLI version 0.0.1[blue]")
    
    def help(self):
        print("[yellow]Type 'clear' to clear history, Type 'exit' to quit, Type 'help' for more options,[/yellow]")
        print("[yellow]--clear-config: Clear the current configuration[/yellow]")
        print("[yellow]--settings: Show settings[/yellow]")
        print("[yellow]--version: Show version[/yellow]")
        print("[yellow]--help: Show help[/yellow]")
        print("[yellow]--logs: Prints all logs[/yellow]")

    def check_config_file(self):
        file_path = 'predacon_cli_config.json'

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
        file_path = 'predacon_cli_config.json'
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
            model_path = Prompt.ask("Enter the model path or hugging face model name")
            trust_remote_code = Prompt.ask("Trust remote code? (true/false)", default="false")
            use_fast_generation = Prompt.ask("Use fast generation? (true/false)", default="false")
            if use_fast_generation.lower() == 'true':
                draft_model_name = Prompt.ask("Enter the draft model name (optional)", default="")
            auto_quantize = Prompt.ask("Enable auto quantize? (true/false)", default="false")
        
        elif model_type == '2':
            model_path = Prompt.ask("Enter the model path or hugging face model name")
            gguf_file = Prompt.ask("Enter the GGUF file path/name", default="")
            trust_remote_code = Prompt.ask("Trust remote code? (true/false)", default="false")
            auto_quantize = Prompt.ask("Enable auto quantize? (true/false)", default="false")

        elif model_type == '3':
            print("[yellow]Not supported yet adding soon... for now try default model[/yellow]")
            model_path = Prompt.ask("Enter the model path or hugging face model name")
            trust_remote_code = Prompt.ask("Trust remote code? (true/false)", default="false")
            use_fast_generation = Prompt.ask("Use fast generation? (true/false)", default="false")
            if use_fast_generation.lower() == 'true':
                draft_model_name = Prompt.ask("Enter the draft model name (optional)", default="")
            auto_quantize = Prompt.ask("Enable auto quantize? (true/false)", default="false")
        else :
            print("[red]Invalid model type selected![/red]")
            return
        
        temperature = Prompt.ask("Enter the temperature", default="0.3")
        max_length = Prompt.ask("Enter the max length for each response", default="1000")
        top_k = Prompt.ask("Enter the top k value", default="50")
        top_p = Prompt.ask("Enter the top p value", default="0.9")
        repetition_penalty = Prompt.ask("Enter the repetition penalty value", default="1.0")
        num_return_sequences = Prompt.ask("Enter the number of return sequences", default="1")



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
            "num_return_sequences": int(num_return_sequences)
        }
        
        with open(file_path, 'w') as f:
            json.dump(config_data, f, indent=4)
        
        print("[green]Configuration file created successfully![/green]")
        return config_data

    def load_config_file(self):
        file_path = 'predacon_cli_config.json'
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


