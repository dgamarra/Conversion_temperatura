class Temperatura_Convert:
    def celsius_to_fahrenheit(self, celsius):
        return (celsius * 9 / 5) + 32

    def celsius_to_kelvin(self, celsius):
        return celsius + 273.15

    def fahrenheit_to_celsius(self, fahrenheit):
        return (fahrenheit - 32) * 5 / 9

    def fahrenheit_to_kelvin(self, fahrenheit):
        return self.fahrenheit_to_celsius(fahrenheit) + 273.15

    def kelvin_to_celsius(self, kelvin):
        return kelvin - 273.15

    def kelvin_to_fahrenheit(self, kelvin):
        return self.celsius_to_fahrenheit(self.kelvin_to_celsius(kelvin))
