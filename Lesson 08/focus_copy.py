first = [1, 2, 3, 4, 5]
choose = input("Ссылка/Копия: ")
if choose == "ссылка".lower():
    second = first              # присваивает ссылку
else:
    second = first.copy()       # копирует элементы списка
first.remove(2)
second.append(9)

print(f"first: {first}")
print(f"second: {second}")