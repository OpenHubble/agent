import argparse
from art import text2art
from termcolor import cprint

from rich.console import Console
from rich_gradient import Gradient

import api.config.config as config

console = Console()

def print_art():
    openhubble_art = text2art("OpenHubble")
    agent_art = text2art("Agent")
    pallete1 = [
        "#8b0000",
        "#dc143c",
        "#ff7f50",
        "#ffc0cb"
    ]
    
    print("\n")

    console.print(
        Gradient(
            openhubble_art,
            colors=pallete1,
            justify="center"
        )
    )
    console.print(
        Gradient(
            agent_art,
            colors=pallete1[::-1],
            justify="center"
        )
    )

def start():
    cprint("Starting the service...", "green")

def stop():
    cprint("Stopping the service...", "red")

def restart():
    cprint("Restarting the service...", "yellow")

def status():
    cprint("Checking the service status...", "blue")

def logs(follow):
    if follow:
        cprint("Showing logs and following the output...", "magenta")
    else:
        cprint("Showing logs...", "magenta")

def update():
    cprint("Updating the service...", "green")

def uninstall():
    cprint("Uninstalling the service...", "red")

def version():
    cprint(f"OpenHubble Agent {config.AGENT_VERSION}", "cyan", attrs=["bold"])

class CustomArgumentParser(argparse.ArgumentParser):
    def print_help(self):
        print_art()
        super().print_help()

def main():
    parser = CustomArgumentParser(description="OpenHubble CLI Agent Manager.")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    subparsers.add_parser("start", help="Start the service")
    subparsers.add_parser("stop", help="Stop the service")
    subparsers.add_parser("restart", help="Restart the service")
    subparsers.add_parser("status", help="Get the status of the service")

    logs_parser = subparsers.add_parser("logs", help="Show logs")
    logs_parser.add_argument("-f", "--follow", action="store_true", help="Follow the logs")

    subparsers.add_parser("update", help="Update the service")
    subparsers.add_parser("uninstall", help="Uninstall the service")
    subparsers.add_parser("help", help="Show help information")
    subparsers.add_parser("version", help="Show the version of the service")

    args = parser.parse_args()

    if args.command == "start":
        start()
    elif args.command == "stop":
        stop()
    elif args.command == "restart":
        restart()
    elif args.command == "status":
        status()
    elif args.command == "logs":
        logs(args.follow)
    elif args.command == "update":
        update()
    elif args.command == "uninstall":
        uninstall()
    elif args.command == "help":
        parser.print_help()
    elif args.command == "version":
        version()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
