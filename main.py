# HW 3.1.

# def my_func(num1, num2):
#     if num2 != 0:
#         return print(num1 / num2)
#     else:
#         print('Ошибка на ноль делить нельзя!')
# number1 = int(input('Введите первое число: '))
# number2 = int(input('Введите первое число: '))
# my_func(number1, number2)

# HW 3.2.

# def my_spr(name, surname, age, city, email, mobi):
#     print(f'Имя: {name} Фамилия: {surname} Год рождения: {age} Город проживания: {city} Email:{email} Телефон: {mobi}')
#
# n = input('Имя: ')
# s = input('Фамилия: ')
# a = input('Год рождения: ')
# c = input('Город проживания: ')
# e = input('Email: ')
# m = input('Телефон: ')
#
# my_spr(n, s, a, c, e, m)

# HW 3.3.

# def my_func(a, b, c):
#     if a >= c and b >= c:
#         print(a + b)
#     elif a >= b and c >= b:
#         print(a + c)
#     else:
#         print(b + c)
# my_func(int(input()), int(input()), int(input()))

# HW 3.4.

# def my_func(x, y):
#     print(x ** y)
#
# n = float(input('X: '))
# s = int(input('Y: '))
# my_func(n, s)

# def my_func(x, y):
#     a = x
#     for i in range(abs(y)-1):
#         a *= x
#     print(1 / a)
#
# n = float(input('X: '))
# s = int(input('Y: '))
# my_func(n, s)

# HW 3.5.
# def my_func(num_text):
#     global num_sum
#     for i_num in num_text.split():
#         if i_num.isdigit():
#             num_sum += int(i_num)
#         elif i_num in ( '+', '-', '!', '*', '/', '@'):
#             global flag
#             flag = False
#             break
#     return num_sum
#
#
# while True:
#     if flag:
#         num_str = input( 'Введите числа: ')
#         print(my_func(num_str))
#     else:
#         break

# HW 3.6.

# def int_func(my_str):
#     return my_str.capitalize()
#
# text = input('Введите слова: ')
# print(int_func(text))

# HW 3.7.

# def int_func(my_str):
#     my_list = []
#     for el in my_str.split():
#         my_list.append(el.capitalize())
#     result = ' '.join(my_list)
#     return result
#
# text = input('Введите слова: ')
# print(int_func(text))
