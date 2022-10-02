# # HW 7.1
# class Matrix:
#
#     def __init__(self, list_list):
#         self.list_list = list_list
#
#     def __str__(self):
#         for row in self.list_list:
#             for i_num in row:
#                 print(f'{i_num} |', end='')
#             print('\n----------')
#         return ''
#
#     def __add__(self, other):
#         for first_list in range(len(self.list_list)):
#             for sec_list in range(len(other.list_list[first_list])):
#                 self.list_list[first_list][sec_list] = \
#                     self.list_list[first_list][sec_list] + \
#                     other.list_list[first_list][sec_list]
#         return Matrix.__str__(self)
#
#
# first = Matrix([[-1, 0, 1], [-1, 0, 1], [0, 1, -1], [1, 1, -1]])
# sec = Matrix([[-2, 0, 2], [-2, 0, 2], [0, 2, -2], [2, 2, -7]])
#
# # print(first)
# # print(sec)
#
# print(first.__add__(sec))

# HW 7.2

# class Clothes():
#
#     def __init__(self, param):
#         self.param = param
#
# class Coat(Clothes):
#     def __init__(self, param):
#         super().__init__(param)
#
#     def consumption(self):
#         self.fabric = self.param / 6.5 + 0.5
#         return f'Для пошива пальто нужно: {self.fabric:.2f} ткани'
#
#
# class Costume(Clothes):
#     def __init__(self, param):
#         super().__init__(param)
#
#     def consumption(self):
#         self.fabric = 2 * self.param + 0.3
#         return f'Для пошива костюма нужно: {self.fabric:.2f} ткани'
#
#
# coat = Coat(250)
# costume = Costume(150)
# print(costume.consumption())
# print(coat.consumption())
# print(f"сумма затраченной ткани = {round(costume.fabric + coat.fabric, 2)} м.")

# HW 7.3

# HW 7.3
# class Cell:
#
#     def __init__(self, quantity):
#         self.quantity = quantity
#
#     def __add__(self, other):
#         return f'Объединение двух клеток, размер новой клетки после суммирования - {self.quantity + other.quantity}'
#
#     def __sub__(self, other):
#         subb = self.quantity - other.quantity
#         if subb <= 0:
#             return 'клетка  мала'
#         else:
#             return f'Новый размер клетки после вычитания - {subb} '
#
#     def __truediv__(self, other):
#         return f'Новый размер клетки после деления -  {self.quantity // other.quantity}'
#
#     def __mul__(self, other):
#         return f'Новый размер клетки после умножения - {self.quantity * other.quantity}'
#
#     def make_order(self, row):
#         result = ''
#         for i in range(int(self.quantity / row)):
#            result += '*' * row + '\n'
#         result += '*' * (self.quantity % row)
#         return result
#
# cell = Cell(22)
# cell_2 = Cell(2)
# print(cell + cell_2)
# print(cell - cell_2)
# print(cell / cell_2)
# print(cell * cell_2)
# print(cell.make_order(10))