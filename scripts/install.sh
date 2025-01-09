#!/bin/bash

# Ensure the script is run as root
if [ "$EUID" -ne 0 ]; then
  echo "Please run this script as root (use sudo)"
  exit 1
fi

# Update packages
apt update -y

# Install some requirements
apt install -y git python3 python3-venv python3-pip

# Create directories
echo "Creating directories..."
mkdir -p /opt/openhubble-agent # App source
mkdir -p /etc/openhubble-agent # Configurations
mkdir -p /var/log/openhubble-agent # Logs

# Change directory to source directory
cd /opt/openhubble-agent

# Clone the project using git
echo "Cloning the project..."
git clone https://github.com/OpenHubble/agent . || {
  echo "Git clone failed."
  exit 1
}

# Copy the config file to the config directory
echo "Setting up configurations..."
cp example/agent.ini.example /etc/openhubble-agent/openhubble-agent.ini || {
  echo "Failed to copy configuration file."
  exit 1
}

# Create a hidden virtual environment
echo "Creating virtual environment..."
python3 -m venv .venv || {
  echo "Failed to create virtual environment."
  exit 1
}

# Install app modules
echo "Installing modules..."
/opt/openhubble-agent/.venv/bin/python3 -m pip install --no-cache-dir -r requirements.txt || {
  echo "Failed to install Python modules."
  exit 1
}

# Copy the service file for systemctl
echo "Setting up service..."
cp /opt/openhubble-agent/openhubble-agent.service /etc/systemd/system/ || {
  echo "Failed to copy service file."
  exit 1
}

# Reload Daemon
echo "Reloading services..."
systemctl daemon-reload

echo "OpenHubble Agent has been installed successfully."
