# Import Config Parser
import configparser

# Import OS lib
import os

APP_MODE = os.getenv("AGENT_APP_MODE", "PRODUCTION")

IS_PRODUCTION = True if str(APP_MODE) == "PRODUCTION" else False

# Basic stuff
AGENT_VERSION = "1.0.0"

# Config file: Specify Path and name
CONFIG_FILE_NAME = "agent.ini"
CONFIG_FILE_PATH = ""

# Log file: Specify Path and name
LOG_FILE_NAME = "agent.log"
LOG_FILE_PATH = ""

# Check path
if IS_PRODUCTION:
    CONFIG_FILE_PATH = "/etc/agent"
    LOG_FILE_PATH = "/var/logs/agent"
else:
    CONFIG_FILE_PATH = "/Users/amirhosseinmohammadi/Projects/amirhossein/amir-monitoring/agent"
    LOG_FILE_PATH = "."
    
# Log file
LOG_DESTINATION = f"{LOG_FILE_PATH}/{LOG_FILE_NAME}"

# Init Config
config = configparser.ConfigParser()
config.read(f"{CONFIG_FILE_PATH}/{CONFIG_FILE_NAME}")

# ----- Read Configs ----- #

# Server
ALLOWED_IPS = config["Server"]["ALLOWED_IPS"].split(",")

# Agent
BIND_IP = config["Agent"]["BIND_IP"]
PORT = config["Agent"]["PORT"]

# Host
HOST_NAME = config["Host"]["HOSTNAME"]