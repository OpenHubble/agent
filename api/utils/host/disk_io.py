"""
disk_io.py

This script provides information about disk I/O (input/output) operations on the host machine.
It uses the `psutil` library to retrieve metrics related to disk reads and writes.

Functions:
----------
- get_disk_io(): 
    Returns a dictionary containing the following disk I/O metrics:
    - read_bytes (int): Total number of bytes read from disk.
    - write_bytes (int): Total number of bytes written to disk.
    - read_count (int): Total number of read operations performed.
    - write_count (int): Total number of write operations performed.

Example Output:
---------------
{'read_bytes': 3257248359424, 
 'write_bytes': 927094636544, 
 'read_count': 132314319, 
 'write_count': 33162176}
    
Dependencies:
-------------
- psutil: A Python library for system and process utilities. 
  Install it via `pip install psutil`.

"""

import psutil

def get_disk_io():
    disk_io = psutil.disk_io_counters()

    io_data = {
        'read_bytes': disk_io.read_bytes,
        'write_bytes': disk_io.write_bytes,
        'read_count': disk_io.read_count,
        'write_count': disk_io.write_count
    }

    return io_data
