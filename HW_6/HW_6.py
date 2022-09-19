# HW_6.1.
# import time
# class TraficLight:
#     __color_ = 'красный', 'желтый', 'зеленый'
#     def running(self, color):
#         self.__color_ = color
#         if color == 'красный':
#             print('красный')
#             time.sleep(7)
#             print('желтый')
#             time.sleep(2)
#             print('зеленый')
#             time.sleep(10)
#         else:
#             print(' Начало с красного цвета')
#
# Tran = TraficLight()
# Tran.running(input('Введите цвет светофора: '))

# HW_6.2.

# class Road:
#
#     def __init__(self, lenght, width):
#         self._lenght_ = lenght
#         self._width_ = width
#         self.mas = int(lenght) * int(width) * 25 * 5
#     def get_info(self):
#         return f'Масса асфальта необходимая для покрытия дороги: {self.mas}'
#
# mas_as = Road(200, 35)
# print(mas_as.get_info())

# HW_6.3.

# HW_6.3.

# class Worker:
#     def __init__(self, wage, bonus):
#         self._income_ = {'wage': wage, 'bonus': bonus}
#
# class Position(Worker):
#
#     def get_full_name(self, name, surname):
#         print(f' Фамилия: {surname} Имя: {name}')
#
#     def get_total_income(self, wage, bonus):
#         super().__init__(wage, bonus)
#         self.get_total = int(wage) + int(bonus)
#         print(f'Доход с учетом премии: {self.get_total_income}')
#
# wor = Position()
# print(wor.get_total_income(250, 30))
