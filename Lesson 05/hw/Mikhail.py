string = input('Введите строку: ')

half_len = int((len(string) + 1) // 2 )

ing_str = string[half_len:] + string[:half_len]

print(f'Результат разрезания на части: {ing_str}')