#!/usr/bin/env python3

# Import necessary libraries

import argparse  # Argument parsing
import subprocess  # Executing system commands like systemctl

from art import text2art  # To generate ASCII art
from termcolor import cprint  # Colored terminal printing
from rich.console import Console  # Enhanced terminal output
from rich_gradient import Gradient  # Gradient effects in text output

import api.config.config as config  # Configuration of agent

# Initialize the rich console for pretty output
console = Console()

# Function to print ASCII art
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


# Function to start the service using systemctl
def start():
    cprint("Starting the service...", "green")
    subprocess.run(["sudo", "systemctl", "start", "openhubble-agent.service"])

# Function to stop the service using systemctl
def stop():
    cprint("Stopping the service...", "red")
    subprocess.run(["sudo", "systemctl", "stop", "openhubble-agent.service"])

# Function to restart the service using systemctl
def restart():
    cprint("Restarting the service...", "yellow")
    subprocess.run(["sudo", "systemctl", "restart", "openhubble-agent.service"])

# Function to check the status of the service using systemctl
def status():
    cprint("Checking the service status...", "blue")
    subprocess.run(["sudo", "systemctl", "status", "openhubble-agent.service"])

# Function to show logs from the service, with an option to follow the log output
def logs(follow):
    log_file = "/var/log/openhubble-agent/openhubble-agent.log"
    
    if follow:
        cprint("Showing logs and following the output...", "magenta")
        subprocess.run(["tail", "-f", log_file])  # Follow the logs
    else:
        cprint("Showing logs...", "magenta")
        subprocess.run(["tail", "-n", "10", log_file])  # Show last 10 lines of logs

# Function to update the service by running the update.sh script
def update():
    cprint("Updating the service...", "blue")
    
    # Confirmation prompt
    confirmation = input("Are you sure you want to update the service? (yes/no): ").strip().lower()
    
    if confirmation in ["yes", "y"]:
        update_script = "/opt/openhubble-agent/scripts/update.sh"
        
        subprocess.run(["sudo", update_script])  # Run the update script
        cprint("Service updated successfully.", "green")
    else:
        cprint("Updating aborted.", "yellow")

# Function to uninstall the service with a user confirmation prompt
def uninstall():
    cprint("Uninstalling the service...", "red")
    
    # Confirmation prompt
    confirmation = input("Are you sure you want to uninstall the service? (yes/no): ").strip().lower()
    
    if confirmation in ["yes", "y"]:
        uninstall_script = "/opt/openhubble-agent/scripts/uninstall.sh"
        
        subprocess.run(["sudo", uninstall_script])  # Run the uninstall script
        cprint("Service uninstalled successfully.", "green")
    else:
        cprint("Uninstallation aborted.", "yellow")

# Function to display the version of the service
def version():
    cprint(f"OpenHubble Agent {config.AGENT_VERSION}", "cyan", attrs=["bold"])

# Custom argument parser to enhance the help output
class CustomArgumentParser(argparse.ArgumentParser):
    def print_help(self):
        print_art()
        super().print_help()

# Main function to handle command-line arguments and trigger the corresponding actions
def main():
    # Initialize the argument parser with a description
    parser = CustomArgumentParser(description="OpenHubble CLI Agent Manager.")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Define subcommands and their corresponding help descriptions
    subparsers.add_parser("start", help="Start the service")
    subparsers.add_parser("stop", help="Stop the service")
    subparsers.add_parser("restart", help="Restart the service")
    subparsers.add_parser("status", help="Get the status of the service")

    # Define subcommand for logs, with an optional argument to follow the logs
    logs_parser = subparsers.add_parser("logs", help="Show logs")
    logs_parser.add_argument("-f", "--follow", action="store_true", help="Follow the logs")

    subparsers.add_parser("update", help="Update the service")
    subparsers.add_parser("uninstall", help="Uninstall the service")
    subparsers.add_parser("help", help="Show help information")
    subparsers.add_parser("version", help="Show the version of the service")

    # Parse the arguments passed to the script
    args = parser.parse_args()

    # Handle the execution of different commands based on the user's input
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

# Entry point to execute the script
if __name__ == "__main__":
    main()
