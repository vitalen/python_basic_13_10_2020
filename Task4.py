"""
Создать (не программно) текстовый файл со следующим содержимым:

One — 1

Two — 2

Three — 3

Four — 4

Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.
"""


def write_to_file(a):
    try:
        with open("file_4_output.txt", "a") as output_file:
            output_file.write(a)
    except IOError:
        print('IOError')


my_dict = {'One': 'один', 'Two': 'два', 'Three': 'три', 'Four': 'четыре'}

try:
    with open("file_4.txt", "r") as my_file:
        for line in my_file:
            if not ''.join(line).strip():
                pass
            else:
                tmp_value = line.split()[0]
                write_to_file(line.replace(line.split()[0],my_dict[tmp_value]))
                print(f'{line.replace(line.split()[0],my_dict[tmp_value])}')
except IOError:
    print('IOError')

