import unittest
from tasks.temperatura.main import convertir_temperatura

class TestTemperatura(unittest.TestCase):
    def test_celsius_a_fahrenheit(self):
        self.assertEqual(convertir_temperatura(0, 'Celsius', 'Fahrenheit'), 32)

    def test_fahrenheit_a_celsius(self):
        self.assertEqual(convertir_temperatura(32, 'Fahrenheit', 'Celsius'), 0)

    def test_kelvin_a_celsius(self):
        self.assertEqual(convertir_temperatura(273.15, 'Kelvin', 'Celsius'), 0)

    def test_celsius_a_kelvin(self):
        self.assertEqual(convertir_temperatura(0, 'Celsius', 'Kelvin'), 273.15)

    def test_fahrenheit_a_kelvin(self):
        self.assertEqual(convertir_temperatura(32, 'Fahrenheit', 'Kelvin'), 273.15)

    def test_kelvin_a_fahrenheit(self):
        self.assertEqual(convertir_temperatura(273.15, 'Kelvin', 'Fahrenheit'), 32)

if __name__ == '__main__':
    unittest.main()