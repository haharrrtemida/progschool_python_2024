string_1 = "qwerty"
string_2 = string_1

print(id(string_1))
print(id(string_2))

del string_1

print(id(string_2))