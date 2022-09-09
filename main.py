
# def my_func(num1, num2):
#     if num2 != 0:
#         return print(num1 / num2)
#     else:
#         print('Ошибка на ноль делить нельзя!')
#
# number1 = int(input('Введите первое число: '))
# number2 = int(input('Введите первое число: '))
#
# my_func(number1, number2)

def my_spr(name, surname, age, city, email, mobi):
    print(f'Имя: {name} Фамилия: {surname} Год рождения: {age} Город проживания: {city} Email:{email} Телефон: {mobi}')

name = input('Имя: ')
surname = input('Фамилия: ')
age = input('Год рождения: ')
city = input('Город проживания: ')
email = input('Email: ')
mobi = input('Телефон: ')

my_spr()