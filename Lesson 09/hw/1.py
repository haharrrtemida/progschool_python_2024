order = '\nВаш заказ:'
i = 1
while True:
    dish = input("Наименование: ")
    if dish == '0':
        print(order)
        break
    else:
        order += f'\n{i}. {dish}'
        i += 1