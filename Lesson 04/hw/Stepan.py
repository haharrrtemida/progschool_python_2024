# Домашнее задание №3.
# Некий бизнесмен продаёт апельсины бочками.
# Напишите программу, которая выбирает правильное слово (из "бочка" , "бочек" , "бочки" ) в зависимости от их количества.

for i in range (1,100):
    barrel = int(i)
    if barrel%100//10 == 1 or barrel%10 not in [1,2,3,4]: 
        name = 'бочек'
    elif barrel%10 == 1:
        name = 'бочка'
    else:
        name = 'бочки'
    print(barrel,name)