from .cli import Cli
import argparse

def launch():
    parser = argparse.ArgumentParser(description="Predacons CLI")
    parser.add_argument('--load-model', type=str, help='Path to the model to load')
    parser.add_argument('--list-models', action='store_true', help='List available models')
    parser.add_argument('--clear-model', action='store_true', help='Clear the current model')
    parser.add_argument('--settins', action='store_true', help='Show settings')
    args = parser.parse_args()

    cli = Cli()
    if args.load_model:
        cli.load_model(args.load_model)
    elif args.list_models:
        cli.list_models()
    elif args.clear_model:
        cli.clear_model()
    elif args.settings:
        cli.settings()
    else:
        cli.launch()