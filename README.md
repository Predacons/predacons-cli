# Predacons CLI

Welcome to the **Predacons CLI**! This command-line interface (CLI) allows you to interact with the Predacons library, providing a seamless way to load models, generate responses, and manage configurations directly from your terminal.

## Features

- **Model Management**: Load and manage different types of models including local, Hugging Face safetensor, PyTorch, and GGUF models.
- **Interactive Chat**: Engage in interactive chat sessions with the loaded model.
- **Vector store**: Supports vector store allowing user to have conversation with any document or any unstructured data source
- **Web Scraper**: It can makes google search and answer based on the search results
- **Configuration Management**: Easily create, update, and clear configuration files.
- **Rich Output**: Utilize rich text formatting for better readability and user experience.
- **Logging**: Optionally enable logging for debugging and tracking purposes.

## Installation

To install the Predacons CLI, you need to have Python installed on your system. You can install the required dependencies using `pip`:

```sh
pip install predacons-cli
```

## Usage

### Launching the CLI

To start the Predacons CLI, simply run:

```sh
predacons
```

### Commands

Once the CLI is launched, you can use the following commands:

- [`clear`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fhome%2Fshourya%2Fcode_wsl%2FGitHub%2FPredacons-git%2Fpredacons-cli%2Fapp%2Fpredacons_cli%2Fsrc%2Fcli.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A56%2C%22character%22%3A23%7D%7D%5D%2C%22a3ad2ba0-b6df-4b55-96bb-4cbb30225959%22%5D "Go to definition"): Clear the chat history.
- [`exit`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fhome%2Fshourya%2Fcode_wsl%2FGitHub%2FPredacons-git%2Fpredacons-cli%2Fapp%2Fpredacons_cli%2Fsrc%2Fcli.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A59%2C%22character%22%3A102%7D%7D%5D%2C%22a3ad2ba0-b6df-4b55-96bb-4cbb30225959%22%5D "Go to definition"): Quit the CLI.
- `clear-config`: Clear the current configuration file.
- [`settings`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fhome%2Fshourya%2Fcode_wsl%2FGitHub%2FPredacons-git%2Fpredacons-cli%2Fapp%2Fpredacons_cli%2Fsrc%2Fcli.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A73%2C%22character%22%3A20%7D%7D%5D%2C%22a3ad2ba0-b6df-4b55-96bb-4cbb30225959%22%5D "Go to definition"): Show and update settings.
- [`version`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fhome%2Fshourya%2Fcode_wsl%2FGitHub%2FPredacons-git%2Fpredacons-cli%2Fapp%2Fpredacons_cli%2Fsrc%2Fcli.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A75%2C%22character%22%3A20%7D%7D%5D%2C%22a3ad2ba0-b6df-4b55-96bb-4cbb30225959%22%5D "Go to definition"): Display the current version of the Predacons CLI.
- [`help`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fhome%2Fshourya%2Fcode_wsl%2FGitHub%2FPredacons-git%2Fpredacons-cli%2Fapp%2Fpredacons_cli%2Fsrc%2Fcli.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A131%2C%22character%22%3A8%7D%7D%5D%2C%22a3ad2ba0-b6df-4b55-96bb-4cbb30225959%22%5D "Go to definition"): Show help information.
- `update`: updates the documents to the vector db

### Example Session

```sh
$ predacons
Welcome to the Predacons CLI!
No config file found. Creating one now...
Creating a new configuration file...
Please enter the following details to create a new configuration file
...
Welcome to the Predacons CLI! Model: Precacons/Pico-Lamma-3.2-1B-Reasoning-Instruct loaded successfully!
You can start chatting with Predacons now. Type 'clear' to clear history, Type 'exit' to quit, Type 'help' for more options,
User: Hello!
Predacons: Hi there! How can I assist you today?
```

## Configuration

The configuration file is stored at `~/.predacons_cli/predacon_cli_config.json`. You can update the configuration settings by using the [`settings`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fhome%2Fshourya%2Fcode_wsl%2FGitHub%2FPredacons-git%2Fpredacons-cli%2Fapp%2Fpredacons_cli%2Fsrc%2Fcli.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A73%2C%22character%22%3A20%7D%7D%5D%2C%22a3ad2ba0-b6df-4b55-96bb-4cbb30225959%22%5D "Go to definition") command within the CLI.

### Configuration Options

