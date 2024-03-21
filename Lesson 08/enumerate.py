borsh = ['вода', 'свекла', "мясо", "картошка", "капуста", "лук", "специи", "морковь"]

# аналог foreach (перебираем элементы из коллекции)
i = 1
for ingredient in borsh:
    print(f"{i}. {ingredient}")
    i += 1

print()
# количественный цикл, элементы получаем по индесу i
for i in range(len(borsh)):
    print(f"{i + 1}. {borsh[i]}")

print()
for i, ingredient in enumerate(borsh, start = 1):
    print(f"{i}. {ingredient}")