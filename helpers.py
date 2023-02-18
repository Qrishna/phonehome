import requests
import psutil
import platform
import socket
import uuid
import time
from datetime import datetime, timezone
import os
import json
import subprocess

cert = ('certificates/full_chain.pem', 'certificates/private_key.pem')


def get_utc_timestamp():
    return datetime.now(timezone.utc).isoformat()


def log(message):
    print("%s - %s" % (str(get_utc_timestamp()), message))


def get_info_registration():
    return {
        "hostname": platform.node(),
        "macaddress": ':'.join(
            ['{:02x}'.format((uuid.getnode() >> ele) & 0xff) for ele in range(0, 8 * 6, 8)][::-1]),
        "public_ip": get_public_ip_address(),
        "ip": ':'.join(psutil.net_if_addrs()['en0'][0].address.split(':')).lower(),
        "platform": platform.system().lower(),
        "network": get_network_info(),
        "info": {
            "geo_location": get_geolocation_info(get_public_ip_address()),
            "release": platform.release(),
            "total_memory": psutil.virtual_memory().total,
            "cpu_info": get_cpu_info(),
            "version": platform.version(),
            "uptime": int(time.time() - psutil.boot_time()),
        }
    }


def get_cpu_info():
    cpu_freq = str(psutil.cpu_freq().current/1000.0) + " GHz"
    num_cores = psutil.cpu_count(logical=False)
    num_threads = psutil.cpu_count(logical=True)
    return {"frequency":  cpu_freq, "cores": num_cores, "threads": num_threads}


def get_network_info():
    interfaces = psutil.net_if_addrs()
    result = {'interfaces': {}}
    for interface_name, interface_addresses in interfaces.items():
        result['interfaces'][interface_name] = []
        for address in interface_addresses:
            if address.family == socket.AF_INET:
                result['interfaces'][interface_name].append({
                    'address': address.address,
                    'netmask': address.netmask,
                    'broadcast': address.broadcast
                })
            elif address.family == socket.AF_INET6:
                result['interfaces'][interface_name].append({
                    'address': address.address,
                    'netmask': address.netmask,
                    'broadcast': None
                })
    return result


def get_geolocation_info(ip_address):
    url = f"http://ip-api.com/json/{ip_address}"
    response = requests.get(url)
    if response.ok:
        response_json = response.json()
        return {
            "city": response_json["city"],
            "region": response_json["regionName"],
            "country": response_json["country"],
            "latitude": response_json["lat"],
            "longitude": response_json["lon"],
        }


def get_public_ip_address():
    response = requests.get('https://api.ipify.org')
    if response.ok:
        return response.text


def get_info_for_phone_home(thing_id, token):
    return {
        "thing_id": thing_id,
        "token": token,
        "message": {
            "ip_address": ':'.join(psutil.net_if_addrs()['en0'][0].address.split(':')).lower(),
            "public_ip": get_public_ip_address(),
            "geo_location": get_geolocation_info(get_public_ip_address()),
            "release": platform.release(),
            "free_memory": psutil.virtual_memory().available,
            "version": platform.version(),
            "uptime": int(time.time() - psutil.boot_time()),
            "load_average": os.getloadavg(),
            "disk_space": {"free": psutil.disk_usage('/').free},
            "policy_execution_results": None
        }
    }


def registration():
    url = "http://localhost:8000/things"
    headers = {'Content-Type': 'application/json'}
    message = get_info_registration()
    try:
        response = requests.post(url, data=json.dumps(message), headers=headers, cert=cert, verify='certificates/ca.pem')
        response.raise_for_status()
        response_data = json.loads(response.text)
        log("registration():: Registration was successful. The response received was: \n%s" % json.dumps(json.loads(response.text), indent=4))

        if response.ok:
            return True, response_data["id"]
    except requests.exceptions.RequestException as e:
        log("registration():: Registration failed: %s" % str(e))
    return False, None


def apply_policies(configs):
    my_config = configs["config"]
    my_policies = my_config["machine_policies"]
    policy_results = None
    if "script" in my_policies:
        # script_type = my_config.get("script_type", "bash")
        script_text = my_config.get("script_text", "")
        try:
            result = subprocess.run(script_text, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            policy_results = {"stdout":  result.stdout, "stderr": result.stderr}
        except subprocess.CalledProcessError as e:
            print("Error executing script: ", e)
    else:
        print("No script policy found.")
    return policy_results


def phone_home(url, headers, message, cert):
    log("phone_home():: Phoning home with this message: \n%s" % json.dumps(message, indent=4))
    try:
        response = requests.post(url, data=json.dumps(message), headers=headers, cert=cert, verify='certificates/ca.pem')
        response.raise_for_status()
        log("phone_home():: Phone home successful. The response received was: \n%s" % json.dumps(json.loads(response.text), indent=4))
        return True, json.loads(response.text)
    except requests.exceptions.RequestException as e:
        log("phone_home():: Phone home failed: %s" % str(e))
    return False, None
