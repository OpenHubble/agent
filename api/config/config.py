# Import Config Parser
import configparser

# Import TOML
import toml

# Import OS lib
import os

APP_MODE = os.getenv("AGENT_APP_MODE", "PRODUCTION")

IS_PRODUCTION = True if str(APP_MODE) == "PRODUCTION" else False

# Project Directory
PROJECT_DIRECTORY = ""

# Config file: Specify Path and name
CONFIG_FILE_PATH = ""
CONFIG_FILE_NAME = "openhubble-agent.ini"

# Log file: Specify Path and name
LOG_FILE_PATH = ""
LOG_API_FILE_NAME = "openhubble-agent.log"
# LOG_APP_FILE_NAME = "openhubble-agent-app.log"

# Project config file path
PROJECT_CONFIG_FILE = "pyproject.toml"

# Check path
if IS_PRODUCTION:
    PROJECT_DIRECTORY = "/opt/openhubble-agent"
    CONFIG_FILE_PATH = "/etc/openhubble-agent"
    LOG_FILE_PATH = "/var/log/openhubble-agent"
else:
    PROJECT_DIRECTORY = "./test"
    CONFIG_FILE_PATH = "./test/dev/config"
    LOG_FILE_PATH = "./test/dev/log"
    
# Log file
LOG_API_DESTINATION = f"{LOG_FILE_PATH}/{LOG_API_FILE_NAME}"
# LOG_APP_DESTINATION = f"{LOG_FILE_PATH}/{LOG_APP_FILE_NAME}"

# Init Config
config = configparser.ConfigParser()
config.read(f"{CONFIG_FILE_PATH}/{CONFIG_FILE_NAME}")

# Read the TOML project config file
project_config = toml.load(f"{PROJECT_DIRECTORY}/{PROJECT_CONFIG_FILE}")

# ----- Read Project Configs (TOML) ----- #
PROJECT_NAME = project_config.get("tool", {}).get("openhubble", {}).get("name", "N/A")
PROJECT_VERSION = project_config.get("tool", {}).get("openhubble", {}).get("version", "N/A")

AGENT_VERSION = PROJECT_VERSION

# ----- Read User Configs (INI) ----- #
ALLOWED_IPS = config["Server"]["ALLOWED_IPS"].split(",") if "Server" in config else []
BIND_IP = config["Agent"]["BIND_IP"] if "Agent" in config else "0.0.0.0"
PORT = config["Agent"]["PORT"] if "Agent" in config else "9703"
HOST_NAME = config["Host"]["HOSTNAME"] if "Host" in config else "localhost"