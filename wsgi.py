from api.main import app

import api.config.config as config

if __name__ == "__main__":
    app.run("0.0.0.0", port=config.APP_PORT, debug=True)