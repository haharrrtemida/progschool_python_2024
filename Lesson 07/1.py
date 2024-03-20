pattern = '|  {} {}  |'
line_sep = '^' * 27

rus_lower = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

cols = 3
lines = len(rus_lower) // cols


i = 0
while i < lines:
    print(line_sep)
    string = pattern * cols
    print(string.format(
        rus_lower[i].upper(), rus_lower[i].lower(),
        rus_lower[i + lines].upper(), rus_lower[i + lines].lower(),
        rus_lower[i + lines*2].upper(), rus_lower[i + lines * 2].lower()
        )
    )
    i += 1
print(line_sep)