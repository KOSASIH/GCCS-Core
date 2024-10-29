# climate_monitor.py

import random
import time
import json
import logging
import sqlite3
import matplotlib.pyplot as plt
from datetime import datetime

class ClimateMonitor:
    def __init__(self, db_path='climate_data.db'):
        self.data = []
        self.db_path = db_path
        self.create_database()

    def create_database(self):
        """Create a SQLite database to store climate data."""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS climate_data (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    timestamp TEXT NOT NULL,
                    temperature REAL NOT NULL,
                    humidity REAL NOT NULL,
                    co2_level REAL NOT NULL
                )
            ''')
            conn.commit()
            conn.close()
            logging.info("Database created successfully.")
        except Exception as e:
            logging.error(f"Error creating database: {e}")

    def validate_data(self, temperature, humidity, co2_level):
        """Validate the collected climate data."""
        if not (-30 <= temperature <= 50):
            logging.warning(f"Invalid temperature: {temperature}")
            return False
        if not (0 <= humidity <= 100):
            logging.warning(f"Invalid humidity: {humidity}")
            return False
        if not (300 <= co2_level <= 600):
            logging.warning(f"Invalid CO2 level: {co2_level}")
            return False
        return True

    def collect_data(self):
        """Simulate data collection from IoT sensors."""
        temperature = round(random.uniform(-30, 50), 2)  # Simulated temperature in Celsius
        humidity = round(random.uniform(0, 100), 2)      # Simulated humidity in percentage
        co2_level = round(random.uniform(300, 600), 2)   # Simulated CO2 level in ppm

        if self.validate_data(temperature, humidity, co2_level):
            climate_data = {
                "timestamp": datetime.now().isoformat(),
                "temperature": temperature,
                "humidity": humidity,
                "co2_level": co2_level
            }
            self.data.append(climate_data)
            self.store_data(climate_data)
            logging.info(f"Collected Data: {json.dumps(climate_data)}")
        else:
            logging.error("Data collection failed due to validation errors.")

    def store_data(self, climate_data):
        """Store collected climate data in the database."""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO climate_data (timestamp, temperature, humidity, co2_level)
                VALUES (?, ?, ?, ?)
            ''', (climate_data['timestamp'], climate_data['temperature'], climate_data['humidity'], climate_data['co2_level']))
            conn.commit()
            conn.close()
            logging.info("Data stored in database successfully.")
        except Exception as e:
            logging.error(f"Error storing data in database: {e}")

    def visualize_data(self):
        """Visualize the collected climate data."""
        if not self.data:
            logging.warning("No data available for visualization.")
            return

        timestamps = [entry['timestamp'] for entry in self.data]
        temperatures = [entry['temperature'] for entry in self.data]
        humidities = [entry['humidity'] for entry in self.data]
        co2_levels = [entry['co2_level'] for entry in self.data]

        plt.figure(figsize=(12, 6))

        plt.subplot(3, 1, 1)
        plt.plot(timestamps, temperatures, label='Temperature (°C)', color='red')
        plt.title('Temperature Over Time')
        plt.xlabel('Timestamp')
        plt.ylabel('Temperature (°C)')
        plt.xticks(rotation=45)
        plt.grid()

        plt.subplot(3, 1, 2)
        plt.plot(timestamps, humidities, label='Humidity (%)', color='blue')
        plt.title('Humidity Over Time')
        plt.xlabel('Timestamp')
        plt.ylabel('Humidity (%)')
        plt.xticks(rotation=45)
        plt.grid()

        plt.subplot(3, 1, 3)
        plt.plot(timestamps, co2_levels, label='CO2 Level (ppm)', color='green')
        plt.title('CO2 Level Over Time')
        plt.xlabel('Timestamp')
        plt.ylabel('CO2 Level (ppm)')
        plt.xticks(rotation=45)
        plt.grid()

        plt.tight_layout()
        plt.show()

    def start_monitoring(self, interval=5):
        """Start monitoring climate data at a specified interval."""
        while True:
            self.collect_data()
            time.sleep(interval)

if __name__ == "__main__":
    climate_monitor = ClimateMonitor()
    climate_monitor.start_monitoring()
