print("Вас приветствует простой калькулятор.\n Он может выполнять простые 4 арифметические действия с целыми и дробными числами.")

try:
    a = float(input("Введите 1 число:"))
    znak= input("Введите арифметическую операцию:")
    b = float(input("Введите 2 число:"))
except ValueError:
    print("Неверный формат чисел!")

if znak != "+" and znak != "-" and znak != "*" and znak != "/":
    raise ValueError("Вы ввели операцию,  которую не поддерживает данный калькулятор.")
else:
    result = 0
    if znak == "+":
        result = a + b
    elif znak == "-":
        result = a - b
    elif znak == "*":
        result = a * b
    elif znak == "/":
        if b == 0:
            raise Exception("Ошибка: кривой код")
        else:
            result = a / b

    print(f"Результат {a} {znak} {b} = {result}")