#!/bin/bash

# Ensure the script is run as root
if [ "$EUID" -ne 0 ]; then
  echo "Please run this script as root (use sudo)"
  exit 1
fi

set -e

# Set install directory
INSTALL_DIR="/opt/openhubble-agent"

# Get the latest release tag from GitHub
LATEST_VERSION=$(curl -s "https://api.github.com/repos/OpenHubble/agent/releases/latest" | jq -r '.tag_name')

if [ -z "$LATEST_VERSION" ] || [ "$LATEST_VERSION" == "null" ]; then
  echo "Failed to get latest version."
  exit 1
fi

TARBALL_URL="https://api.github.com/repos/OpenHubble/agent/tarball/$LATEST_VERSION"

echo "Updating OpenHubble Agent to version $LATEST_VERSION..."

# Change directory to source directory
cd "$INSTALL_DIR" || {
  echo "Source directory not found."
  exit 1
}

# Backup existing installation (optional, in case you need to roll back)
echo "Backing up current installation..."
tar -czf "/tmp/openhubble-agent-backup-$LATEST_VERSION.tar.gz" "$INSTALL_DIR"

# Preserve the db directory (move it out temporarily)
if [ -d "$INSTALL_DIR/db" ]; then
  echo "Preserving database directory..."
  mv "$INSTALL_DIR/db" /tmp/openhubble-agent-db-backup
fi

# Remove existing files except db (already moved)
echo "Removing old files..."
rm -rf "$INSTALL_DIR"/*

# Download and extract the latest version
curl -L "$TARBALL_URL" -o /tmp/openhubble-agent.tar.gz
tar -xzf /tmp/openhubble-agent.tar.gz --strip-components=1 -C "$INSTALL_DIR"

# Restore the db directory or create it if it didn’t exist
if [ -d "/tmp/openhubble-agent-db-backup" ]; then
  echo "Restoring database directory..."
  mv /tmp/openhubble-agent-db-backup "$INSTALL_DIR/db"
else
  echo "Creating new database directory..."
  mkdir -p "$INSTALL_DIR/db"
fi

# Set permissions for db directory (match install.sh)
chown -R root:root "$INSTALL_DIR/db"  # Adjust to your service user if not root
chmod 755 "$INSTALL_DIR/db"

# Recreate the virtual environment
echo "Recreating virtual environment..."
python3 -m venv "$INSTALL_DIR/.venv"

# Install Python dependencies
echo "Installing Python dependencies..."
"$INSTALL_DIR/.venv/bin/python3" -m pip install --no-cache-dir -r "$INSTALL_DIR/requirements.txt"

# Only copy config if it doesn’t already exist (preserve user changes)
echo "Checking configurations..."
if [ ! -f "/etc/openhubble-agent/openhubble-agent.ini" ]; then
  cp "$INSTALL_DIR/example/openhubble.ini.example" /etc/openhubble-agent/openhubble-agent.ini || {
    echo "Failed to copy configuration file."
    exit 1
  }
else
  echo "Existing configuration preserved at /etc/openhubble-agent/openhubble-agent.ini"
fi

# Make the Agent executable
chmod +x "$INSTALL_DIR/cli/wrapper.sh"

# Reload the Daemon
echo "Reloading services..."
systemctl daemon-reload

# Restart the service
echo "Restarting the service..."
systemctl restart openhubble-agent.service || {
  echo "Failed to restart the service."
  exit 1
}

echo "OpenHubble Agent has been updated to version $LATEST_VERSION successfully."