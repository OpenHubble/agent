# Import Flask
from flask import Flask, jsonify
from flask_cors import CORS

# Import utils
from api.utils.cpu import get_cpu_usage
from api.utils.memory import get_memory_usage
from api.utils.swap import get_swap_usage
from api.utils.disk_io import get_disk_io
from api.utils.network_io import get_network_io
from api.utils.system_load import get_system_load
from api.utils.disk_space import get_disk_space

# Middlewares
from api.middlewares.ip import allowed_ip

# Init app
app = Flask(__name__)

# Set CORS
CORS(app)

# Ping
@allowed_ip
@app.route('/api/ping', methods=['GET'])
def ping():
    response = {}

    response['message'] = "pong"

    return jsonify(response), 200

# Metrics
@allowed_ip
@app.route('/api/metrics', methods=['GET'])
def metrics():
    response = {}
    
    metrics = {
        "cpu": get_cpu_usage(),
        "memory": get_memory_usage(),
        "swap": get_swap_usage(),
        "disk_io": get_disk_io(),
        "network_io": get_network_io(),
        "system_load": get_system_load(),
        "disk_space": get_disk_space(),
    }

    response['metrics'] = metrics

    return jsonify(response), 200