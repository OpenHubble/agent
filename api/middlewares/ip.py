from flask import request, jsonify
from functools import wraps

import ipaddress

import api.config.config as config

def allowed_ip(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        client_ip = request.remote_addr
        
        print(client_ip)
        
        ALLOWED_IP_RANGES = [ipaddress.ip_network(ip.strip()) for ip in config.ALLOWED_IPS]
        
        if not any(ipaddress.ip_address(client_ip) in network for network in ALLOWED_IP_RANGES):
            return jsonify({"error": "Forbidden", "message": "Your IP is not allowed"}), 403
        
        return func(*args, **kwargs)

    return decorated_function
