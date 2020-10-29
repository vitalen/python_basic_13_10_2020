"""
Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""
try:
    with open(r"file_3.txt", "r") as my_file:
        sum_salary = 0
        for idx, value in enumerate(my_file):
            tmp_name = value.split()[0]
            tmp_salary = float(value.split()[1])
            sum_salary += tmp_salary
            if tmp_salary < 20000:
                print(f'фамилия сотрудникa: {tmp_name}, ({tmp_salary})')
        print(f'средняя величинa дохода сотрудников: {float(sum_salary/idx):.2f}')
except IOError:
    print('IOError')
except ZeroDivisionError:
    print('ZeroDivisionError')
except ValueError:
    print('ValueError')
