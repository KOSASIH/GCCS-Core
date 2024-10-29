# predictive_model.py

import numpy as np
import pandas as pd
import json
import logging
import joblib
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

class PredictiveModel:
    def __init__(self):
        self.models = {
            'linear_regression': LinearRegression(),
            'random_forest': RandomForestRegressor()
        }
        self.trained_models = {}
        self.data = []

    def add_data(self, climate_data):
        """Add new climate data for training."""
        self.data.append(climate_data)

    def prepare_data(self):
        """Prepare features and targets for training."""
        df = pd.DataFrame(self.data)
        features = df[['temperature', 'humidity', 'co2_level']]
        targets = df['temperature']  # Predicting temperature as an example
        return train_test_split(features, targets, test_size=0.2, random_state=42)

    def train_model(self, model_name):
        """Train the specified predictive model."""
        X_train, X_test, y_train, y_test = self.prepare_data()
        model = self.models[model_name]
        
        # Hyperparameter tuning using GridSearchCV for Random Forest
        if model_name == 'random_forest':
            param_grid = {
                'n_estimators': [50, 100, 200],
                'max_depth': [None, 10, 20, 30],
                'min_samples_split': [2, 5, 10]
            }
            grid_search = GridSearchCV(model, param_grid, cv=5, scoring='neg_mean_squared_error')
            grid_search.fit(X_train, y_train)
            model = grid_search.best_estimator_
            logging.info(f"Best parameters for {model_name}: {grid_search.best_params_}")

        model.fit(X_train, y_train)
        self.trained_models[model_name] = model
        logging.info(f"{model_name} trained successfully.")

        # Evaluate the model
        self.evaluate_model(model, X_test, y_test)

    def evaluate_model(self, model, X_test, y_test):
        """Evaluate the trained model and log performance metrics."""
        predictions = model.predict(X_test)
        mse = mean_squared_error(y_test, predictions)
        r2 = r2_score(y_test, predictions)
        logging.info(f"Model Evaluation - MSE: {mse}, R²: {r2}")

        # Visualize predictions vs actual values
        plt.figure(figsize=(10, 5))
        plt.scatter(y_test, predictions, color='blue')
        plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2)
        plt.title(f'{model.__class__.__name__} Predictions vs Actual')
        plt.xlabel('Actual Values')
        plt.ylabel('Predicted Values')
        plt.grid()
        plt.show()

    def save_model(self, model_name):
        """Save the trained model to a file."""
        if model_name in self.trained_models:
            joblib.dump(self.trained_models[model_name], f"{model_name}.joblib")
            logging.info(f"{model_name} model saved successfully.")
        else:
            logging.warning(f"No trained model found for {model_name}.")

    def load_model(self, model_name):
        """Load a trained model from a file."""
        try:
            model = joblib.load(f"{model_name}.joblib")
            self.trained_models[model_name] = model
            logging.info(f"{model_name} model loaded successfully.")
        except FileNotFoundError:
            logging.error(f"{model_name} model file not found.")

if __name__ == "__main__":
    model = PredictiveModel()
    # Simulate adding historical data
    for _ in range(100):
        model.add_data({
            "temperature": np.random.uniform(15, 30),
            "humidity": np.random.uniform(40, 80),
            "co2_level": np.random.uniform(350, 450)
        })
    
    # Train and evaluate models
    for model_name in model.models.keys():
        model.train_model(model_name)
        model.save_model(model_name)
