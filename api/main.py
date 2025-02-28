# FastAPI
from fastapi import FastAPI, Depends # Main
from fastapi.responses import Response # Response
from fastapi.middleware.gzip import GZipMiddleware # Middlewares

# ASYNC
import asyncio

# Message Pack
import msgpack

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
app.add_middleware(GZipMiddleware, minimum_size=500) # Implement use GZIP

async def host_metrics_data():
    tasks = [
        asyncio.to_thread(get_cpu_usage),
        asyncio.to_thread(get_memory_usage),
        asyncio.to_thread(get_swap_usage),
        asyncio.to_thread(get_disk_io),
        asyncio.to_thread(get_network_io),
        asyncio.to_thread(get_system_load),
        asyncio.to_thread(get_disk_space),
    ]
    results = await asyncio.gather(*tasks)
    return {
        "cpu": results[0],
        "memory": results[1],
        "swap": results[2],
        "disk_io": results[3],
        "network_io": results[4],
        "system_load": results[5],
        "disk_space": results[6],
    }

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
    data = await host_metrics_data()
    # packed_data = msgpack.packb(data, use_bin_type=True)
    
    return data
    # return Response(content=packed_data, media_type="application/msgpack")

@app.get("/api/metrics/docker", dependencies=[Depends(allowed_ip)])
async def docker_metrics():
    return {"metrics": get_docker_metrics()}
