number = int(input("введите количество апельсинов: "))
if 10 < number % 100 < 15:
    print("бочек")
elif number % 10 == 1:
    print("бочка")
elif 2 <= number % 10 <= 4:
    print("бочки")
else:
    print("бочек")