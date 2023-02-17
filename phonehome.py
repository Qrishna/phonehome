

import os
import json
import requests
import psutil
import platform
import time
from datetime import datetime, timezone

debug = True


def get_utc_timestamp():
    return datetime.now(timezone.utc).isoformat()


def log(message):
    print("%s - %s" % (str(get_utc_timestamp()), message))


def phone_home(thing_id, token, url, headers, cert=None):
    # Get system information for the message message
    hostname = platform.node()
    mac_address = ':'.join(psutil.net_if_addrs()['en0'][0].address.split(':')).lower()
    release = platform.release()
    platform_name = platform.system().lower()
    total_memory = psutil.virtual_memory().total
    free_memory = psutil.virtual_memory().available
    version = platform.version()
    uptime = int(time.time() - psutil.boot_time())
    load_average = os.getloadavg()
    disk_space = psutil.disk_usage('/').free

    # Create the message message
    message = {
        "thing_id": thing_id,
        "token": token,
        "message": {
            "hostname": hostname,
            "mac_address": mac_address,
            "release": release,
            "platform": platform_name,
            "total_memory": total_memory,
            "free_memory": free_memory,
            "version": version,
            "uptime": uptime,
            "load_average": load_average,
            "disk_space": {"free": disk_space}
        }
    }

    # Send the POST request and handle errors
    try:
        response = requests.post(url, data=json.dumps(message), headers=headers, cert=cert, verify='certificates/ca.pem')
        response.raise_for_status()
        if debug:
            log("Phoned home with this message: \n%s" % json.dumps(message, indent=4))
        log("Phone home successful. The response received was: %s" % response.text)
    except requests.exceptions.RequestException as e:
        log("Phone home failed: %s" % str(e))


# MAIN
def main():
    interval = 30  # 30 seconds
    thing_id = 2
    # token = "1b87af3292ac69091ac89595716ffa3a026419bee4a6aa0f69ec8de6a1f968c9"
    token = "YfmSl6Cb_6yT5JHH0achxcQDvoRnHBN7XQ8hCBNBA9A"
    # Override with environment variables if they exist
    if 'THING_ID' in os.environ:
        thing_id = os.environ['THING_ID']
    if 'TOKEN' in os.environ:
        token = os.environ['TOKEN']

    # Set the URL and headers for the request
    # url = "http://localhost:8000/phonehome/"
    url = "https://manjusapkota.com/phonehome/"
    headers = {'Content-Type': 'application/json'}

    cert = ('certificates/full_chain.pem', 'certificates/private_key.pem')
    # Run the phone home function at the specified interval
    while True:
        log("Starting Phone Home...")
        phone_home(thing_id, token, url, headers, cert)

        time.sleep(interval)


if __name__ == "__main__":
    main()


