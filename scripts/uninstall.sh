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

# Reload Daemon to remove any lingering references to the service
echo "Reloading systemd daemon..."
systemctl daemon-reload

# Ask for confirmation before removing directories
echo "This will remove the following directories:"
echo "/opt/openhubble-agent (Agent source)"
echo "/etc/openhubble-agent (Configuration files)"
echo "/var/log/openhubble-agent (Logs)"
echo "Are you sure you want to continue? (y/n)"
read -r CONFIRM

if [[ "$CONFIRM" =~ ^[Yy]$ ]]; then
  # Remove directories
  echo "Removing agent files..."
  rm -rf /opt/openhubble-agent
  rm -rf /etc/openhubble-agent
  rm -rf /var/log/openhubble-agent
else
  echo "Uninstallation aborted. Files were not deleted."
  exit 1
fi

# Remove the symbolic link for openhubble-agent
echo "Removing symbolic link..."
rm -f /usr/local/bin/openhubble-agent

echo "OpenHubble Agent has been uninstalled successfully."
