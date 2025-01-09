#!/bin/bash

# Ensure the script is run as root
if [ "$EUID" -ne 0 ]; then
  echo "Please run this script as root (use sudo)"
  exit 1
fi

# Stop the service using systemctl
echo "Stopping service..."
systemctl stop openhubble-agent.service || echo "Service not running."

# Disable the service
echo "Disabling service..."
systemctl disable openhubble-agent.service || echo "Service already disabled."

# Remove the service file
echo "Removing service..."
rm -f /etc/systemd/system/openhubble-agent.service

# Reload Daemon
echo "Reloading services..."
systemctl daemon-reload

# Remove directories
echo "Removing agent files..."
rm -rf /opt/openhubble-agent
rm -rf /etc/openhubble-agent
rm -rf /var/log/openhubble-agent

echo "OpenHubble Agent has been uninstalled successfully."
