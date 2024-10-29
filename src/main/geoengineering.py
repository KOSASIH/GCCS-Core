# geoengineering.py

import numpy as np
import pandas as pd
import logging
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error

class Geoengineering:
    def __init__(self):
        self.techniques = {
            'solar_radiation_management': self.solar_radiation_management,
            'carbon_capture': self.carbon_capture
        }
        self.results = []

    def solar_radiation_management(self, initial_temperature, reduction_factor):
        """Simulate the effects of solar radiation management."""
        # Simulate temperature reduction
        new_temperature = initial_temperature * (1 - reduction_factor)
        logging.info(f"Solar Radiation Management applied: Initial Temp: {initial_temperature}, New Temp: {new_temperature}")
        return new_temperature

    def carbon_capture(self, initial_co2, capture_efficiency):
        """Simulate the effects of carbon capture."""
        # Simulate CO2 reduction
        new_co2 = initial_co2 * (1 - capture_efficiency)
        logging.info(f"Carbon Capture applied: Initial CO2: {initial_co2}, New CO2: {new_co2}")
        return new_co2

    def apply_technique(self, technique_name, initial_conditions):
        """Apply the specified geoengineering technique."""
        if technique_name not in self.techniques:
            logging.error(f"Technique {technique_name} not recognized.")
            return None

        if technique_name == 'solar_radiation_management':
            new_temperature = self.techniques[technique_name](initial_conditions['temperature'], initial_conditions['reduction_factor'])
            self.results.append({'temperature': new_temperature, 'co2_level': initial_conditions['co2_level']})
            return new_temperature

        elif technique_name == 'carbon_capture':
            new_co2 = self.techniques[technique_name](initial_conditions['co2_level'], initial_conditions['capture_efficiency'])
            self.results.append({'temperature': initial_conditions['temperature'], 'co2_level': new_co2})
            return new_co2

    def analyze_results(self):
        """Analyze the results of the geoengineering techniques."""
        df = pd.DataFrame(self.results)
        if df.empty:
            logging.warning("No results to analyze.")
            return

        # Calculate mean and standard deviation
        mean_temp = df['temperature'].mean()
        mean_co2 = df['co2_level'].mean()
        logging.info(f"Mean Temperature after techniques: {mean_temp}")
        logging.info(f"Mean CO2 Level after techniques: {mean_co2}")

        # Visualize results
        self.visualize_results(df)

    def visualize_results(self, df):
        """Visualize the results of the geoengineering techniques."""
        plt.figure(figsize=(12, 6))

        plt.subplot(2, 1, 1)
        plt.plot(df.index, df['temperature'], label='Temperature', color='red')
        plt.title('Temperature Over Time After Geoengineering')
        plt.xlabel('Time Steps')
        plt.ylabel('Temperature (°C)')
        plt.grid()

        plt.subplot(2, 1, 2)
        plt.plot(df.index, df['co2_level'], label='CO2 Level', color='green')
        plt.title('CO2 Level Over Time After Geoengineering')
        plt.xlabel('Time Steps')
        plt.ylabel('CO2 Level (ppm)')
        plt.grid()

        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    
    geoengineering = Geoengineering()
    
    # Simulate initial conditions
    initial_conditions = {
        'temperature': 25.0,  # Initial temperature in °C
        'co2_level': 400.0,   # Initial CO2 level in ppm
        'reduction_factor': 0.1,  # 10% reduction in temperature
        'capture_efficiency': 0.2  # 20% CO2 capture efficiency
    }

    # Apply geoengineering techniques
    geoengineering.apply_technique('solar_radiation_management', initial_conditions)
    geoengineering.apply_technique('carbon_capture', initial_conditions)

    # Analyze and visualize results
    geoengineering.analyze_results()
