# src/iot/sensor_integration.py

import random
import time
import json

class SensorData:
    """Class to manage and retrieve data from IoT sensors."""

    def __init__(self):
        self.sensors = {
            'temperature': self.simulate_temperature_sensor,
            'humidity': self.simulate_humidity_sensor,
            'co2': self.simulate_co2_sensor
        }
        self.latest_data = {}

    def simulate_temperature_sensor(self):
        """Simulate temperature sensor data."""
        return round(random.uniform(-10.0, 40.0), 2)

    def simulate_humidity_sensor(self):
        """Simulate humidity sensor data."""
        return round(random.uniform(0.0, 100.0), 2)

    def simulate_co2_sensor(self):
        """Simulate CO2 sensor data."""
        return round(random.uniform(300, 1000), 2)

    def read_sensors(self):
        """Read data from all sensors."""
        for sensor_name, sensor_function in self.sensors.items():
            self.latest_data[sensor_name] = sensor_function()
        return self.latest_data

    def get_latest_data(self):
        """Get the latest sensor data."""
        return self.latest_data if self.latest_data else self.read_sensors()

    def start_data_collection(self, interval=5):
        """Start collecting data from sensors at a specified interval."""
        while True:
            self.read_sensors()
            time.sleep(interval)

if __name__ == "__main__":
    sensor_data = SensorData()
    sensor_data.start_data_collection()
