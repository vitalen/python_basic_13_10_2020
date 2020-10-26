"""
Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""

from sys import argv

script_name, count_hour, price_hour, surprice = argv


def my_calc_salary():
    try:
        print(int(count_hour) * int(price_hour) + int(surprice))
        return int(count_hour) * int(price_hour) + int(surprice)
    except ValueError:
        print('Error')


my_calc_salary()
