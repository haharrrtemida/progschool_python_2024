
boch = int(input("Сколько бочек вы хотели бы приобрести:"))
if boch == 0:
    print("Неверно введено количество бочек")

elif boch == 10:
    print(f"Вам необходимо {boch} бочек апельсин")

else:
    col_boch = boch % 100

    if col_boch == 1:
        print (f"Вам необходима {col_boch} бочка апельсин")
    elif 2 <= col_boch and col_boch < 5:
        print (f"Вам необходимо {col_boch} бочки апельсин")
    elif 5 <= col_boch < 9 and col_boch == 0:
        print(f"Вам необходимо {col_boch} бочек апельсин")