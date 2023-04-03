import unittest
from Gahdf5.Gahdf5 import Gahdf5


class Gahdf5TestCase(unittest.TestCase):
    def setUp(self):
        self.gahdf5 = Gahdf5("data")

    def test_create_data_type(self):
        result = type(self.gahdf5.create_data())
        self.assertEqual(result, dict)

    def test_create_data_values(self):
        result = str(self.gahdf5.create_data())
        compare = open("data_test.txt", "r")
        self.assertEqual(result, compare.read())
        compare.close()


if __name__ == '__main__':
    unittest.main()
