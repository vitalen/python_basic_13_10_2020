"""
 Реализовать класс Stationery (канцелярская принадлежность).
 Определить в нем атрибут title (название) и метод draw (отрисовка).
 Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
 В каждом из классов реализовать переопределение метода draw. Для каждого из классов методы должен выводить уникальное сообщение.
 Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""


class Stationery:
    title = ''

    def __init__(self, param_1):
        self.title = param_1

    def draw(self):
        print('Запуск отрисовки.')


class Pen(Stationery):
    def __init__(self, param_1):
        super().__init__(param_1)

    def draw(self):
        print(f'Запуск отрисовки от {self.title} (класс Pen)')


class Pencil(Stationery):
    def __init__(self, param_1):
        super().__init__(param_1)

    def draw(self):
        print(f'Запуск отрисовки от {self.title} (класс Pencil)')


class Hanle(Stationery):
    def __init__(self, param_1):
        super().__init__(param_1)

    def draw(self):
        print(f'Запуск отрисовки от {self.title} (класс Hanle)')



black = Pen('Pelikan')
black.draw()

caran = Pencil('Caran d`Ache')
caran.draw()

boby = Hanle('Alphacolor')
boby.draw()