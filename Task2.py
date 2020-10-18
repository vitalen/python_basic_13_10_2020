"""
Для списка реализовать обмен значений соседних элементов, т.е.
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().
"""
list_1 = []
while True:
    user_input = input('У пользователя запрашивать новый элемент (или "exit"): ')
    if user_input == 'exit':
        break
    list_1.append(user_input)
print('Дo:')
print(list_1)

for el in range(len(list_1) if ((len(list_1) % 2) == 0) else len(list_1)-1):
    if (el % 2) == 0:
        list_1[el], list_1[el+1] = list_1[el+1], list_1[el]
print('Пocле:')
print(list_1)


