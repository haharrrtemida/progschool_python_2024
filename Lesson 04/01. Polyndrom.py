# Пользователь вводит некое слово с клавиатуры. Необходимо написать программу, которая напишет,
# является ли введённое слово палиндромом.

str = input("введи слово... ")
rts = str[::-1]

if str == rts:
    print("True")
else:
    print("False")