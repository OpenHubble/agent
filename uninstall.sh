#!/bin/sh

systemctl stop agent-monitoring.service

systemctl disable agent-monitoring.service

rm -f /etc/systemd/system/agent-monitoring.service

systemctl daemon-reload

rm -rf /opt/agent
rm -rf /etc/agent
rm -rf /var/logs/agent

rm -rf /opt/agent/.venv

echo "Amir Monitoring Agent has been uninstalled successfully."
