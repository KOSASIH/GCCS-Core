# src/tests/test_iot.py

import pytest
from src.main.iot import IoTDeviceManager

def test_register_iot_device():
    device_manager = IoTDeviceManager()
    response = device_manager.register_device('sensor_1', 'temperature')
    assert response['status'] == 'success'
    assert 'device_id' in response

def test_get_device_data():
    device_manager = IoTDeviceManager()
    device_manager.register_device('sensor_1', 'temperature')
    data = device_manager.get_device_data('sensor_1')
    assert data is not None
    assert 'temperature' in data

def test_get_nonexistent_device_data():
    device_manager = IoTDeviceManager()
    data = device_manager.get_device_data('nonexistent_sensor')
    assert data is None
