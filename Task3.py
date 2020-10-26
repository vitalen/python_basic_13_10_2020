"""
Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Необходимо решить задание в одну строку.
Подсказка: использовать функцию range() и генератор.
"""
def my_range(start, end):
    result = []
    while start < end:
        result.append(start)
        start += 1
    return result


my_list = [el for el in my_range(20, 240) if el % 20 == 0 or el % 21 == 0]
print(my_list)
