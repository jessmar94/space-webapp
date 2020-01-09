import unittest
from model.lat_long import Coordinates

class TestCoordinates(unittest.TestCase):

    def setUp(self):
        self.coords = Coordinates()

    def test(self):
        self.assertTrue(True)

    def test_lat_long(self):
        city = "New York"
        params = {
            "lat": 40.71,
            "lon": -74,
        }
        self.assertEqual(self.coords.lat_long(city), params)

if __name__ == '__main__':
    unittest.main()
