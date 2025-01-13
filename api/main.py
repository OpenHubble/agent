# Import Flask
from flask import Flask, jsonify
from flask_cors import CORS

# Import utils
from api.utils.host.cpu import get_cpu_usage
from api.utils.host.memory import get_memory_usage
from api.utils.host.swap import get_swap_usage
from api.utils.host.disk_io import get_disk_io
from api.utils.host.network_io import get_network_io
from api.utils.host.system_load import get_system_load
from api.utils.host.disk_space import get_disk_space

# Middlewares
from api.middlewares.ip import allowed_ip

# Config
import api.config.config as config

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
        "hostnme": config.HOST_NAME,
        "version": config.AGENT_VERSION,
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

# Host Metrics
@allowed_ip
@app.route('/api/metrics/host', methods=['GET'])
def host_metrics():
    response = {}
    
    metrics = {
        "hostnme": config.HOST_NAME,
        "version": config.AGENT_VERSION,
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

# Docker Metrics
@allowed_ip
@app.route('/api/metrics/docker', methods=['GET'])
def docker_metrics():
    response = {}
    
    metrics = {
        "hostnme": config.HOST_NAME,
        "version": config.AGENT_VERSION,
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

# Handle 404 Error
@app.errorhandler(404)
def not_found(e):
    response = {
        "message": "404 - Not found"
    }

    return jsonify(response), 404