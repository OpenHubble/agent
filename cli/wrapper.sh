#!/bin/bash

export PYTHONPATH=/opt/openhubble-agent

/opt/openhubble-agent/.venv/bin/python3 /opt/openhubble-agent/cli/cli.py "$@"
