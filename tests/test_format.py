import unittest
from model.format import Formatter
import json, requests

class TestFormatter(unittest.TestCase):

    def setUp(self):
        self.format = Formatter()

    def test(self):
        self.assertTrue(True)

    def test_datetime(self):
        pass_times = [
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
        results = [
            'Thu 09 Jan 2020, 02:43',
            'Thu 09 Jan 2020, 04:18',
            'Thu 09 Jan 2020, 05:55',
            'Thu 09 Jan 2020, 07:33',
            'Thu 09 Jan 2020, 09:11'
            ]
        self.assertEqual(self.format.datetime(pass_times), results)

    def test_array_length(self):
        pass_times = [
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
        results = [
            'Thu 09 Jan 2020, 02:43',
            'Thu 09 Jan 2020, 04:18',
            'Thu 09 Jan 2020, 05:55',
            'Thu 09 Jan 2020, 07:33',
            'Thu 09 Jan 2020, 09:11'
            ]
        list = self.format.datetime(pass_times)
        self.assertEqual(len(list), 5)

if __name__ == '__main__':
    unittest.main()
