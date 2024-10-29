# src/tests/test_data_processing.py

import unittest
import pandas as pd
from src.data_processing import DataProcessor  # Assuming you have a DataProcessor class

class TestDataProcessor(unittest.TestCase):
    
    def setUp(self):
        self.processor = DataProcessor()

    def test_data_cleaning(self):
        raw_data = pd.DataFrame({'A': [1, None, 3], 'B': [4, 5, 6]})
        cleaned_data = self.processor.clean_data(raw_data)
        self.assertFalse(cleaned_data.isnull().values.any())

    def test_feature_engineering(self):
        raw_data = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
        engineered_data = self.processor.feature_engineer(raw_data)
        self.assertIn('A_B', engineered_data.columns)  # Assuming 'A_B' is a new feature

if __name__ == '__main__':
    unittest.main()
