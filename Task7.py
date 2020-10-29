"""
Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.

Пример строки файла: firm_1 ООО 10000 5000.

Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.

Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).

Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].

Итоговый список сохранить в виде json-объекта в соответствующий файл.

Пример json-объекта:

[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджеры контекста.
"""
import json
list_profit = []
dict_profit = {}
average_profit = 0


def my_diff(param_1, param_2):
    try:
        return int(param_1) - int(param_2)
    except ValueError:
        print('ValueError')


def format_line(param):
    tmp = param.split()
    return tmp[0], tmp[1], tmp[2], tmp[3]


try:
    with open("file_7.txt", "r") as my_file:
        idx = 0
        for line in my_file:
            a, b, c, d = format_line(line)
            profit = my_diff(c, d)
            dict_profit.update({a: profit})
            if profit >= 0:
                print(f'прибыль компании {b} {a}: {profit}')
                average_profit += profit
                idx += 1
        print(f'Cредняя прибыль: {(average_profit / idx):.2f}')
        list_profit.append(dict_profit)
        list_profit.append({'average_profit': (average_profit / idx).__round__(2)})
        print(list_profit)
except IOError:
    print('IOError')
except ZeroDivisionError:
    print('ZeroDivisionError')



try:
    with open("file_7.json", "w") as my_object:
        data = json.dumps(list_profit)
        my_object.write(data)
except IOError:
    print('IOError')