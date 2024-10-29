# src/ml/model_evaluation.py

import joblib
import pandas as pd
from sklearn.metrics import mean_squared_error, r2_score

class ModelEvaluator:
    """Class to evaluate machine learning models."""

    def __init__(self, model_path='models'):
        self.model_path = model_path
        self.model = joblib.load(f'{self.model_path}/model.pkl')
        self.scaler = joblib.load(f'{self.model_path}/scaler.pkl')

    def load_data(self, file_path):
        """Load dataset from a CSV file."""
        data = pd.read_csv(file_path)
        return data

    def preprocess_data(self, data):
        """Preprocess the data for evaluation."""
        X = data.drop('target', axis=1)  # Assuming 'target' is the label column
        y = data['target']
        X_scaled = self.scaler.transform(X)
        return X_scaled, y

    def evaluate_model(self, X_test, y_test):
        """Evaluate the model and return metrics."""
        predictions = self.model.predict(X_test)
        mse = mean_squared_error(y_test, predictions)
        r2 = r2_score(y_test, predictions)
        return mse, r2

    def run(self, data_file):
        """Load data, preprocess, and evaluate the model."""
        data = self.load_data(data_file)
        X_test, y_test = self.preprocess_data(data)
        mse, r2 = self .evaluate_model(X_test, y_test)
        print(f'Mean Squared Error: {mse:.2f}')
        print(f'R2 Score: {r2:.2f}')

if __name__ == "__main__":
    evaluator = ModelEvaluator()
    evaluator.run('data/testing_data.csv')  # Path to your testing data
