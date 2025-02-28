"""
network_io.py

This script provides information about network I/O (input/output) operations on the host machine.
It uses the `psutil` library to retrieve metrics related to network data transmission and reception.

Functions:
----------
- get_network_io():
    Returns a dictionary containing the following network I/O metrics:
    - bytes_sent (int): Total number of bytes sent over the network.
    - bytes_received (int): Total number of bytes received from the network.
    - packets_sent (int): Total number of packets sent.
    - packets_received (int): Total number of packets received.

Example Output:
---------------
{'bytes_sent': 2675965952, 
 'bytes_received': 3748928512, 
 'packets_sent': 48013411, 
 'packets_received': 52815362}
    
Dependencies:
-------------
- psutil: A Python library for system and process utilities.
  Install it via `pip install psutil`.

"""

import psutil

def get_network_io():
    network_io = psutil.net_io_counters()

    return {
        'bytes_sent': network_io.bytes_sent,
        'bytes_received': network_io.bytes_recv,
        'packets_sent': network_io.packets_sent,
        'packets_received': network_io.packets_recv
    }
