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
#     def __init__(self, wage, bonus, name, surname, position):
#         self._income = {'wage': wage, 'bonus': bonus}
#         self.wage = wage
#         self.bonus = bonus
#         self.name = name
#         self.surname = surname
#         self.position = position
#
#
# class Position(Worker):
#
#     def __init__(self, wage, bonus, name, surname, position):
#         super().__init__(wage, bonus, name, surname, position)
#
#     def get_full_name(self):
#         return f' Фамилия: {self.surname} Имя: {self.name}'
#
#     def get_total_income(self):
#         self.get_total = int(self.wage) + int(self.bonus)
#         return f'Доход с учетом премии: {self.get_total}'
#
#
# wor = Position(250, 30, 'NIK', 'Nes', 'md')
# print(wor.get_full_name())
# print(wor.get_total_income())
