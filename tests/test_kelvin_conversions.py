import unittest
from src.logica.Temperature_converter import Temperatura_Convert


class TestKelvinConversions(unittest.TestCase):
    def setUp(self):
        self.convertir = Temperatura_Convert()

    def tearDown(self):
        self.convertir = None

    def test_kelvin_to_celsius(self):
        self.assertAlmostEqual(self.convertir.kelvin_to_celsius(273.15), 0)
        self.assertAlmostEqual(self.convertir.kelvin_to_celsius(373.15), 100)

    def test_kelvin_to_fahrenheit(self):
        self.assertAlmostEqual(self.convertir.kelvin_to_fahrenheit(273.15), 32)
        self.assertAlmostEqual(self.convertir.kelvin_to_fahrenheit(373.15), 212)


if __name__ == '__main__':
    unittest.main()
