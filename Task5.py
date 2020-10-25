"""
Реализовать формирование списка, используя функцию range() и возможности генератора.
В список должны войти четные числа от 100 до 1000 (включая границы).
Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce().
"""
from functools import reduce

my_list = [el for el in range(100, 1001, 2)]

print('#' * 20)
print('1 вариант')
print(reduce(lambda el, result: result * el, my_list))

print('#' * 20)
print('2 вариант')


def my_func(pre_el, el):
    return pre_el * el


print(reduce(my_func, my_list))
