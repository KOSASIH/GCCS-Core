# src/tests/test_geoengineering.py

import unittest
from src.geoengineering import GeoengineeringModel  # Assuming you have a GeoengineeringModel class

class TestGeoengineeringModel(unittest.TestCase):
    
    def setUp(self):
        self.model = GeoengineeringModel()

    def test_model_parameters(self):
        params = self.model.get_parameters()
        self.assertIn('albedo', params)
        self.assertIn('solar_radiation', params)

    def test_model_simulation(self):
        result = self.model.simulate()
        self.assertIsInstance(result, dict)  # Assuming the result is a dictionary

if __name__ == '__main__':
    unittest.main()
