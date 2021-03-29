"""
Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.

Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
изученных на уроках по ООП.
"""


class WarehouseEquipment():
    printers = {}
    scanners = {}
    xeroxs = {}

    def __init__(self):
        self.name = input('Geben Sie bitte Name des Lagers ein (Leerzeichen Defaultwert): \n>>>')
        if self.name == '':
            self.name = 'Muster-Lager'
        adr_input = input('Adresse (Street hous zip city country) (Leerzeichen Defaultwert): \n>>>').split()
        if len(adr_input) == 0:
            adr_input.append("Bremer")
            adr_input.append("11")
            adr_input.append("21244")
            adr_input.append("Hamburg")
            adr_input.append("Germany")
        self.address = {"street": adr_input[0], "house": adr_input[1], "zip": adr_input[2], "city": adr_input[3],
                        "country": adr_input[4]}

        while True:
            try:
                user_input = input(
                    'Welches Objekt möchten Sie hinzufügen? \nGeben Sie printer, xeros oder scanner ein: \n>>>')
                if user_input == "printer":
                    while True:
                        count_input = input('Geben Sie bitte Anzahl der Geräte ein: \n>>>')
                        if not count_input.isdigit():
                            raise OwnException("Es ist kein Zahl!")
                        else:
                            data_input = input(
                                'Zum Beispiel: X360 Brother 50x140x40 120 (Leerzeichen Defaultwert) \n>>>').split()
                            if len(data_input) == 0:
                                data_input.append("X360")
                                data_input.append("Brother")
                                data_input.append("50x140x40")
                                data_input.append("120")
                            tmp = Printer(data_input[0], data_input[1], data_input[2], data_input[3])
                            self.department_printers(count_input, tmp)
                            break
                if user_input == "xerox":
                    while True:
                        count_input = input('Geben Sie bitte Anzahl der Geräte ein: \n>>>')
                        if not count_input.isdigit():
                            raise OwnException("Es ist kein Zahl!")
                        else:
                            data_input = input(
                                'Zum Beispiel: YAA Xerox 30x100x40 01.03.2020 (Leerzeichen Defaultwert) \n>>>').split()
                            if len(data_input) == 0:
                                data_input.append("YAA")
                                data_input.append("Xerox")
                                data_input.append("30x100x40")
                                data_input.append("01.03.2020")
                            tmp = Xerox(data_input[0], data_input[1], data_input[2], data_input[3])
                            self.department_xeroxs(count_input, tmp)
                            break
                if user_input == "scanner":
                    while True:
                        count_input = input('Geben Sie bitte Anzahl der Geräte ein: \n>>>')
                        if not count_input.isdigit():
                            raise OwnException("Es ist kein Zahl!")
                        else:
                            data_input = input(
                                'Zum Beispiel: T1000 Terminator 90x60x90 2000 (Leerzeichen Defaultwert) \n>>>').split()
                            if len(data_input) == 0:
                                data_input.append("T1000")
                                data_input.append("Terminator")
                                data_input.append("90x60x90")
                                data_input.append("2000")
                            tmp = Scanner(data_input[0], data_input[1], data_input[2], data_input[3])
                            self.department_scanners(count_input, tmp)
                            break
                if user_input == "stop":
                    break
            except OwnException as err:
                print(err)

    def __str__(self):
        result = f"Name: {self.name.upper()}, \n{self.address['street']} {self.address['house']}\n" \
                 f"{self.address['zip']} - {self.address['city']}\n{self.address['country']} \n"
        result += '\nPrinters: \n'
        for key, value in self.printers.items():
            if key == 'data':
                result += f'    {value[0]}\n'
            else:
                result += f'    Count: {value}\n'
        result += '\nScanners: \n'
        for key, value in self.scanners.items():
            if key == 'data':
                result += f'    {value[0]}\n'
            else:
                result += f'    Count: {value}\n'
        result += '\nXeroxs:  \n'
        for key, value in self.xeroxs.items():
            if key == 'data':
                result += f'    {value[0]}\n'
            else:
                result += f'    Count: {value}\n'
        return result

    def department_printers(self, count, *printers):
        self.printers.update({"count": count, "data": printers})

    def department_scanners(self, count, *scanners):
        self.scanners.update({"count": count, "data": scanners})

    def department_xeroxs(self, count, *xeroxs):
        self.xeroxs.update({"count": count, "data": xeroxs})

    @staticmethod
    def valid_count_param(param):
        if not isinstance(param, int):
            return False

    def __setitem__(self, key, value):
        pass


class OwnException(Exception):
    def __init__(self, param):
        self.param = param


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


we = WarehouseEquipment()
print(we)
