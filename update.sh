#!/bin/sh

set -e

cd /opt/agent

echo "Pulling latest changes from Git..."
git pull origin main

echo "Updating Python dependencies..."
/opt/agent/.venv/bin/python3 -m pip install --no-cache-dir -r requirements.txt

echo "Clearing Python cache..."
find /opt/agent -name "*.pyc" -delete
find /opt/agent -name "__pycache__" -delete

echo "Restarting the service..."
systemctl daemon-reload
systemctl restart agent-monitoring.service

echo "Update complete!"
