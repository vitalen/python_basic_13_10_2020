"""
Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""


def my_max(*args):
    idx = 0
    max_value = 0
    my_list = list(args)
    while idx < len(my_list):
        try:
            tmp = int(args[idx])
            if max_value < tmp:
                max_value = tmp
            idx += 1
        except ValueError:
            print('Error')
            break
    return max_value


def my_sort(*args):
    idx = 0
    max_value = 0
    my_result = []
    my_tmp_list = list(args)
    while len(my_result) < len(args):
        while idx < len(my_tmp_list):
            try:
                tmp = int(my_tmp_list[idx])
                if max_value < tmp:
                    max_value = tmp
                idx += 1
            except ValueError:
                print('Error')
                break
        my_tmp_list.remove(max_value)
        my_result.append(max_value)
        idx = 0
        max_value = 0
    return my_result


# print(my_sort(2, 9, 8, 52, 4, 6, 8, 7, 2, 3))


def my_func(var_1, var_2, var_3):
    var_tmp = my_sort(var_1, var_2, var_3)
    return var_tmp[0] + var_tmp[1]


while True:
    try:
        user_input = input('Введите три числа, разделенных пробелами (Exit "q"): ')
        user_args = user_input.split()
        print(my_func(int(user_args[0]), int(user_args[1]), int(user_args[2])))
        break
    except ValueError:
        print('Пожалуйста, проверьте свой ввод!')
        continue
