"""
Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно.Для определения расхода ткани по каждому типу одежды использовать формулы:
для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
"""
from abc import ABC, abstractmethod


class Clothes(ABC):
    costums = []
    topcoats = []

    @abstractmethod
    def get_mass(self):
        pass

    @classmethod
    def get_result(cls):
        tmp_1 = sum([el.get_mass for el in cls.costums])
        tmp_2 = sum([el.get_mass for el in cls.topcoats])
        return tmp_1 + tmp_2


class Costume(Clothes):

    def __init__(self, param, param_2):
        self.growth = param
        self.name = param_2
        super().costums.append(self)

    @property
    def get_mass(self):
        return 2 * self.growth + 0.3

    def __str__(self):
        return f"Параметры в классе: " \
               f"{self.name}, {self.get_mass}"


class Topcoat(Clothes):

    def __init__(self, param, param_2):
        self.size = param
        self.name = param_2
        super().topcoats.append(self)

    @property
    def get_mass(self):
        return self.size / 6.5 + 0.5

    def __str__(self):
        return f"Параметры в классе: " \
               f"{self.name}, {self.get_mass}"


costume = Costume(200, 'TomTailor')
print(costume.get_mass)
print(costume)

topcoat = Topcoat(135, 'Reebok')
print(topcoat.get_mass)
print(topcoat)

print(Clothes.get_result())
