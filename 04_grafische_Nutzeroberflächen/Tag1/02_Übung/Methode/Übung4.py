class TemperatureConverter:
    @staticmethod
    def zu_fahrenheit(x):
        return ((x * 9 / 5) + 32)

    @staticmethod
    def zu_celsius(x):
        return ((x - 32) * 5 / 9)


print(TemperatureConverter.zu_fahrenheit(30))
print(TemperatureConverter.zu_celsius(100))
