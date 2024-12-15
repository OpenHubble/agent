from api.main import app

import api.config.config as config

if __name__ == "__main__":
    app.run(config.BIND_IP, port=config.PORT, debug=True)
