class GarageIterator:
    def __init__(self, box):
        self.idx = 0
        self.__box = box

    def __next__(self):
        self.idx += 1
        len_box = len(self.__box)
        while self.idx - 1 < len_box:
            car = self.__box[self.idx - 1]
            if car.vin[-1] == 'q':
                self.idx += 1
            else:
                return car
        raise StopIteration


class Garage:
    __instance = None

    def __init__(self, name):
        self.__box = []
        self.name = name

    def add_cars(self, *cars):
        self.__box.extend(cars)

    def __getitem__(self, item):
        if isinstance(item, int):
            return self.__box[item]
        if isinstance(item, str):
            for itm in self.__box:
                if item == itm.name or item == itm.vin:
                    return itm
        raise KeyError('Авто с таким отсутсвуете')

    def __iter__(self):
        return GarageIterator(self.__box)

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super().__new__(cls)
        return cls.__instance


class Car:
    __vin_codes = {}

    def __init__(self, name, vin):
        self.name = name
        self.__vin = str(vin)

    @property
    def vin(self):
        return self.__vin

    # @vin.setter
    # def vin(self, value):
    #     print(value, 'not set')

    def __str__(self):
        return f'{self.name}: {self.vin}'

    def __eq__(self, other):
        return self.name == other.name

    def __new__(cls, name, vin):
        instance = cls.__vin_codes.get(vin)
        if instance:
            return instance
        instance = super().__new__(cls)
        cls.__vin_codes[vin] = instance
        return instance

    @classmethod
    def factory(cls, name, count, vin_prefix):
        result = []
        for idx in range(count):
            result.append(cls(name, f"{vin_prefix}-{idx}"))
        return result

    @staticmethod
    def some(a, b):
        return a + b


if __name__ == '__main__':
    garage = Garage('Crazy Monkey')
    car1 = Car('FORD', 465476548684486486)
    car2 = Car('TESLA', 45475445454765)
    car3 = Car('LADA', 464846846648468)

    garage.add_cars(car1, car2, car3)
    garage.add_cars(Car('LADA', "fjfhkjfhkfhkq"))
    garage.add_cars(Car('PONTIAC', "fjfhkjfh3535373q"))
    print(1)