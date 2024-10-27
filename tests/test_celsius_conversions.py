import unittest
from src.logica.Temperature_converter import Temperatura_Convert


class TestCelsiusConversions(unittest.TestCase):
    def setUp(self):
        self.conversion = Temperatura_Convert()

    def tearDown(self):
        self.conversion = None

    def test_celsius_to_fahrenheit(self):
        self.assertAlmostEqual(self.conversion.celsius_to_fahrenheit(0), 32)
        self.assertAlmostEqual(self.conversion.celsius_to_fahrenheit(100), 212)

    def test_celsius_to_kelvin(self):
        self.assertAlmostEqual(self.conversion.celsius_to_kelvin(0), 273.15)
        self.assertAlmostEqual(self.conversion.celsius_to_kelvin(100), 373.15)


if __name__ == '__main__':
    unittest.main()
