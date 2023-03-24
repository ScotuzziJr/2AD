import requests
import unittest

BASE_URL = "http://127.0.0.1:8000/healthcheck"

class TestHealthcheck(unittest.TestCase):
    def test_status_code_200(self):
        res = requests.get(BASE_URL)
        
        self.assertEqual(res.status_code, 200)

    def test_fail_status_code_201(self):
        res = requests.get(BASE_URL)
        self.assertEqual(res.status_code, 201)

    def test_response_body_ok_field(self):
        res = requests.get(BASE_URL)
        self.assertIsNotNone(res.json()["OK"])

if __name__ == "__main__":
    unittest.main()
