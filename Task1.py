"""
Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""
try:
    my_file = open("file_1.txt", "w")
    while True:
        user_input = input('данные пользователем: ')
        if len(user_input) > 0:
            my_file.write(user_input + '\n')
        else:
            break
except IOError:
    print('Error')
finally:
    my_file.close()