"""
 Реализовать базовый класс Worker (работник),
 в котором определить атрибуты: name, surname, position (должность), income (доход).
 Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, например,
 {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
 В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и
 дохода с учетом премии (get_total_income).
 Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
 проверить значения атрибутов, вызвать методы экземпляров).
"""
class Worker():
    name = ''
    surname = ''
    position = ''
    _income = {}

    def __init__(self, param_1, param_2, param_3, param_4):
        self.name = param_1
        self.surname = param_2
        self.position = param_3
        self._income = param_4

    def get_income(self):
        return self._income


class Position(Worker):
    def __init__(self):
        input_name = input('name:')
        input_surname = input('surname:')
        input_position = input('position:')
        input_wage = int(input('wage:'))
        input_bonus = int(input('bonus:'))
        super().__init__(input_name, input_surname, input_position, {"wage": input_wage, "bonus": input_bonus})

    def get_full_name(self):
        print(f'полного имени сотрудника: {self.surname} {self.name} нa должности {self.position}')

    def get_total_income(self):
        print(f'доход с учетом премии сотрудника: {self.get_income()["wage"] + self.get_income()["bonus"]}')


assisten = Position()
assisten.get_full_name()
assisten.get_total_income()
