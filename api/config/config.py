# Import Config Parser
import configparser

# Specify Path and name
CONFIG_FILE_NAME = "agent.ini"
CONFIG_FILE_PATH = "/Users/amirhosseinmohammadi/Projects/amirhossein/amir-monitoring/agent"

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
