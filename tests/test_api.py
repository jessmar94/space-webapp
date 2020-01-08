import unittest
from model.api import API
import json, requests
from unittest.mock import Mock, patch

class TestAPI(unittest.TestCase):

    def setUp(self):
        self.api = API()

    def test(self):
        self.assertTrue(True)

    @patch('app.requests.get')
    def test_datetime(self, obj):
        """Mocking a whole function"""
        mock_get_patcher = patch('app.requests.get')
        json_response = {
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

        results = [
            'Thu 09 Jan 2020, 02:43',
            'Thu 09 Jan 2020, 04:18',
            'Thu 09 Jan 2020, 05:55',
            'Thu 09 Jan 2020, 07:33',
            'Thu 09 Jan 2020, 09:11'
            ]

        # Start patching 'requests.get'.
        mock_get = mock_get_patcher.start()

        # Configure the mock to return a response with status code 200 and relevant data.
        mock_get.return_value = Mock(status_code = 200)
        mock_get.return_value.json.return_value = json_response

        # Call the service, which will send a request to the server.
        response = self.api.datetime(json.parse(json_response))

        # Stop patching 'requests'.
        mock_get_patcher.stop()

        # Assert that the request-response cycle completed successfully.
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), results)


        # parameters = {
        #     "lat": 40.71,
        #     "lon": -74
        # }
        # response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)
        # results = [
        #     'Thu 09 Jan 2020, 02:43',
        #     'Thu 09 Jan 2020, 04:18',
        #     'Thu 09 Jan 2020, 05:55',
        #     'Thu 09 Jan 2020, 07:33',
        #     'Thu 09 Jan 2020, 09:11'
        #     ]
        #
        # self.assertEqual(response.status_code, 200)
        # self.assertEqual(self.api.datetime(response), results)

if __name__ == '__main__':
    unittest.main()
