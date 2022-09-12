from sys import argv      # я не совсем понял как надо реализовать это правильно, поэтому два варианта сделал
# 1 вариант
# vyr, sta, pre = map(int, argv[1:])
# ZP = (vyr * sta) + pre
# print('Зароботная плата:',ZP)
# 2 вариант
vyr = int(input('Выработка в часах: '))
sta = int(input('Ставка в часах: '))
pre = int(input('Премия: '))
ZP = (vyr * sta) + pre
print('Зароботная плата:',ZP)