# src/tests/test_ml.py

import pytest
from src.main.ml_model import MLModel

def test_train_model():
    model = MLModel()
    training_data = [
        {'features': [1, 2, 3], 'label': 0},
        {'features': [4, 5, 6], 'label': 1}
    ]
    response = model.train(training_data)
    assert response['status'] == 'success'
    assert model.is_trained() is True

def test_predict_with_trained_model():
    model = MLModel()
    training_data = [
        {'features': [1, 2, 3], 'label': 0},
        {'features': [4, 5, 6], 'label': 1}
    ]
    model.train(training_data)
    prediction = model.predict([2, 3, 4])
    assert prediction in [0, 1]  # Assuming binary classification

def test_predict_without_training():
    model = MLModel()
    with pytest.raises(Exception):
        model.predict([2, 3, 4])
