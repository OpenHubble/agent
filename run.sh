#!/bin/sh

apt update -y
apt upgrade -y

apt install python3 python3-venv python3-pip -y

mkdir -p /apps
cd /apps

git clone https://gitlab.com/BlackIQ/amir-monitoring-agent agent

cd /apps/agent

cp -r agent.ini.example agent.ini

nano /apps/agent/agent.ini

mkdir -p /etc/agent

cp -r /apps/agent/agent.ini /etc/agent

python3 -m venv .venv

source .venv/bin/activate

pip3 install -r requirements.txt

python3 wsgi.py