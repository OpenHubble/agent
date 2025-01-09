# Logging
import logging
from logging.handlers import RotatingFileHandler

# Main API
from api.main import app

# Config
import api.config.config as config

log_file = config.LOG_DESTINATION

handler = RotatingFileHandler(log_file, maxBytes=5 * 1024 * 1024, backupCount=5)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
handler.setLevel(logging.INFO)

app.logger.addHandler(handler)
app.logger.setLevel(logging.INFO)

flask_log = logging.getLogger('werkzeug')
flask_log.addHandler(handler)
flask_log.setLevel(logging.INFO)

app.logger.info("Agent application started!")
app.logger.info(f"Agent Version: {config.AGENT_VERSION}")
app.logger.info("OpenHubble LTD By Amirhossein Mohammadi - 2024")

if __name__ == "__main__":
    app.run(config.BIND_IP, port=config.PORT, debug=True)
