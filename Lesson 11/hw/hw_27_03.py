# Задание 1. Сумматор
# Напишите функцию sum_range(start, end), которая суммирует все целые числа от
# значения start включительно до величины end включительно. Если пользователь
# задаст первое число большее чем второе, просто поменяйте их местами.

print("-" * 8 + "\nЗадание 1")

def sum_range(start: int, end: int):
    if start > end:
        start, end = end, start
    result = 0
    for n in range(start, end + 1):
        result += n
    return result

first_num = int(input("Укажите первое число: "))
second_num = int(input("Укажите второе число: "))

print(f"Сумма всех чисел диапазона: {sum_range(first_num, second_num)}")

# Задание 2. Банковский вклад
# Один банк сделал у Вас заказ: реализовать калькулятор для вкладов. 
# Пользователь вводит сумму вклада в размере n рублей сроком на years лет
# под 10% годовых. Написать функцию calculate(), принимающую аргументы n и years
# и возвращающую сумму, которая будет на счету пользователя через years лет.

print("-" * 8 + "\nЗадание 2")

MULTIPLIER = 1.1

def calculate(n: int, years: int):
    for y in range(years):
        n *= MULTIPLIER
    return n

n = int(input("Укажите первоначальный взнос: "))
years = int(input("Укажите продолжительность вклада в годах: "))

print(f"Ваш доход составит: {int(calculate(n, years))}")