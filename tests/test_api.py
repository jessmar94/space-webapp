import unittest
from model.api import API

class TestAPI(unittest.TestCase):

    def setUp(self):
        self.api = API()

    def test(self):
        self.assertTrue(True)



if __name__ == '__main__':
    unittest.main()
