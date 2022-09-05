#HW 2.1.

li = [-7, 21.8, False, 'hi', {"name":"Nick"} ]
for el in li:
    print(type(el))

#HW 2.2.

a = input('Введите свой список:').split()
for i in range(0, len(a)-1, 2):
       a[i], a[i+1] = a[i+1], a[i]
print(a)
