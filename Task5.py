"""
Реализовать формирование списка, используя функцию range() и возможности генератора.
В список должны войти четные числа от 100 до 1000 (включая границы).
Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce().
"""
from functools import reduce
from my_functions import my_reduce

my_list = [el for el in range(100, 1001, 2)]


def my_func(pre_el, el):
    return pre_el * el


print('#' * 20)
print('1 вариант')
print(reduce(lambda el, result: result * el, my_list))


print('#' * 20)
print('2 вариант')
print(my_reduce(my_func, my_list))
