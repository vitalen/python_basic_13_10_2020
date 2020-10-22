"""
Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
"""
def getUserInfo(fistname, lastname, birthday, city, email, fon):
    print(f'имя - {fistname}; фамилия - {lastname}; год рождения - {birthday}; город проживания - {city}; email - {email}; телефон - {fon}')


input_fisrtname = input('имя: ')
input_lastname = input('фамилия: ')
input_birthday = input('год рождения: ')
input_city = input('город проживания: ')
input_email = input('email: ')
input_fon = input('телефон: ')
getUserInfo(birthday=input_birthday, city=input_city, fistname=input_fisrtname, lastname=input_lastname,  email=input_email, fon=input_fon)
