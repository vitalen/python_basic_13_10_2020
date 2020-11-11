"""
 Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
 В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц,
 год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
 месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
"""


class Data():
    day = 1
    month = 1
    year = 1

    def __init__(self, dat_str):
        self.datum = dat_str

    @classmethod
    def format_str(cls, param):
        try:
            cls.year = Data.valid_date('year', int(param.split('-')[2]))
            cls.month = Data.valid_date('month', int(param.split('-')[1]))
            cls.day = Data.valid_date('day', int(param.split('-')[0]), int(param.split('-')[1]),
                                      int(param.split('-')[2]))
        except ValueError:
            pass

    @staticmethod
    def valid_date(*args):
        if args[0] == 'year' and args[1] in [idx for idx in range(1900, 2100)]:
            return args[1]
        elif args[0] == 'month' and args[1] in [idx for idx in range(1, 13)]:
            return args[1]
        elif args[0] == 'day' and args[2] in [1, 3, 5, 7, 8, 10, 12] and args[1] in [idx for idx in range(1, 32)]:
            return args[1]
        elif args[0] == 'day' and args[2] in [4, 6, 9, 11] and args[1] in [idx for idx in range(1, 31)]:
            return args[1]
        elif args[0] == 'day' and args[2] == 2 and ((args[3] % 4) == 0) and args[1] in [idx for idx in range(1, 30)]:
            return args[1]
        elif args[0] == 'day' and args[2] == 2 and ((args[3] % 4) != 0) and args[1] in [idx for idx in range(1, 29)]:
            return args[1]
        else:
            raise Exception(f'Ошибка: {args}')


mc = Data('29-2-2024')

mc.format_str(mc.datum)

print(f'day: {mc.day}, month: {mc.month}, year: {mc.year} ')
