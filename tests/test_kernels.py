import requests
import unittest

BASE_URL = "http://127.0.0.1:8000/kernels"

class TestKernels(unittest.TestCase):
    def test_get_all_kernels_status_code_200(self):
        res = requests.get(BASE_URL)
        self.assertEqual(res.status_code, 200)

    def test_get_all_kernels_response_body(self):
        res = requests.get(BASE_URL)
        self.assertIsNotNone(res.json())

    def test_wrong_end_point_status_code_404(self):
        res = requests.get(BASE_URL[:len(BASE_URL) - 1]) # endpoint will be 'kernel' instead of 'kernels'
        self.assertEqual(res.status_code, 404)

    def test_get_kernel_by_name_status_code_200(self):
        res = requests.get(BASE_URL + "/Linux")
        self.assertEqual(res.status_code, 200)

    def test_get_distro_by_name_response_body(self):
        res = requests.get(BASE_URL + "/Linux")
        self.assertIsNotNone(res.json())

        # testing fields
        self.assertIn("id", res.json())
        self.assertIn("name", res.json())
        self.assertIn("latest_version", res.json())

        # testing value of specific field
        self.assertIn("Linux", res.json()["name"])

    def test_get_inexistent_distro_response_body(self):
        res = requests.get(BASE_URL + "/Solaris")
        self.assertEqual(res.json(), None)

if __name__ == "__main__":
    unittest.main()
