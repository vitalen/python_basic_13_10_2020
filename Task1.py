"""
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
31       22
37       43
51       86
3 5 32 246 -1 64 -8
3583 8371
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем
с первым элементом первой строки второй матрицы и т.д.
"""


class Matrix():

    def __init__(self, param):
        if isinstance(param, list):
            self.my_list = param

    def __str__(self):
        result = ''
        for el in self.my_list:
            tmp = ''
            for itm in el:
                tmp += str(itm) + ' '
            result += tmp + '\n'
        return result

    def __add__(self, other):
        tmp_0 = []
        result = []
        for j in range(max(len(self.my_list), len(other.my_list))):
            if j < len(self.my_list):
                value = self.my_list[j]
            else:
                value = []
            if j < len(other.my_list):
                value2 = other.my_list[j]
            else:
                value2 = []

            for i in range(max(len(value), len(value2))):
                temp = 0
                if i < len(value):
                    temp += value[i]
                if i < len(value2):
                    temp += value2[i]
                tmp_0.append(temp)
            result.append(tmp_0)
            tmp_0 = []
        self.my_list = result
        return Matrix(self.my_list)


m_1 = Matrix([[31, 22], [37, 43], [51, 86]])
print(m_1)

m_2 = Matrix([[3, 5, 32], [2, 4, 6], [-1, 64, -8]])
print(m_2)

m_3 = Matrix([[3, 5, 8, 3], [8, 3, 7, 1]])

print(m_1 + m_2 + m_3)
