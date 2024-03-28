"""
Представим, что мы пишем логику для робота-официанта,
который должен принять заказ у клиентов и обязательно повторить все позиции, пронумеровав их.
Пользователь вводит блюда, подтверждая каждое нажатием клавиши Enter.
Чтобы завершить ввод блюд, пользователь вводит 0.
После завершения заказа, официант повторяет весь заказ,
нумеруя каждую позицию в заказе, в том порядке, как их вводил пользователь.
"""
order = list()
i = 0

print("Здравствуйте,что вы будете заказывать? ")

result = ""
while not result == "0":
    dish = input()
    if dish == "0":
        break
    order.append(dish)

print("Ваш заказ: ")
for i, dish in enumerate(order, start = 1):
    print(f"{i}. {dish}")