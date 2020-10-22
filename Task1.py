"""
Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""

def division(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print('На 0 делить нельзя')


print('#' * 20)

while True:
    user_input = input('Введите делимое и делитель (Exit "q"): ')
    try:
        user_args = user_input.split()
        if len(user_args) == 2:
            print(division(int(user_args[0]), int(user_args[1])))
        elif user_input == 'q':
            break
    except ValueError:
        print('Нужно вводить числа')
