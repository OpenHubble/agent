#!/bin/sh

apt update -y
apt upgrade -y

apt install python3 python3-venv python3-pip -y

mkdir -p /apps
cd /apps

git clone https://gitlab.com/BlackIQ/amir-monitoring-agent agent

cd /apps/agent

cp -r agent.ini.example agent.ini

# nano /apps/agent/agent.ini

mkdir -p /etc/agent

cp -r /apps/agent/agent.ini /etc/agent

python3 -m venv .venv

/apps/agent/.venv/bin/python3 -m pip install -r requirements.txt

cp /apps/agent/agent-monitoring.service /etc/systemd/system/

systemctl daemon-reload

systemctl enable agent-monitoring.service

systemctl start agent-monitoring.service
