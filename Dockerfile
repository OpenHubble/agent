# Use a lightweight Python image
FROM python:3.10-alpine

# Install required packages and pipenv
RUN apk add --no-cache \
    gcc \
    libc-dev \
    libffi-dev \
    musl-dev \
    && pip install --upgrade pip \
    && pip install pipenv

# Set working directory
WORKDIR /app

# Copy the Pipfile and Pipfile.lock first to leverage Docker cache
COPY Pipfile Pipfile.lock /app/

# Install dependencies using pipenv
RUN pipenv install --deploy --ignore-pipfile

# Copy the rest of the project files into the container
COPY . /app

# Make the /proc and /sys directories accessible
VOLUME ["/proc", "/sys"]

# Run the main.py script inside the virtual environment
CMD ["pipenv", "run", "python", "main.py"]
