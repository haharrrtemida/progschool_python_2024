# инициализация
eng_rus_dict = dict()
eng_rus_dict = {}

# словарь состоит из пар ключ : значение
eng_rus_dict = {
    "dog" : "собака",
    "home": "дом",
    "tree": "дерево",
    2 : "два",
    True : True
}

# задать значение имеющегося ключа
eng_rus_dict[True] = "правда"
# добавить новую пару по неимеющемуся ключу
eng_rus_dict["Python"] = "питон"


# поиск не по индексу, а по ключу
# если ключа нет, то KeyError
print(eng_rus_dict["Python"])


# создаст словарь по ключам из keys и всем даст значение value
keys = ["admin", "user", "c00lguy"]
value = "p@ssw0rd"

a = eng_rus_dict.fromkeys(keys, value)
print(a)

# get возвращает:
#   * значение ключа (если есть)
#   * None (если ключа нет)
result = eng_rus_dict.get("Math", "Такого элемента не нашлось")
if result is None:
    print("Ошибочка вышла")
print(result)


# получаем все пары из словаря (dict_items)
print(eng_rus_dict.items())

# получить ключи из словаря (dict_keys)
keys = list(eng_rus_dict.keys())
print(keys)

# получить значения из словаря (dict_values)
values = list(eng_rus_dict.values())
print(values)

# добавить пары в словарь
eng_rus_dict.update([("capital", "столица"), ("city", "город")])
print(eng_rus_dict)