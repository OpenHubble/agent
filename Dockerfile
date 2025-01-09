# Use an official Python runtime as a base image
FROM python:3.12-slim

# Set environment variables
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH=/opt/openhubble-agent

# Install system dependencies for building packages
RUN apt-get update -y && apt-get install -y \
  build-essential \
  gcc \
  python3-dev \
  libffi-dev \
  libssl-dev \
  && rm -rf /var/lib/apt/lists/*  # Clean up apt cache to reduce image size

# Create and set the working directory
WORKDIR /opt/openhubble-agent

# Copy the requirements file first to leverage Docker cache
COPY requirements.txt /opt/openhubble-agent/

# Install Python dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . /opt/openhubble-agent

# Create directories for logs and config if not already created by the host
RUN mkdir -p /etc/openhubble-agent /var/log/openhubble-agent

# Expose any ports your agent uses (optional, if your agent runs a service)
EXPOSE 9703

# Set the default command
CMD ["python3", "wsgi.py"]