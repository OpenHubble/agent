# Use an official Python runtime as a base image
FROM python:3.12-slim

# Set environment variables
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH=/opt/openhubble-agent

# Install system dependencies
RUN apt-get update -y && apt-get install -y \
  python3-venv \
  python3-pip

# Create and set the working directory
WORKDIR /opt/openhubble-agent

# Copy the contents of the current directory (the agent repository) into the container
COPY . /opt/openhubble-agent

# Create the virtual environment
RUN python3 -m venv .venv

# Install Python dependencies
RUN ./.venv/bin/pip3 install --no-cache-dir -r requirements.txt

# Expose any ports your agent uses (optional, if your agent runs a service)
EXPOSE 9703

# Copy the wrapper.sh file to make the CLI command available
# COPY cli/wrapper.sh /usr/local/bin/openhubble-agent

# Make wrapper.sh executable
# RUN chmod +x /usr/local/bin/openhubble-agent

# Create directories for logs and config if not already created by host
RUN mkdir -p /etc/openhubble-agent /var/log/openhubble-agent

# Make sure to mount the host's /proc, /sys, /dev and other directories during runtime
# VOLUME ["/host_proc", "/host_sys", "/host_dev", "/etc/openhubble-agent", "/var/log/openhubble-agent"]

# Set the default command
CMD ["/opt/openhubble-agent/.venv/bin/python3", "wsgi.py"]