- [`model_path`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fhome%2Fshourya%2Fcode_wsl%2FGitHub%2FPredacons-git%2Fpredacons-cli%2Fapp%2Fpredacons_cli%2Fsrc%2Fcli.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A90%2C%22character%22%3A25%7D%7D%5D%2C%22a3ad2ba0-b6df-4b55-96bb-4cbb30225959%22%5D "Go to definition"): Path to the model or Hugging Face model name.
- [`trust_remote_code`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fhome%2Fshourya%2Fcode_wsl%2FGitHub%2FPredacons-git%2Fpredacons-cli%2Fapp%2Fpredacons_cli%2Fsrc%2Fcli.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A90%2C%22character%22%3A36%7D%7D%5D%2C%22a3ad2ba0-b6df-4b55-96bb-4cbb30225959%22%5D "Go to definition"): Boolean to trust remote code.
- [`use_fast_generation`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fhome%2Fshourya%2Fcode_wsl%2FGitHub%2FPredacons-git%2Fpredacons-cli%2Fapp%2Fpredacons_cli%2Fsrc%2Fcli.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A90%2C%22character%22%3A60%7D%7D%5D%2C%22a3ad2ba0-b6df-4b55-96bb-4cbb30225959%22%5D "Go to definition"): Boolean to enable fast generation.
- [`draft_model_name`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fhome%2Fshourya%2Fcode_wsl%2FGitHub%2FPredacons-git%2Fpredacons-cli%2Fapp%2Fpredacons_cli%2Fsrc%2Fcli.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A90%2C%22character%22%3A87%7D%7D%5D%2C%22a3ad2ba0-b6df-4b55-96bb-4cbb30225959%22%5D "Go to definition"): Optional draft model name.
- [`gguf_file`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fhome%2Fshourya%2Fcode_wsl%2FGitHub%2FPredacons-git%2Fpredacons-cli%2Fapp%2Fpredacons_cli%2Fsrc%2Fcli.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A90%2C%22character%22%3A109%7D%7D%5D%2C%22a3ad2ba0-b6df-4b55-96bb-4cbb30225959%22%5D "Go to definition"): Path to the GGUF file.
- [`auto_quantize`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fhome%2Fshourya%2Fcode_wsl%2FGitHub%2FPredacons-git%2Fpredacons-cli%2Fapp%2Fpredacons_cli%2Fsrc%2Fcli.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A90%2C%22character%22%3A124%7D%7D%5D%2C%22a3ad2ba0-b6df-4b55-96bb-4cbb30225959%22%5D "Go to definition"): Boolean to enable auto quantization.
- [`temperature`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fhome%2Fshourya%2Fcode_wsl%2FGitHub%2FPredacons-git%2Fpredacons-cli%2Fapp%2Fpredacons_cli%2Fsrc%2Fcli.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A218%2C%22character%22%3A8%7D%7D%5D%2C%22a3ad2ba0-b6df-4b55-96bb-4cbb30225959%22%5D "Go to definition"): Temperature setting for response generation.
- [`max_length`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fhome%2Fshourya%2Fcode_wsl%2FGitHub%2FPredacons-git%2Fpredacons-cli%2Fapp%2Fpredacons_cli%2Fsrc%2Fcli.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A219%2C%22character%22%3A8%7D%7D%5D%2C%22a3ad2ba0-b6df-4b55-96bb-4cbb30225959%22%5D "Go to definition"): Maximum length for each response.
- [`top_k`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fhome%2Fshourya%2Fcode_wsl%2FGitHub%2FPredacons-git%2Fpredacons-cli%2Fapp%2Fpredacons_cli%2Fsrc%2Fcli.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A220%2C%22character%22%3A8%7D%7D%5D%2C%22a3ad2ba0-b6df-4b55-96bb-4cbb30225959%22%5D "Go to definition"): Top K value for response generation.
- [`top_p`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fhome%2Fshourya%2Fcode_wsl%2FGitHub%2FPredacons-git%2Fpredacons-cli%2Fapp%2Fpredacons_cli%2Fsrc%2Fcli.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A221%2C%22character%22%3A8%7D%7D%5D%2C%22a3ad2ba0-b6df-4b55-96bb-4cbb30225959%22%5D "Go to definition"): Top P value for response generation.
- [`repetition_penalty`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fhome%2Fshourya%2Fcode_wsl%2FGitHub%2FPredacons-git%2Fpredacons-cli%2Fapp%2Fpredacons_cli%2Fsrc%2Fcli.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A222%2C%22character%22%3A8%7D%7D%5D%2C%22a3ad2ba0-b6df-4b55-96bb-4cbb30225959%22%5D "Go to definition"): Repetition penalty value.
- [`num_return_sequences`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fhome%2Fshourya%2Fcode_wsl%2FGitHub%2FPredacons-git%2Fpredacons-cli%2Fapp%2Fpredacons_cli%2Fsrc%2Fcli.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A223%2C%22character%22%3A8%7D%7D%5D%2C%22a3ad2ba0-b6df-4b55-96bb-4cbb30225959%22%5D "Go to definition"): Number of return sequences.
- [`print_as_markdown`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fhome%2Fshourya%2Fcode_wsl%2FGitHub%2FPredacons-git%2Fpredacons-cli%2Fapp%2Fpredacons_cli%2Fsrc%2Fcli.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A224%2C%22character%22%3A8%7D%7D%5D%2C%22a3ad2ba0-b6df-4b55-96bb-4cbb30225959%22%5D "Go to definition"): Boolean to print response as markdown.
- `chat_with_data`: enable vector db
- `vector_db_path`: path to the vector store
- `document_path`: path to the directory containing the documents
- `embedding_model`: embedding model id or path
- `scrap_web`: enable web scraping
## Logging

To enable logging, launch the CLI with the `--logs` flag:

```sh
python cli.py --logs
```

## License

This project is licensed under the MIT License. See the [`LICENSE`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fhome%2Fshourya%2Fcode_wsl%2FGitHub%2FPredacons-git%2Fpredacons-cli%2FLICENSE%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22a3ad2ba0-b6df-4b55-96bb-4cbb30225959%22%5D "/home/shourya/code_wsl/GitHub/Predacons-git/predacons-cli/LICENSE") file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request on GitHub.

## Contact

For any questions or support, please open an issue on the GitHub repository.

---

Enjoy using the Predacons CLI! 🚀
