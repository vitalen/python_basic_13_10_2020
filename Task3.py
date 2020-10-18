"""
Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень). Напишите решения через list и через dict.
"""
winter = [12, 1, 2]
spring = [3, 4, 5]
summer = [6, 7, 8]
fall = [9, 10, 11]
year = [winter, spring, summer, fall]
while True:
    user_input = input('введите месяц в виде целого числа от 1 до 12?')
    if user_input.isdigit() and int(user_input) > 0 and int(user_input) < 13:
        user_input = int(user_input)
        break

print('\n'*2)
print('#'*40)
print('решения через через list')
year = ['зима', 'зима', 'весна', 'весна', 'весна', 'лето', 'лето', 'лето', 'осень', 'осень', 'осень', 'зима']
print(f'месяц относится к времени года: {year[user_input-1]}')

print('\n'*2)
print('#'*40)
print('решения через через dict')
winter = (12, 1, 2)
spring = (3, 4, 5)
summer = (6, 7, 8)
fall = (9, 10, 11)
year = {'зима': winter, 'весна': spring, 'лето': summer, 'осень': fall}
for key, value in year.items():
    if user_input in value:
        print(f'месяц относится к времени года: {key}')
        break