"""
Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
from itertools import count


def my_sum(param_a, param_b):
    return param_a + param_b


def my_reduce(func, param):
    try:
        result = float(param[0])
        for el in param[1:]:
            result = func(result, float(el))
        return result
    except ValueError:
        print('ValueError')


def read_sum_from_file():
    try:
        with open("file_5.txt", "r") as output_file:
            content = output_file.readline().split()
            print(f'content: {my_reduce(my_sum, content)}')
    except IOError:
        print('IOError')


try:
    with open("file_5.txt", "w") as my_file:
        tmp_value = ''
        for el in count(5):
            if el > 35:
                break
            else:
                tmp_value += ' ' + str(el)
        my_file.write(tmp_value)
except IOError:
    print('Error')

read_sum_from_file()
