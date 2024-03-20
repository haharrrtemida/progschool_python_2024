print("Программа рассчитывает за сколько дней спортсмен пробежит указанную дистанцию")
x = int(input("Введите колчиство км., которое пробежал спортсмен в первый день: "))
y = int(input("Введите колчиство км. для целевого расчёта: "))
numbers_of_days = int(1)
result = x
probeg = x + x/10 
 
# начало цикла           
while result <= y:
    # обработка окончания слова день
    if numbers_of_days == 1 or numbers_of_days == 21 or numbers_of_days == 31:
        ending_in_a_word = "день"
    elif numbers_of_days == 2 or numbers_of_days == 3 or numbers_of_days == 4 or numbers_of_days == 22 or numbers_of_days == 23 or numbers_of_days == 24:
        ending_in_a_word = "дня"
    else:
        ending_in_a_word = "дней" 
    print(f"За {numbers_of_days} {ending_in_a_word} пробежал {result} км.") # промежуточный результат
    numbers_of_days += 1
    result = probeg
    probeg *= 1.1
print(f"Для переодоления расстояния в {y} км. спортсмену потребовалось {numbers_of_days} {ending_in_a_word}.")    
