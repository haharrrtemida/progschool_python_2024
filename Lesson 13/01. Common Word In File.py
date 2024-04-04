'''
Необходимо реализовать функцию, которая принимает в себя путь к файлу и
возвращает слово из файла, встречающееся чаще всего
'''

def get_most_common_word(file_path : str):
    with open(file_path, 'rb') as file:
        file_text = file.read()

    SYMBOLS = "!@#$%^~&*()-_=+:;\'\"|/?,.><№—"
    table = {}

    # удаляем из текста все символы, при необходимости добавляем символы в список "symbol"
    for symbol in SYMBOLS:
        file_text = file_text.replace(symbol, "")

    # понижаем регистр и разбиваем текст на слова
    words_list = file_text.lower().split()

    # заполняем словарь "table" и записываем значение (переберая лист "word_list", прибавляем value +1)
    for word in words_list:
        table[word] = table.get(word, 0) + 1

    # сортируем полученные значения по убыванию и возрващаем первое слово
    sorted_data_by_often = sorted(table.items(), key = lambda word: word[1], reverse = True)
    common_word_pair = sorted_data_by_often[0]
    word = common_word_pair[0]
    return word

path = input("Type file path: ")
common_word = get_most_common_word(path)
print(common_word)