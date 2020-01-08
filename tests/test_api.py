import unittest
from model.api import API
import json, requests

class TestAPI(unittest.TestCase):

    def setUp(self):
        self.api = API()

    def test(self):
        self.assertTrue(True)

    def test_datetime(self):
        response2 = {
            "message": "success",
            "request": {
                "altitude": 100,
                "datetime": 1578497662,
                "latitude": 40.71,
                "longitude": -74.0,
                "passes": 5
            },
            "response": [
                {
                    "duration": 466,
                    "risetime": 1578537826
                },
                {
                    "duration": 650,
                    "risetime": 1578543504
                },
                {
                    "duration": 609,
                    "risetime": 1578549348
                },
                {
                    "duration": 556,
                    "risetime": 1578555238
                },
                {
                    "duration": 605,
                    "risetime": 1578561078
                }
            ]
        }
        parameters = {
            "lat": 40.71,
            "lon": -74
        }
        response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)
        results = [
            'Thu 09 Jan 2020, 02:43',
            'Thu 09 Jan 2020, 04:18',
            'Thu 09 Jan 2020, 05:55',
            'Thu 09 Jan 2020, 07:33',
            'Thu 09 Jan 2020, 09:11'
            ]
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.api.datetime(response), results)

if __name__ == '__main__':
    unittest.main()
