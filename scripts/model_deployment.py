# scripts/model_deployment.py

import joblib
import os
from flask import Flask, request, jsonify
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

app = Flask(__name__)

class ModelDeployment:
    def __init__(self, model_path):
        self.model_path = model_path
        self.model = self.load_model()

    def load_model(self):
        if os.path.exists(self.model_path):
            model = joblib.load(self.model_path)
            logging.info("Model loaded successfully.")
            return model
        else:
            logging.error("Model file not found.")
            raise FileNotFoundError("Model file not found.")

    def predict(self, input_data):
        prediction = self.model.predict([input_data])
        return prediction[0]

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    input_data = data.get('features')
    if input_data is None:
        return jsonify({'error': 'No input data provided'}), 400
    try:
        prediction = model_deployment.predict(input_data)
        return jsonify({'prediction': prediction}), 200
    except Exception as e:
        logging.error(f"Prediction error: {e}")
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    model_deployment = ModelDeployment(model_path='path/to/your/model.pkl')
    app.run(host='0.0.0.0', port=5000)
