# src/tests/test_climate_models.py

import unittest
from src.climate_models import ClimateModel  # Assuming you have a ClimateModel class

class TestClimateModel(unittest.TestCase):
    
    def setUp(self):
        self.model = ClimateModel()

    def test_model_initialization(self):
        self.assertIsNotNone(self.model)

    def test_model_prediction(self):
        input_data = [1, 2, 3]  # Example input
        prediction = self.model.predict(input_data)
        self.assertIsInstance(prediction, float)  # Assuming the prediction is a float

if __name__ == '__main__':
    unittest.main()
