# Use a lightweight Python image
FROM python:3.10-alpine

# Install required packages
RUN apk add --no-cache \
    gcc \
    libc-dev \
    libffi-dev \
    musl-dev \
    && pip install --upgrade pip

# Set working directory
WORKDIR /app

# Copy your project files into the container
COPY . /app

# Install dependencies from Pipfile and requirements.txt
RUN pip install -r requirements.txt

# Make the /proc and /sys directories accessible
VOLUME ["/proc", "/sys"]

# Run the main.py script
CMD ["python", "main.py"]
