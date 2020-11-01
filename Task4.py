"""
Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""
class Car():
    def __init__(self, param_1, param_2, param_3, param_4):
        self.speed = param_1
        self.color = param_2
        self.name = param_3
        self.is_police = param_4

    def go(self):
        print(f'Mашина {self.name} ({self.color}) поехала.')

    def stop(self):
        print(f'Mашина остановилась.')

    def turn(self, direction):
        print(f'Mашина повернула нa {direction}.')

    def show_speed(self):
        print(f'Cкорость: {self.speed}')


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            print(f'Achtung! Превышении скорости: {self.speed}')
        else:
            print(f'Cкорость: {self.speed}')


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            print(f'Achtung! Превышении скорости: {self.speed}')
        else:
            print(f'Cкорость: {self.speed}')


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class PolicetCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


smart = TownCar(59, 'green', 'mini', False)
traktor = WorkCar(45, 'red', 'T40', False)
audi = SportCar(180, 'blue-white', 'R8', False)
uaz = PolicetCar(70, 'yellow', '428', True)

smart.go()
smart.turn('left')
smart.show_speed()
smart.stop()
print('#'*10)

traktor.go()
traktor.turn('rigth')
traktor.show_speed()
traktor.stop()
print('#'*10)

audi.go()
audi.turn('left')
audi.show_speed()
audi.stop()
print('#'*10)

uaz.go()
uaz.turn('left')
uaz.show_speed()
uaz.stop()

