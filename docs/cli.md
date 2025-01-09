# OpenHubble CLI Agent Manager

The `openhubble-agent` is a command-line tool for managing the **OpenHubble agent** service. You can start, stop, restart, check the status of the service, view logs, update, or uninstall it using the CLI.

## Installation

After installing OpenHubble, you can use the `openhubble-agent` command in the terminal.

## Available Commands

### Start the Service

To start the OpenHubble agent service:

```bash
openhubble-agent start
```

This will start the agent service using `systemctl`.

### Stop the Service

To stop the OpenHubble agent service:

```bash
openhubble-agent stop
```

This will stop the agent service.

### Restart the Service

To restart the OpenHubble agent service:

```bash
openhubble-agent restart
```

This will stop and start the agent service again.

### Check the Service Status

To check the status of the OpenHubble agent service:

```bash
openhubble-agent status
```

This will display the current status of the agent service, whether it's running or not.

### View Logs

To view the logs of the OpenHubble agent:

```bash
openhubble-agent logs
```

This will show the last 10 lines of the agent's log. You can also use the `-f` or `--follow` flag to follow the logs in real-time:

```bash
openhubble-agent logs -f
```

### Update the Service

To update the OpenHubble agent:

```bash
openhubble-agent update
```

You will be prompted for confirmation before the update begins. If confirmed, the update script will be executed.

### Uninstall the Service

To uninstall the OpenHubble agent:

```bash
openhubble-agent uninstall
```

You will be prompted for confirmation before the uninstallation begins. If confirmed, the uninstall script will be executed, and the service will be removed.

### Show Version

To check the version of the OpenHubble agent:

```bash
openhubble-agent version
```

This will display the current version of the OpenHubble agent.

### Show Help

To view the help documentation and available commands:

```bash
openhubble-agent help
```

This will show the usage information for the CLI tool, including all available subcommands.

## Example Commands

- **Start the agent:**

  ```bash
  openhubble-agent start
  ```

- **View logs and follow output:**

  ```bash
  openhubble-agent logs -f
  ```

- **Update the agent:**

  ```bash
  openhubble-agent update
  ```

- **Uninstall the agent:**
  ```bash
  openhubble-agent uninstall
  ```

## Troubleshooting

If you encounter any issues, ensure that you have the necessary permissions and the service is installed correctly. You can also check the logs for any error messages using the `logs` command.
