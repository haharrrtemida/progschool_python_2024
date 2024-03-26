"""
Создайте список с именами, после чего напишите программу,
которая считывает с клавиатуры имя пользователя и определяет,есть ли он в списке.
"""

count = int(input("Сколько будет человек в списке? "))

if not count > 0:
    print("Не верное значение")
else:
    base_name = list()
    for i in range(count):
        i += 1
        name = input("Введите имя: ")
        base_name.append(name)

    print("Найти имя в списке")
    name_who = input("Кто вас интересует: ")

    if name_who in base_name:
        print("Данное имя есть в списке")
    else:
        print("Такого имени нет")