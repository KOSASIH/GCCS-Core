# data_processing.py

import pandas as pd
import numpy as np
import logging
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer

class DataProcessor:
    def __init__(self, data):
        self.data = data
        self.processed_data = None

    def clean_data(self):
        """Clean the dataset by removing duplicates and handling missing values."""
        initial_shape = self.data.shape
        self.data.drop_duplicates(inplace=True)
        logging.info(f"Removed duplicates: {initial_shape[0]} -> {self.data.shape[0]}")

        # Handle missing values
        imputer = SimpleImputer(strategy='mean')
        numeric_cols = self.data.select_dtypes(include=[np.number]).columns.tolist()
        self.data[numeric_cols] = imputer.fit_transform(self.data[numeric_cols])
        logging.info("Missing values imputed for numeric columns.")

    def normalize_data(self):
        """Normalize the numeric features in the dataset."""
        scaler = StandardScaler()
        numeric_cols = self.data.select_dtypes(include=[np.number]).columns.tolist()
        self.data[numeric_cols] = scaler.fit_transform(self.data[numeric_cols])
        logging.info("Numeric features normalized.")

    def feature_engineering(self):
        """Create new features based on existing data."""
        # Example: Create a temperature anomaly feature
        if 'temperature' in self.data.columns:
            self.data['temperature_anomaly'] = self.data['temperature'] - self.data['temperature'].mean()
            logging.info("Temperature anomaly feature created.")

    def encode_categorical_features(self):
        """Encode categorical features using OneHotEncoder."""
        categorical_cols = self.data.select_dtypes(include=['object']).columns.tolist()
        if categorical_cols:
            encoder = OneHotEncoder(sparse=False, drop='first')
            encoded_features = encoder.fit_transform(self.data[categorical_cols])
            encoded_df = pd.DataFrame(encoded_features, columns=encoder.get_feature_names_out(categorical_cols))
            self.data = pd.concat([self.data.reset_index(drop=True), encoded_df.reset_index(drop=True)], axis=1)
            self.data.drop(categorical_cols, axis=1, inplace=True)
            logging.info("Categorical features encoded.")

    def visualize_data_distribution(self):
        """Visualize the distribution of numeric features."""
        numeric_cols = self.data.select_dtypes(include=[np.number]).columns.tolist()
        for col in numeric_cols:
            plt.figure(figsize=(10, 5))
            sns.histplot(self.data[col], bins=30, kde=True)
            plt.title(f'Distribution of {col}')
            plt.xlabel(col)
            plt.ylabel('Frequency')
            plt.grid()
            plt.show()

    def process_data(self):
        """Run the complete data processing pipeline."""
        self.clean_data()
        self.normalize_data()
        self.feature_engineering()
        self.encode_categorical_features()
        self.visualize_data_distribution()
        self.processed_data = self.data
        logging.info("Data processing complete.")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    # Simulate loading data
    data = pd.DataFrame({
        'temperature': [22.5, 23.0, np.nan, 24.5, 25.0, 22.0, 23.5, 22.5, 24.0, 25.5],
        'humidity': [55, 60, 65, np.nan, 70, 75, 80, 85, 90, 95],
        'co2_level': [400, 410, 420, 430, 440, 450, 460, 470, 480, 490],
        'region': ['North', 'South', 'East', 'West', 'North', 'South', 'East', 'West', 'North', 'South']
    })

    processor = DataProcessor(data)
    processor.process_data()
