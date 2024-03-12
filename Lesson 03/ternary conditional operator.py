number = int(input("Number: "))
if number % 2 == 0:
    print("Чётное")
else:
    print("Нечётное")


# тернарный оператор
# что_вернуть_если_истина if условие else что_вернуть_если_ложь
print("Чётное" if number % 2 == 0 else "Нечётное")