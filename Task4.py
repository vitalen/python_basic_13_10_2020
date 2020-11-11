"""
Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
"""


class WarehouseEquipment():
    def __init__(self, name, address):
        self.name = name
        self.address = address
    def __str__(self):
        return f"Name: {self.name}, \nAddress: \n{self.address['street']} {self.address['house']}\n" \
               f"{self.address['zip']} - {self.address['city']}\n{self.address['country']}"


class Equipment():
    def __init__(self, name, brand, masse):
        self.name = name
        self.brand = brand
        self.masse = masse


class Printer(Equipment):
    def __init__(self, param_1, param_2, param_3, speed):
        super().__init__(param_1, param_2, param_3)
        self.speed = speed

    def __str__(self):
        return f"Name: {self.name}, Brand: {self.brand}, Masse: {self.masse}, Speed: {self.speed}"


class Scanner(Equipment):
    def __init__(self, param_1, param_2, param_3, dpi_value):
        super().__init__(param_1, param_2, param_3)
        self.dpi_value = dpi_value

    def __str__(self):
        return f"Name: {self.name}, Brand: {self.brand}, Masse: {self.masse}, DPI: {self.dpi_value}"


class Xerox(Equipment):
    def __init__(self, param_1, param_2, param_3, date_of_production):
        super().__init__(param_1, param_2, param_3)
        self.date_of_production = date_of_production

    def __str__(self):
        return f"Name: {self.name}, Brand: {self.brand}, Masse: {self.masse}, Date of production: {self.date_of_production} "


we = WarehouseEquipment("New WareHouse", {"street": "Bremer Str.", "house": 11, "zip": 21244, "city": "Hamburg", "country": "Germany"})
print(we)

printer = Printer("X199", "Brother",  "50x135x40", "60 Site pro Minute")
print(printer)