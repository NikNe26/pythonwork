# HW_4.2

# Li = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# Li2 = [Li[i] for i in range(1, len(Li)) if Li[i] > Li[i-1]]
# print(Li2)

# HW_4.3

# Li = [i for i in range(20, 241) if i % 20 == 0 or i % 21 == 0]
# print(Li)

# HW_4.4

# Li = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# Li2 = [el for el in list(Li) if Li.count(el) ==1]
# print(Li2)

# HW_4.5

# from functools import reduce
# Li = [i for i in range(100, 1001) if i % 2 == 0]
# pov = reduce(lambda x, y: x * y, Li)
# print(pov)
