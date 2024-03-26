text = "Мама мыла раму"

text_list = list(text)
text_set = set(text)    # или {1, 2, 3}
print(text_list)
print(text_set)

# так делать нельзя (ошибка TypeError)
# print(text_set[2])

# если создать set через {}, то получится
# не set, а dict
test = {}
print(type(test))
