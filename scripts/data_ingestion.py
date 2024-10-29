# scripts/data_ingestion.py

import requests
import pandas as pd
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class DataIngestion:
    def __init__(self, source_type, source_details):
        self.source_type = source_type
        self.source_details = source_details

    def ingest_data(self):
        if self.source_type == 'api':
            return self._ingest_from_api()
        elif self.source_type == 'csv':
            return self._ingest_from_csv()
        elif self.source_type == 'iot':
            return self._ingest_from_iot()
        else:
            logging.error("Unsupported data source type.")
            raise ValueError("Unsupported data source type.")

    def _ingest_from_api(self):
        try:
            response = requests.get(self.source_details['url'])
            response.raise_for_status()
            data = response.json()
            logging.info("Data ingested from API successfully.")
            return pd.DataFrame(data)
        except Exception as e:
            logging.error(f"Error ingesting data from API: {e}")
            raise

    def _ingest_from_csv(self):
        try:
            data = pd.read_csv(self.source_details['file_path'])
            logging.info("Data ingested from CSV successfully.")
            return data
        except Exception as e:
            logging.error(f"Error ingesting data from CSV: {e}")
            raise

    def _ingest_from_iot(self):
        # Placeholder for IoT data ingestion logic
        logging.info("Ingesting data from IoT devices...")
        # Implement IoT data collection logic here
        return pd.DataFrame()  # Return an empty DataFrame for now

if __name__ == "__main__":
    # Example usage
    source = {
        'type': 'api',
        'details': {'url': 'https://api.example.com/climate_data'}
    }
    ingestion = DataIngestion(source['type'], source['details'])
    data = ingestion.ingest_data()
    print(data.head())
