# example_usage.py

import requests
import yaml

# Load configuration
with open('example_config.yaml', 'r') as file:
    config = yaml.safe_load(file)

# API settings
api_host = config['api']['host']
api_port = config['api']['port']
climate_data_endpoint = f"http://{api_host}:{api_port}{config['api']['endpoints']['climate_data']}"
predictive_model_endpoint = f"http://{api_host}:{api_port}{config['api']['endpoints']['predictive_model']}"

# Fetch climate data
def fetch_climate_data():
    response = requests.get(climate_data_endpoint)
    if response.status_code == 200:
        data = response.json()
        print("Climate Data:", data)
    else:
        print("Failed to fetch climate data:", response.status_code)

# Make a prediction
def make_prediction(input_data):
    response = requests.post(predictive_model_endpoint, json=input_data)
    if response.status_code == 200:
        prediction = response.json()
        print("Prediction:", prediction)
    else:
        print("Failed to make prediction:", response.status_code)

if __name__ == "__main__":
    fetch_climate_data()
    
    # Example input data for prediction
    input_data = {
        "temperature": 22.5,
        "humidity": 60,
        "co2_levels": 400
    }
    
    make_prediction(input_data)
