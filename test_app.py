import unittest
from app import app

class TestApp(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_home(self):
        response = self.client.get('/')
        self.assertEqual(response.data, b'Hello, CI/CD with Tests!')

if __name__ == '__main__':
    unittest.main()

