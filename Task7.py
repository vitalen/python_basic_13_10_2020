"""
 Реализовать проект «Операции с комплексными числами».
 Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
 Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
 Проверьте корректность полученного результата.
"""


class ComplexNumbers:

    def __init__(self, param):
        self.complex = complex(param)
        self.real = self.complex.real
        self.imag = self.complex.imag

    def __add__(self, other):
        return complex((self.real + other.real), (self.imag + other.imag))

    def __mul__(self, other):
        return complex(((self.real * other.real) - (self.imag + other.imag)),
                       ((self.imag * other.real) + (self.real * other.imag)))

    def __str__(self):
        return f'{self.complex}'


a = ComplexNumbers(3 + 4j)
b = ComplexNumbers(2)

print(a)
print(b)

c = ComplexNumbers(a + b)
print(c)
d = ComplexNumbers(a * b)
print(d)
