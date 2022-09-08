# HW 1.1.

number = int(input('Enter your number: '))
print(number // 5)

growth = float(input('Укажите ваш рост: '))
weight = float(input('Укажите ваш вес: '))
IMT = weight / growth *100
print('Индекс массы тела =', int(IMT))

pulse = int(input('Your pulse: '))
if pulse <= 90 and pulse >= 60:
    print("you ok")
else:
    print("see a doctor")

# HW 1.2.

time =int(input('Enter your seconds: '))
hour = time //3600
min = (time - hour*3600)//60
sec = time - (hour*3600)-(min*60)
print(f'{hour}:{min}:{sec}')

# HW 1.3.

n =int(input("Enter your number 0-9: "))
summa = n + n*11 + n*111
print(summa)

# HW 1.4.

n = int(input('Your number: '))
maxi = 0
while n > 0:
    last = n % 10
    if last >= maxi:
        maxi = last
    n //= 10
print(maxi)

# HW 1.5.

rev = int(input('Ваша выручка: '))
cos = int(input('Ваши издержки: '))
if rev > cos:
    print("прибыль")
if cos > rev:
    print("убыток")

# HW 1.6.

rev = int(input('Ваша выручка: '))
cos = int(input('Ваши издержки: '))
if rev > cos:
    prof = (rev - cos) / rev
    print("Рентабельность =", prof)
    people = int(input('Количество сотрудников: '))
    prof_on = (rev - cos) / people
    print("Прибыль на сотрудника  =", prof_on)
if cos > rev:
    print("убыток")

#HW 1.7.-

a = float(input('первичный результат: '))
b = float(input('желанный результат: '))
days = 0
while True:
    a = a + (a * 0.1)
    if a >= b:
        days += 1
        print(days)
        break
    if a < b:
        days += 1