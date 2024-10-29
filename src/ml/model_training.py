# src/ml/model_training.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
import joblib
import os

class ModelTrainer:
    """Class to train machine learning models."""

    def __init__(self, model_path='models', test_size=0.2, random_state=42):
        self.model_path = model_path
        self.test_size = test_size
        self.random_state = random_state
        self.model = RandomForestRegressor()

    def load_data(self, file_path):
        """Load dataset from a CSV file."""
        data = pd.read_csv(file_path)
        return data

    def preprocess_data(self, data):
        """Preprocess the data for training."""
        X = data.drop('target', axis=1)  # Assuming 'target' is the label column
        y = data['target']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=self.test_size, random_state=self.random_state)
        scaler = StandardScaler()
        X_train = scaler.fit_transform(X_train)
        X_test = scaler.transform(X_test)
        return X_train, X_test, y_train, y_test, scaler

    def train_model(self, X_train, y_train):
        """Train the model."""
        self.model.fit(X_train, y_train)

    def save_model(self, model_name='model.pkl', scaler_name='scaler.pkl'):
        """Save the trained model and scaler to disk."""
        os.makedirs(self.model_path, exist_ok=True)
        joblib.dump(self.model, os.path.join(self.model_path, model_name))
        joblib.dump(self.scaler, os.path.join(self.model_path, scaler_name))

    def run(self, data_file):
        """Load data, preprocess, train, and save the model."""
        data = self.load_data(data_file)
        X_train, X_test, y_train, y_test, self.scaler = self.preprocess_data(data)
        self.train_model(X_train, y_train)
        self.save_model()

if __name__ == "__main__":
    trainer = ModelTrainer()
    trainer.run('data/training_data.csv')  # Path to your training data
