"""
Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""
with open("file_2.txt", "r") as my_file:
    for idx, value in enumerate(my_file):
        tmp_list = value.split()
        print(f'строкa: {idx}, количества слов в строке: {len(tmp_list)}')
    print(f'количествo строк: {idx}')

