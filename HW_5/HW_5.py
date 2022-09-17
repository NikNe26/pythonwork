#HW_5.1

# f = open(r'Hw_5.txt', 'a+', encoding='utf-8')
# a = input('Ваша строка: ')
# while a != ' ':
#     f.writelines([f'{a} \n'])
#     a = input('Ваша строка: ')
# else:
#     f.close()

#HW_5.2 Последнюю пустую строку почему-то не считает

#Для определения строк
# f = open(r'str.txt', 'r', encoding='utf-8')
# i = 0
# for line in f:
#     i += 1
# print(i)
# f.close()
#
# count = len(f.readlines())
# print(count)
# f.close()
#
# count = 0
# for count, line in enumerate(f):
#     pass
# count += 1
# print(count)
# f.close()

## Для определения слов в строке

# f = open(r'str.txt', 'r', encoding='utf-8')
# lines = f.readlines()
# for line in lines:
#     line = line.split()
#     print(len(line))
# f.close()

#HW_5.3

# with open(r'ZP.txt', 'r', encoding='utf-8') as f:
#     line = f.read().splitlines()
#     summ = []
#     for el in line:
#         el = el.split()
#         if float(el[1]) < 20000:
#             print('Менее 20000: ', el[0])
#         summ.append(el[1])
# print(f'Средний оклад: {sum(map(float, summ)) / len(summ)}')

#HW_5.4

# di = {'One':'Один', 'Two':'Два', 'Three':'Три', 'Four':'Четыре'}
# rus = []
# with open(r'One.txt', 'r', encoding='utf-8') as f:
#     # line = f.read().splitlines()
#     for el in f:
#         el = el.split(' ', 1)
#         rus.append(di[el[0]] + el[1])
#     print(rus)
# with open(r'One_new.txt', 'w', encoding='utf-8') as f_2:
#     f_2.writelines(rus)

#HW_5.5

# with open(r'number.txt', 'r', encoding='utf-8') as f:
#     line = f.readline().split()
#     print(f'Сумма чисел:{sum(map(int,line))}')