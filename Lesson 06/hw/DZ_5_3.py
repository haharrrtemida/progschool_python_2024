print("Программа для проверки слов на анаграммы.")
Str1 = input("Введите первое слово для сравнения: ")
Str2 = input("Введите второе слово для сравнения: ")
Rez1 = sorted(Str1.lower())
Rez2 = sorted(Str2.lower())
if Rez1 == Rez2:
    print(f"Слова {Str1}  и  {Str2} явлюятся анограммами")
else:
    print(f"Слова {Str1}  и  {Str2}  не явлюятся анограммами")
