# src/tests/test_api.py
import unittest
from src.api.api import app

class TestAPI(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_get_endpoint(self):
        response = self.app.get('/api/some_endpoint')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
