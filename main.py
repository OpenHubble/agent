import requests
import time
import json

from utils.cpu import get_cpu_usage
from utils.memory import get_memory_usage
from utils.swap import get_swap_usage
from utils.disk_io import get_disk_io
from utils.network_io import get_network_io
from utils.system_load import get_system_load
from utils.disk_space import get_disk_space

from config.config import API_ENDPOINT, SERVER_ID, ACCESS_TOKEN

def send_metrics_to_server(metrics):
    try:
        payload = json.dumps(metrics)
        headers = {
            'accessToken': ACCESS_TOKEN,
            'serverID': SERVER_ID,
            'Content-Type': 'application/json',
        }
        
        response = requests.post(API_ENDPOINT, data=payload, headers=headers)

        if response.status_code == 200:
            print("Metrics sent successfully")
        else:
            print("Failed to send metrics")
    except Exception as e:
        print("Error sending metrics to the server:", str(e))

def main():
    try:
        while True:
            metrics = {
                "cpu": get_cpu_usage(),
                "memory": get_memory_usage(),
                "swap": get_swap_usage(),
                "disk_io": get_disk_io(),
                "network_io": get_network_io(),
                "system_load": get_system_load(),
                "disk_space": get_disk_space(),
            }
                        
            send_metrics_to_server(metrics)
                        
            time.sleep(1)
    except Exception as e:
        print("Error during data collection or transmission:", str(e))

if __name__ == "__main__":
    main()
