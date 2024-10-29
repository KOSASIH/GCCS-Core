# api/rest_api.py

from flask import Flask, jsonify, request
from flask_cors import CORS
from src.core.climate_models import ClimateModel
from src.iot.sensor_integration import SensorData

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Initialize climate model and sensor data
climate_model = ClimateModel()
sensor_data = SensorData()

@app.route('/api/v1/climate-data', methods=['GET'])
def get_climate_data():
    """Retrieve the latest climate data from IoT sensors."""
    data = sensor_data.get_latest_data()
    return jsonify(data), 200

@app.route('/api/v1/predict', methods=['POST'])
def predict_climate_outcome():
    """Predict climate outcomes based on input parameters."""
    input_data = request.json
    prediction = climate_model.predict(input_data)
    return jsonify(prediction), 200

@app.route('/api/v1/geoengineering', methods=['POST'])
def initiate_geoengineering():
    """Initiate a geoengineering intervention."""
    intervention_data = request.json
    result = climate_model.initiate_geoengineering(intervention_data)
    return jsonify(result), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
