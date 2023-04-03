import unittest

import requests

BASE_URL = "http://127.0.0.1:8000/distros"


class TestDistros(unittest.TestCase):
    def test_get_all_distros_status_code_200(self):
        res = requests.get(BASE_URL)
        self.assertEqual(res.status_code, 200)

    def test_get_all_distros_response_body(self):
        res = requests.get(BASE_URL)
        self.assertIsNotNone(res.json())

    def test_wrong_end_point_status_code_404(self):
        res = requests.get(
            BASE_URL[: len(BASE_URL) - 1]
        )  # endpoint will be 'distro' instead of 'distros'
        self.assertEqual(res.status_code, 404)

    def test_get_distro_by_name_status_code_200(self):
        res = requests.get(BASE_URL + "/Ubuntu")
        self.assertEqual(res.status_code, 200)

    def test_get_distro_by_name_response_body(self):
        res = requests.get(BASE_URL + "/Ubuntu")
        self.assertIsNotNone(res.json())

        # testing fields
        self.assertIn("id", res.json())
        self.assertIn("name", res.json())
        self.assertIn("description", res.json())
        self.assertIn("based_on", res.json())
        self.assertIn("desktop", res.json())
        self.assertIn("kernel", res.json())
        self.assertIn("latest_version", res.json())
        self.assertIn("website", res.json())

        # testing value of specific field
        self.assertIn("Ubuntu", res.json()["name"])

    def test_get_inexistent_distro_response_body(self):
        res = requests.get(BASE_URL + "/MX Linux")
        self.assertEqual(res.json(), None)


if __name__ == "__main__":
    unittest.main()
