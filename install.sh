#!/bin/sh

apt update -y

apt install git python3 python3-venv python3-pip -y

mkdir -p /opt
cd /opt

git clone https://gitlab.com/BlackIQ/amir-monitoring-agent agent

cd /opt/agent

cp -r agent.ini.example agent.ini

# nano /opt/agent/agent.ini

mkdir -p /etc/agent
mkdir -p /var/logs/agent

cp -r /opt/agent/agent.ini /etc/agent

python3 -m venv .venv

/opt/agent/.venv/bin/python3 -m pip install -r requirements.txt

cp /opt/agent/agent-monitoring.service /etc/systemd/system/

systemctl daemon-reload

systemctl enable agent-monitoring.service

systemctl start agent-monitoring.service
