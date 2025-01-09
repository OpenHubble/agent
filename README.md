# OpenHubble Monitoring Agent

Lightweight **monitoring agent** written in **Python** with **Flask**, designed to collect system metrics and expose an API for data retrieval and visualization. Includes installation, configuration, update, and uninstallation guides.

## Installing the Agent

To install the **OpenHubble Agent**, follow these steps:

### 1. Download and Run the Installation Script
Use `curl` to fetch the installation script and run it with **root** privileges:

```bash
curl -s https://get.openhubble.com | sudo bash
```

This script will:
- Update your system's packages.
- Install required dependencies (`git`, `python3`, `python3-venv`, and `python3-pip`).
- Clone the **OpenHubble agent** repository.
- Set up the required directories and configurations.
- Create a Python virtual environment and install the necessary Python modules.
- Set up a systemd service for the **OpenHubble agent**.

### 2. Configure the Agent
After the installation, you need to configure the **agent**. Edit the configuration file located at:

```bash
sudo nano /etc/openhubble-agent/openhubble-agent.ini
```

Update the configuration values according to your system and monitoring requirements. Save and close the file when done.

### 3. Enable the Service
To ensure the **agent** starts automatically after a reboot, enable the service:

```bash
sudo systemctl enable openhubble-agent.service
```

### 4. Restart the Service
After editing the configuration file, restart the service to apply the changes:

```bash
sudo systemctl restart openhubble-agent.service
```

### 5. Verify Installation
To confirm the agent is running, use:

```bash
sudo systemctl status openhubble-agent.service
```

The service status should indicate it is `active (running)`.

---

## Updating the Agent

The OpenHubble Agent can be updated using the built-in CLI tool. Run the following command with **root** privileges:

```bash
sudo openhubble-agent update
```

This will:
- Pull the latest updates from the repository.
- Update Python dependencies.
- Restart the service.

---

## Uninstalling the Agent

To uninstall the OpenHubble Agent, use the built-in CLI tool:

```bash
sudo openhubble-agent uninstall
```

This will:
- Stop and disable the service.
- Remove the service file, directories, and configuration files.
