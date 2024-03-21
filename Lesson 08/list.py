# список (list)
name = "Artyom"

empty_list = list()
list_2 = [1, 2, 3, 4, 5]
list_1 = list(name)


# добавление элемента
list_2.append(0)        # добавить в конец списка
list_2.insert(0, 9)     # добавить в 0 позицию
list_2.insert(110, 1)   # добавить в конец списка
list_2.insert(-1, 66)   # добавить в -1 (предпоследнюю) позицию

# удаление элемента
list_2.remove(1)                # удалить первое вхождение элемента
deleted_item = list_2.pop(2)    # вытащить и вернуть объект по индексу
del list_2[5]                   # удалить элемент с индексом 5

# индекс
index = list_2.index(2)     # получение индекса элемента

if 66 in list_2:            # если элемент в списке
    print(True)

one_count = list_2.count(1) # возвращает количество вхождений элемента
list_2.reverse()            # развернуть задом наперёд список
list_2.sort()               # отсортировать элементы по возрастанию
list_2.clear()              # очистить список / удалить всё

print(list_1)
print(list_2)
print(deleted_item)
print(index)