# Logging
import logging
from logging.handlers import RotatingFileHandler

# Use proccessing
import multiprocessing

# Uvicorn
import uvicorn

# Main API
from api.main import app

# Config
import api.config.config as config

# Setup logging
log_file = config.LOG_DESTINATION

handler = RotatingFileHandler(log_file, maxBytes=5 * 1024 * 1024, backupCount=5)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
handler.setLevel(logging.INFO)

logger = logging.getLogger("uvicorn")
logger.addHandler(handler)
logger.setLevel(logging.INFO)

logger.info("Agent application started!")
logger.info(f"Agent Version: {config.AGENT_VERSION}")
logger.info("OpenHubble By Amirhossein Mohammadi - 2025")

# Run the ASGI server
if __name__ == "__main__":
    num_workers = multiprocessing.cpu_count() # Cound of proccessors
    print(num_workers)
    uvicorn.run("asgi:app", host=config.BIND_IP, port=int(config.PORT), workers=num_workers)
