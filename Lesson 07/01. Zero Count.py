"""
Дано N чисел: сначала вводится число N,
затем вводится ровно N целых чисел.
Подсчитайте количество нулей среди введенных
чисел и выведите это количество.
Вам нужно подсчитать количество чисел,
равных нулю, а не количество цифр.
"""

n = int(input("Укажите сколько будет вводиться чисел: "))

null_count = 0
for _ in range(n):
    a = int(input("Введите число: "))
    if a == 0:
        null_count += 1

print(f"Количество чисел равных нулю: {null_count}/{n}")