# Date and time stuff
from datetime import datetime
import time

# Database
from database.influx import get_write_api, check, DB
from influxdb_client import Point

# Utils
from utils.cpu import get_cpu_usage
from utils.memory import get_memory_usage
from utils.swap import get_swap_usage
from utils.disk_io import get_disk_io
from utils.network_io import get_network_io
from utils.system_load import get_system_load

# Other libs
import logging

logging.basicConfig(level=logging.INFO)

def main():
    # Check database connection
    if not check():
        logging.error("Error in connecting to database")
        return

    write_api = get_write_api()
    try:
        while True:
            # Get data from utils
            cpu_data = get_cpu_usage()
            memory_data = get_memory_usage()
            swap_data = get_swap_usage()
            disk_io_data = get_disk_io()
            network_io_data = get_network_io()
            system_load_data = get_system_load()
            
            # Creating Points
            cpu_point = (
                Point("cpu_analyze")
                .field("total_usage", cpu_data['total_usage'])
                .time(datetime.utcnow())
            )
            memory_point = (
                Point("memory_analyze")
                .field("total_memory", memory_data['total'])
                .field("available_memory", memory_data['available'])
                .field("used_memory", memory_data['used'])
                .field("memory_percent", memory_data['percent'])
                .time(datetime.utcnow())
            )
            swap_point = (
                Point("swap_analyze")
                .field("total_swap", swap_data['total'])
                .field("used_swap", swap_data['used'])
                .field("free_swap", swap_data['free'])
                .field("swap_percent", swap_data['percent'])
                .time(datetime.utcnow())
            )
            disk_io_point = (
                Point("disk_io_analyze")
                .field("read_bytes", disk_io_data['read_bytes'])
                .field("write_bytes", disk_io_data['write_bytes'])
                .field("read_count", disk_io_data['read_count'])
                .field("write_count", disk_io_data['write_count'])
                .time(datetime.utcnow())
            )
            network_io_point = (
                Point("network_io_analyze")
                .field("bytes_sent", network_io_data['bytes_sent'])
                .field("bytes_received", network_io_data['bytes_received'])
                .field("packets_sent", network_io_data['packets_sent'])
                .field("packets_received", network_io_data['packets_received'])
                .time(datetime.utcnow())
            )
            system_load_point = (
                Point("system_load_analyze")
                .field("1_min", system_load_data['1_min'])
                .field("5_min", system_load_data['5_min'])
                .field("15_min", system_load_data['15_min'])
                .time(datetime.utcnow())
            )

            # Writing Points
            write_api.write(bucket=DB['bucket'], org=DB['org'], record=cpu_point)
            write_api.write(bucket=DB['bucket'], org=DB['org'], record=memory_point)
            write_api.write(bucket=DB['bucket'], org=DB['org'], record=swap_point)
            write_api.write(bucket=DB['bucket'], org=DB['org'], record=disk_io_point)
            write_api.write(bucket=DB['bucket'], org=DB['org'], record=network_io_point)
            write_api.write(bucket=DB['bucket'], org=DB['org'], record=system_load_point)

            # Logging
            logging.info(f"CPU Data Written: {cpu_data}")
            logging.info(f"Memory Data Written: {memory_data}")
            logging.info(f"Swap Data Written: {swap_data}")
            logging.info(f"Disk I/O Data Written: {disk_io_data}")
            logging.info(f"Network I/O Data Written: {network_io_data}")
            logging.info(f"System Load Data Written: {system_load_data}")

            time.sleep(1)
    except Exception as e:
        logging.error("Error during data collection or write operation", exc_info=True)
    finally:
        write_api.close()
        logging.info("InfluxDB client closed.")

if __name__ == "__main__":
    main()
