# api/websocket_api.py

from flask import Flask
from flask_socketio import SocketIO, emit
from src.iot.sensor_integration import SensorData

app = Flask(__name__)
socketio = SocketIO(app)

# Initialize sensor data
sensor_data = SensorData()

@socketio.on('connect')
def handle_connect():
    """Handle new WebSocket connections."""
    print('Client connected')
    emit('response', {'message': 'Connected to WebSocket API'})

@socketio.on('request_latest_data')
def handle_request_latest_data():
    """Send the latest climate data to the client."""
    data = sensor_data.get_latest_data()
    emit('latest_data', data)

@socketio.on('disconnect')
def handle_disconnect():
    """Handle WebSocket disconnections."""
    print('Client disconnected')

if __name__ == '__main__':
    socketio.run(app, debug=True, host='0.0.0.0', port=5001)
