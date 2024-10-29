# src/iot/data_acquisition.py

import requests
import json
from datetime import datetime

class DataAcquisition:
    """Class to acquire data from external sources."""

    def __init__(self, api_url):
        self.api_url = api_url

    def fetch_external_data(self):
        """Fetch data from an external API."""
        try:
            response = requests.get(self.api_url)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching external data: {e}")
            return None

    def combine_data(self, sensor_data, external_data):
        """Combine sensor data with external data."""
        combined_data = {
            'timestamp': datetime.utcnow().isoformat(),
            'sensor_data': sensor_data,
            'external_data': external_data
        }
        return combined_data

if __name__ == "__main__":
    # Example usage
    api_url = "https://api.example.com/climate-data"
    data_acquisition = DataAcquisition(api_url)
    external_data = data_acquisition.fetch_external_data()
    print(external_data)
