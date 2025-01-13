import docker

def docker_metrics():
    host = docker.from_env()
    running_containers = host.containers.list(all=True)
    
    print(running_containers)
    
docker_metrics()