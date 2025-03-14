import asyncio
import logging

from api.events.client import push_event
from api.events.triggers import sync_triggers, get_triggers

from api.main import host_metrics_data
from api.utils.docker.docker import get_docker_metrics

from api.config import config

logger = logging.getLogger("uvicorn")

state = {"cpu_high": False, "containers": {}}

def evaluate_condition(condition, data):
    """Evaluate a trigger condition (e.g., 'cpu_percentage > 85')."""
    
    key, op, value = condition.split()
    value = float(value) if "." in value else int(value)
    data_value = data.get(key)
    if op == ">":
        return data_value > value
    elif op == "<=":
        return data_value <= value
    elif op == "==":
        return data_value == value
    return False

async def monitor_metrics():
    """Monitor metrics and push events to Survey."""
    
    while True:
        await sync_triggers()
        host_data = await host_metrics_data()
        cpu_data = {"cpu_percentage": host_data["cpu"]["total_usage"]}

        triggers = get_triggers()
        for name, input, condition, message in triggers:
            if "cpu" in name:
                data = cpu_data
                if evaluate_condition(condition, data):
                    if name == "cpu_utilization_trigger" and not state["cpu_high"]:
                        await push_event(name, data)
                        state["cpu_high"] = True
                    elif name == "cpu_normal_trigger" and state["cpu_high"]:
                        await push_event(name, data)
                        state["cpu_high"] = False

            # Docker metrics
            docker_data = get_docker_metrics()
            for container in docker_data:
                container_id = container["id"]
                container_data = {
                    "id": container_id,
                    "name": container["name"],
                    "status": container["status"],
                    "health": container["health"]
                }
                prev_state = state["containers"].get(container_id, {"status": None, "health": None})

                if "container" in name and evaluate_condition(condition, container_data):
                    if (name == "container_down_trigger" and prev_state["status"] != "exited") or \
                       (name == "container_health_trigger" and prev_state["health"] != "unhealthy") or \
                       (name == "container_up_trigger" and prev_state["status"] != "running"):
                        await push_event(name, container_data)
                state["containers"][container_id] = {"status": container["status"], "health": container["health"]}

        await asyncio.sleep(config.MONITOR_INTERVAL)
