# src/utils/configuration.py

import json
import os

class ConfigManager:
    """Class to manage application configuration."""

    def __init__(self, config_file='config.json'):
        self.config_file = config_file
        self.config = self.load_config()

    def load_config(self):
        """Load configuration from a JSON file."""
        if not os.path.exists(self.config_file):
            raise FileNotFoundError(f"Configuration file {self.config_file} not found.")
        
        with open(self.config_file, 'r') as file:
            return json.load(file)

    def get(self, key, default=None):
        """Get a configuration value by key."""
        return self.config.get(key, default)

if __name__ == "__main__":
    config_manager = ConfigManager()
    print(config_manager.get('api_url', 'Not Found'))
