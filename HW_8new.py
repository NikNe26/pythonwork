# HW 8_1.
# class Date:
#     def __init__(self, day=0, month=0, year=0):
#         self.day = day
#         self.month = month
#         self.year = year
#
#     def __str__(self):
#         return "День: {}\tМесяц: {}\t Год: {}".format(self.day, self.month, self.year)
#
#     @staticmethod
#     def is_date_valid(date):
#         day, month, year = map(int, date.split('-'))
#         return 0 < day <= 31 and 0 < month <= 12 and 0 < year <= 9999
#
#     @classmethod
#     def from_string(cls, date):
#         day, month, year = map(int, date.split('-'))
#         date_obj = cls(day, month, year)
#         return date_obj
#
# date = Date.from_string('10-12-2077')
# print(date)
# print(Date.is_date_valid('10-12-2077'))
# print(Date.is_date_valid('40-12-2077'))

# HW 8_2.
# class ZeroNumber(Exception):
#     pass
#
# n = int(input('ВВедите целое число: '))
# m = int(input('ВВедите целое число: '))
# if m == 0:
#     print('Деление на ноль')
# else:
#     print('Все нормально:', float(n / m))

# HW 8_3.
# class NotNumber(Exception):
#     pass
#
# answer = ''
# num_list = []
# nums = '0987654321'
# flag = True
# while flag:
#     answer = input('Введите символ ')
#     try:
#         if answer == 'stop':
#             flag = False
#         elif answer not in nums:
#             raise NotNumber
#         else:
#             num_list.append(answer)
#     except NotNumber:
#         print('Not a number')
#
# print(num_list)

# HW 8_4.5.6.
# class Equipment:
#     def __init__(self, name, make, year):
#         self.name = name
#         self.make = make
#         self.year = year
#     def action(self):
#         return 'Не определено'
#     def __str__(self):
#         return f'{self.name} {self.make} {self.year}'
#
# class Printer(Equipment):
#     def __init__(self, series, name, make, year):
#         super().__init__(name, make, year)
#         self.series = series
#     def __str__(self):
#         return f'{self.name} {self.series} {self.make} {self.year}'
#     def action(self):
#         return 'Печатает'
#
# class Scaner(Equipment):
#     def __init__(self, name, make, year):
#         super().__init__(name, make, year)
#         def action(self):
#             return 'Сканирует'
#
# class Xerox(Equipment):
#     def __init__(self, name, make, year):
#         super().__init__(name, make, year)
#     def action(self):
#         return 'Копирует'
#
# sklad = []
# scaner = Scaner('Mustek','BearPow 1200CU', 2010)
# sklad.append(scaner)
# xerox = Xerox('Xerox','Phaser 3120', 2019)
# sklad.append(xerox)
# printer = Printer("1200",'hp', 'Laser Jet', 2018)
# sklad.append(printer)
# print("На складе имеются:")
# for x in sklad:
#     print(x,end=' ')
#     print(x.action())
# for x in sklad:
#     if isinstance(x,Printer):
#         sklad.remove(x)
#
# print("\nНа складе осталось:")
# for x in sklad:
#     print(x,end=' ')
#     print(x.action())