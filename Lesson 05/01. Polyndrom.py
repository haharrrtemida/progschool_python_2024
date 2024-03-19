'''
Пользователь вводит некую строку с клавиатуры. Необходимо
написать программу, которая напишет, является ли введённое
слово палиндромом.
'''
text = input("Напишите текст: ")
text_without_spaces = text.replace(' ', '')

output = """Фраза "{}" {}является палиндромом."""

if text_without_spaces.lower() == text_without_spaces[::-1].lower():
    output = output.format(text, "")
else:
    output = output.format(text, "не ")

print(output)