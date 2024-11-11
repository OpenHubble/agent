# Variables
IMAGE_NAME=amir-monitoring-agent
TAG=latest
CONTAINER_NAME=amir-monitoring-agent

# Build the Docker image
build:
	docker build -t $(IMAGE_NAME):$(TAG) .

# Run the Docker container
# docker run --name $(CONTAINER_NAME) --detach --network app --restart always $(IMAGE_NAME):$(TAG)
run:
	docker run --rm --privileged -v /proc:/host_proc:ro -v /sys:/host_sys:ro $(IMAGE_NAME):$(TAG)

# Stop the Docker container
stop:
	docker stop $(CONTAINER_NAME) && docker rm $(CONTAINER_NAME)

# Clean up
clean:
	docker rmi $(IMAGE_NAME):$(TAG)

all: stop clean build run
