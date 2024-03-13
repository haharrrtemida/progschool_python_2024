# Домашнее задание №3.
# Некий бизнесмен продаёт апельсины бочками.
# Напишите программу, которая выбирает правильное слово (из "бочка" , "бочек" , "бочки" ) в зависимости от их количества.

import random


num_tpl = ()

while True:
    user_input = input("""Напишите "Рандом" или "Random", чтобы сгенерировать 10 случайных чисел или укажите своё число\n---> """)
    try:
        num_tpl = (int(user_input), )
        print(f"Вы ввели число {user_input}.")
        break
    except ValueError:
        if user_input.lower() in ('рандом', 'random'):
            num_tpl = (random.randint(0, 1000) for i in range(0, 10))
            print("Вы выбрали генерацию чисел.")
            break
        else:
            print("Неккоректный вод, повторите действие.")
            continue

word_form = ""

for num in num_tpl:
    if str(num)[-2:] in ('11', '12', '13', '14'):
        word_form = "бочек"
    else:
        match num % 10:
            case 1: word_form = "бочка"
            case 2 | 3 | 4: word_form = "бочки"
            case _: word_form = "бочек"

    print(f"У вас {num} {word_form}.")