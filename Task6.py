"""
Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.

Примеры строк файла:

Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —
Пример словаря:

{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""
my_dict = {}


def my_sum(param_a, param_b):
    return param_a + param_b


def my_reduce(func, param):
    try:
        result = int(snip_digit(param[0]))
        for el in param[1:]:
            result = func(result, int(snip_digit(el)))
        return result
    except ValueError:
        print('ValueError')


def snip_digit(param):
    try:
        result = ''
        for elem in param:
            if elem.isdigit():
                result += elem
        return int(result)
    except ValueError:
        #print(f'ValueError: {elem}')
        return 0


my_list = []
try:
    with open("file_6.txt", "r") as my_file:
        for line in my_file:
            tmp_field = line.split(':')
            tmp_hours = tmp_field[1].split()
            tmp = my_reduce(my_sum, tmp_hours)
            my_dict.update({tmp_field[0]: tmp})
except IOError:
    print('Error')

print(my_dict)
