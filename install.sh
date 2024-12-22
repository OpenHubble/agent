#!/bin/sh

set -e
set -u

echo "Updating package lists and installing dependencies..."
apt update -y
apt install -y git python3 python3-venv python3-pip

INSTALL_DIR="/opt/agent"
CONFIG_DIR="/etc/agent"
LOG_DIR="/var/logs/agent"
SERVICE_FILE="/etc/systemd/system/agent-monitoring.service"
REPO_URL="https://gitlab.com/BlackIQ/amir-monitoring-agent"

echo "Cloning repository to $INSTALL_DIR..."
mkdir -p "$INSTALL_DIR"
git clone "$REPO_URL" "$INSTALL_DIR"

echo "Setting up configuration..."
cp "$INSTALL_DIR/agent.ini.example" "$INSTALL_DIR/agent.ini"
mkdir -p "$CONFIG_DIR"
cp "$INSTALL_DIR/agent.ini" "$CONFIG_DIR"

mkdir -p "$LOG_DIR"

echo "Setting up Python virtual environment..."
python3 -m venv "$INSTALL_DIR/.venv"
"$INSTALL_DIR/.venv/bin/python3" -m pip install --no-cache-dir -r "$INSTALL_DIR/requirements.txt"

echo "Setting up systemd service..."
cp "$INSTALL_DIR/agent-monitoring.service" "$SERVICE_FILE"
systemctl daemon-reload
systemctl enable agent-monitoring.service

echo "Starting the agent-monitoring service..."
systemctl start agent-monitoring.service

echo "Installation completed successfully."
