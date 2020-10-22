"""
Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел.
Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введен после нескольких чисел,
то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого
завершить программу.
"""
sum_all = 0


def my_sum(input_list):
    try:
        idx = 0
        tmp_sum = 0
        while idx < len(input_list):
            tmp_sum += int(input_list[idx])
            idx += 1
        global sum_all
        sum_all += tmp_sum
        return sum_all
    except ValueError:
        print('Нужно вводить числа')
        return None


while True:
    try:
        user_input = input('строку чисел, разделенных пробелом (Exit "q"): ')
        if user_input == 'q':
            break
        else:
            user_args = user_input.split()
            if "q" in user_args:
                user_args.remove("q")
                print(my_sum(user_args))
                break
            else:
                print(my_sum(user_args))
    except ValueError:
        print('Нужно вводить числа')
        continue
