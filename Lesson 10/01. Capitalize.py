"""
Напишите функцию capitalize(), которая принимает строку из нескольких
слов из маленьких латинских букв и возвращает её же, меняя первую
букву каждого слова на большую.
"""

def capitalize(text):
    text = text.split()
    for i in range(len(text)):
        text[i] = text[i][0].upper() + text[i][1:]
    result = " ".join(text)
    return result


word = input("Ваше слово: ")

new_word = capitalize(word)
print(new_word)