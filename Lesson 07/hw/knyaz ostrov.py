# Домашнее Задание 6. Цикл while

from math import ceil
from time import sleep

def num_input_request(req_txt=''):
    while True:
        num = input(req_txt)
        if num.isdigit() == True: return int(num)
        else: print("Повторите ввод.")


# 1. В первый день спортсмен пробежал x километров,
# а затем он каждый день увеличивал пробег на 10% от предыдущего значения.
# По данному числу y определите номер дня, на который пробег спортсмена составит не менее y километров.

print("--------\nЗадача 1.")

x = num_input_request("Сколько километров пробежал спортсмен в первый день? ---> ")
y = num_input_request("Укажите пробег, чтобы узнать, на какой день спортсмен смог его достигнуть: ")

record_distance, day = x, 1
while record_distance < y:
    day += 1
    record_distance *= 1.1

print(f"На {day} день спортсмен смог совершить пробег в {y} км.")

###

# 2. По данному числу n определите n-е число Фибоначчи.

print("--------\nЗадача 2.")

n = num_input_request("Введите порядковый номер числа Фибоначчи: ")

if 0 <= n <= 1:
    fibo_num = 0
else:
    a, b = 0, 1
    counter = 2
    while counter < n:
        counter += 1
        a, b = b, a + b
    fibo_num = b

print(f"Числом Фибоначчи под порядковым номером {n} является {fibo_num}.")

sleep(1)

###

# 3*. Англоязычная школа сделала Вам Ваш первый заказ: необходимо составить таблицу с заглавными и строчными буквами русского алфавита в красивом формате.
# Результат работы программы продемонстрирован на скриншоте. Сможете ли Вы повторить следующую конструкцию?

print("--------\nЗадача 3.")

line_sep = '^' * 27                                                         # Разделяющая линия из галочек
pattern = '|  {} {}  |'                                                     # Шаблон вывода каждой буквы

literals_list = [chr(i) for i in range(ord('а'), ord('я') + 1)]             # Создаем список со всем алфавитом
literals_list.insert(6, 'ё')                                                # Добавляем недостающую букву "ё"

cols = 11                                                                    # Количество столбцов, которое будет у нас в таблице
lines = ceil(len(literals_list) // cols)                                     # Вычисляем количество строк, которое зависит от количества букв и столбцов

steps = [lines * s for s in range(0, cols)]                                 # Логика вывода букв слева-направо
groups = ['' for i in range(lines)]                                         # Создаем список, каждый объект в котором будет отдельной строкой в таблице

n = 0
for line_num, line in enumerate(groups):                                    # Цикл для заполнения каждого объекта в groups нужными нам строками
    for i in steps:
        if n + i >= len(literals_list):
            break
        groups[line_num] += pattern.format(literals_list[n + i].upper(), literals_list[n + i])
    n += 1

result = f'{line_sep}\n' + f'\n{line_sep}\n'.join(groups) + f'\n{line_sep}' # Добавляем дополнительные разделяющие линии снизу и сверху таблицы
print(result)