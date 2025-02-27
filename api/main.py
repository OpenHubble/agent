# Import FastAPI
from fastapi import FastAPI, Depends

# Import your utils and config
from api.utils.host.cpu import get_cpu_usage
from api.utils.host.memory import get_memory_usage
from api.utils.host.swap import get_swap_usage
from api.utils.host.disk_io import get_disk_io
from api.utils.host.network_io import get_network_io
from api.utils.host.system_load import get_system_load
from api.utils.host.disk_space import get_disk_space
from api.utils.docker.docker import get_docker_metrics

# Middleware
from api.middlewares.ip import allowed_ip

# Config
import api.config.config as config

# Init FastAPI app
app = FastAPI()

# IP Middleware as a Dependency
@app.get("/api/ping", dependencies=[Depends(allowed_ip)])
async def ping():
    return {"message": "pong"}

@app.get("/api/metrics", dependencies=[Depends(allowed_ip)])
async def metrics():
    return {
        "metrics": {
            "hostname": config.HOST_NAME,
            "version": config.AGENT_VERSION,
            "cpu": get_cpu_usage(),
            "memory": get_memory_usage(),
            "swap": get_swap_usage(),
            "disk_io": get_disk_io(),
            "network_io": get_network_io(),
            "system_load": get_system_load(),
            "disk_space": get_disk_space(),
        }
    }

@app.get("/api/metrics/host", dependencies=[Depends(allowed_ip)])
async def host_metrics():
    return {
        "metrics": {
            "hostname": config.HOST_NAME,
            "version": config.AGENT_VERSION,
            "cpu": get_cpu_usage(),
            "memory": get_memory_usage(),
            "swap": get_swap_usage(),
            "disk_io": get_disk_io(),
            "network_io": get_network_io(),
            "system_load": get_system_load(),
            "disk_space": get_disk_space(),
        }
    }

@app.get("/api/metrics/docker", dependencies=[Depends(allowed_ip)])
async def docker_metrics():
    return {"metrics": get_docker_metrics()}
