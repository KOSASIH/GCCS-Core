# src/ml/model_deployment.py

from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

class ModelDeployer:
    """Class to deploy machine learning models using Flask."""

    def __init__(self, model_path='models'):
        self.model_path = model_path
        self.model = joblib.load(f'{self.model_path}/model.pkl')
        self.scaler = joblib.load(f'{self.model_path}/scaler.pkl')

    def deploy_model(self):
        """Deploy the model using Flask."""
        @app.route('/predict', methods=['POST'])
        def predict():
            data = request.get_json()
            X = np.array(data['features'])
            X_scaled = self.scaler.transform(X)
            predictions = self.model.predict(X_scaled)
            return jsonify({'predictions': predictions.tolist()})

        app.run(debug=True)

if __name__ == "__main__":
    deployer = ModelDeployer()
    deployer.deploy_model()
