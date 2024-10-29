# example_iot_integration.py

import time
import random
import requests
import yaml

# Load configuration
with open('example_config.yaml', 'r') as file:
    config = yaml.safe_load(file)

# API settings
api_host = config['api']['host']
api_port = config['api']['port']
climate_data_endpoint = f"http://{api_host}:{api_port}{config['api']['endpoints']['climate_data']}"

# Simulate IoT device data collection
def collect_sensor_data(device):
    if device['type'] == "temperature":
        return {
            "id": device['id'],
            "type": device['type'],
            "value": round(random.uniform(-30.0, 50.0), 2),  # Random temperature
            "location": device['location']
        }
    elif device['type'] == "humidity":
        return {
            "id": device['id'],
            "type": device['type'],
            "value": round(random.uniform(0, 100), 2),  # Random humidity
            "location": device['location']
        }

# Send data to the API
def send_data_to_api(data):
    response = requests.post(climate_data_endpoint, json=data)
    if response.status_code == 200:
        print("Data sent successfully:", data)
    else:
        print("Failed to send data:", response.status_code)

if __name__ == "__main__":
    for device in config['iot']['devices']:
        while True:
            sensor_data = collect_sensor_data(device)
            send_data_to_api(sensor_data)
            time.sleep(device['sampling_rate'])  # Wait for the next sampling
