"""
Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и
возвращающую его же, но с прописной первой буквой.
Например, print(int_func(‘text’)) -> Text.
Продолжить работу над заданием. В программу должна попадать строка из слов,
разделенных пробелом. Каждое слово состоит из латинских букв в нижнем регистре.
Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
Необходимо использовать написанную ранее функцию int_func().
"""


def int_func(input_str):
    if input_str.istitle():
        return input_str
    else:
        return input_str.title()


try:
    user_input = input('введите строкy из слов, разделенных пробелом: ').split()
    idx = 0
    tmp_result = ''
    while idx < len(user_input):
        print(f'{int_func(user_input[idx])}')
        tmp_result += int_func(user_input[idx]) + ' '
        idx += 1
    print('или тak ')
    print(tmp_result)

except ValueError:
    print('Error')