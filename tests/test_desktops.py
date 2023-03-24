import requests
import unittest

BASE_URL = "http://127.0.0.1:8000/desktops"

class TestDesktops(unittest.TestCase):
    def test_get_all_desktops_status_code_200(self):
        res = requests.get(BASE_URL)
        self.assertEqual(res.status_code, 200)

    def test_get_all_desktops_response_body(self):
        res = requests.get(BASE_URL)
        self.assertIsNotNone(res.json())

    def test_wrong_end_point_status_code_404(self):
        res = requests.get(BASE_URL[:len(BASE_URL) - 1]) # endpoint will be 'desktop' instead of 'desktops'
        self.assertEqual(res.status_code, 404)

    def test_get_desktop_by_name_status_code_200(self):
        res = requests.get(BASE_URL + "/GNOME")
        self.assertEqual(res.status_code, 200)

    def test_get_desktop_by_name_response_body(self):
        res = requests.get(BASE_URL + "/GNOME")
        self.assertIsNotNone(res.json())

        # testing fields
        self.assertIn("id", res.json())
        self.assertIn("name", res.json())
        self.assertIn("latest_version", res.json())

        # testing value of specific field
        self.assertIn("GNOME", res.json()["name"])

    def test_get_inexistent_distro_response_body(self):
        res = requests.get(BASE_URL + "/KDE")
        self.assertEqual(res.json(), None)

if __name__ == "__main__":
    unittest.main()
