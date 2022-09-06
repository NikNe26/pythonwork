# #HW 2.1.
#
# li = [-7, 21.8, False, 'hi', {"name":"Nick"} ]
# for el in li:
#     print(type(el))
#
# #HW 2.2.
#
# a = input('Введите свой список:').split()
# for i in range(0, len(a)-1, 2):
#        a[i], a[i+1] = a[i+1], a[i]
# print(a)
# HW 2.3.
#
# a = int(input('Введите номер месяца: '))
# win = [12, 1, 2]
# spr = [3, 4, 5]
# summ = [6, 7, 8]
# aut = [9, 10, 11]
# if a in win:
#     print('зима')
# if a in spr:
#     print('весна')
# if a in summ:
#     print('лето')
# if a in aut:
#     print('осень')
#
# season = {'зима': [12, 1, 2], 'весна': [3, 4, 5], 'лето': [6, 7, 8], 'осень': [9, 10, 11]}
# a = int(input('Введите номер месяца: '))
# for el in season:
#     if a in season[el]:
#         print(el)
#         break
#
# HW 2.4.
#
a = input('Введите свой список:').split()
for el,u in enumerate(b, 1):
    if len(u) <10:
        print(el, u)
    else:
        print(el, u[0:10])
