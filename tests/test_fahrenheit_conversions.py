import unittest
from src.logica.Temperature_converter import Temperatura_Convert


class TestFahrenheitConversions(unittest.TestCase):
    def setUp(self):
        self.convertir = Temperatura_Convert()

    def tearDown(self):
        self.convertir = None

    def test_fahrenheit_to_celsius(self):
        self.assertAlmostEqual(self.convertir.fahrenheit_to_celsius(32), 0)
        self.assertAlmostEqual(self.convertir.fahrenheit_to_celsius(212), 100)

    def test_fahrenheit_to_kelvin(self):
        self.assertAlmostEqual(self.convertir.fahrenheit_to_kelvin(32), 273.15)
        self.assertAlmostEqual(self.convertir.fahrenheit_to_kelvin(212), 373.15)


if __name__ == '__main__':
    unittest.main()
