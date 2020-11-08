class Temperature:
    __KELVIN_CONST_C = 273.15
    __slots__ = ('kelvin',)

    def __init__(self):
        self.kelvin = 0

    @property
    def celsius(self):
        return self.kelvin - self.__KELVIN_CONST_C

    @celsius.setter
    def celsius(self, value):
        self.kelvin = value + self.__KELVIN_CONST_C

    @property
    def fahrenheit(self):
        return self.kelvin * 1.8 - 459.67

    @fahrenheit.setter
    def fahrenheit(self, value):
        self.kelvin = (value + 459.67) / 1.8


if __name__ == '__main__':
    termo = Temperature()
    termo.celsius = 0
    print(termo.celsius)
    print(termo.kelvin)
    print(termo.fahrenheit)