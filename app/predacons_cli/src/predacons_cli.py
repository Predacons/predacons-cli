from .cli import Cli
from .rag import VectorStore, WebScraper
import argparse

def launch():
    parser = argparse.ArgumentParser(description="Predacons CLI")
    parser.add_argument('--clear-config', action='store_true', help='Clear the current configuration')
    parser.add_argument('--settings', action='store_true', help='Show settings')
    parser.add_argument('--version', action='store_true', help='Show version')
    # parser.add_argument('--help', action='store_true', help='Show help')
    parser.add_argument('--logs', action='store_true', help='Prints all logs')
    args = parser.parse_args()

    cli = Cli()
    
    if args.clear_config:
        cli.clear_config()
    elif args.settings:
        cli.settings()
    elif args.version:
        cli.version()
    # elif args.help:
    #     cli.help()
    elif args.logs:
        cli.launch(logs =True)
    else:
        cli.launch()