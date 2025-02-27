from fastapi import HTTPException, Request, Depends
import ipaddress
import api.config.config as config

# Dependency function
def allowed_ip(request: Request):
    client_ip = request.client.host  # Get client IP
    
    # Convert ALLOWED_IPS to a list of ip_network objects
    ALLOWED_IP_RANGES = [ipaddress.ip_network(ip.strip()) for ip in config.ALLOWED_IPS]
    
    # Check if client_ip is in any of the allowed IP ranges
    if not any(ipaddress.ip_address(client_ip) in network for network in ALLOWED_IP_RANGES):
        raise HTTPException(
            status_code=403, 
            detail="Forbidden: Your IP is not allowed"
        )
