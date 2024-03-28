# Кайгородов И.С.
""""
Задание 2. Банковский вклад
Один банк сделал у Вас заказ: реализовать калькулятор для вкладов.
Пользователь вводит сумму вклада в размере n рублей сроком на years лет под 10% годовых.
Написать функцию calculate(), принимающую аргументы n и years и возвращающую сумму, которая будет на счету пользователя через years лет.
"""
# функция возвращает итоговую сумму вклада
def calculate(n : float, years):
    i = 1
    while i < years:
        n *= 1.1
        i += 1
    return round(n, 2)

# записываем в переменные сумму вклада и количество лет
n = float(input("Желаемая сумма вклада: "))
years = int(input("На сколько лет? "))

# проверка на отрицательные значения
if n < 0 or years < 1:
    print("Некорректное значение")

# Обращение в функции и вывод
else:
    result = calculate(n, years)
    print(f"Итого: {result} ")