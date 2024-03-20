# По данному числу n определите n-е число Фибоначчи.

n = int(input("Введите число: "))
count = 0
f = 1
f_old = 0
if n > 0:
    while n > count:
        count += 1
        sum = f + f_old
        f_old = f
        f = sum
    print(f_old)

else:
    print("Вы ввели не правильное значение!")