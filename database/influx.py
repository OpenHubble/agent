import influxdb_client
from influxdb_client.client.write_api import SYNCHRONOUS

import config.config as config

mode = ''

if config.PRODUCTION:
    mode = 'influx_prod'
else:
    mode = 'influx_local'
    
DB = config.DB[mode]

influx_url = DB['url']
influx_token = DB['token']
influx_org = DB['org']
influx_bucket = DB['bucket']

client = influxdb_client.InfluxDBClient(url=influx_url, token=influx_token, org=influx_org)

def check():
    ping = client.ping()
    
    return ping

def get_write_api():
    return client.write_api(write_options=SYNCHRONOUS)

def get_query_api():
    return client.query_api()

def close_client():
    client.close()
