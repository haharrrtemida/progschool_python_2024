import random                                                               # подключаем модуль для генерации случайных чисел
import enum                                                                 # подключаем модуль для создания перечислений

class GameDifficulty(enum.IntEnum):                                         # создаём перечисление GameDifficulty
    EASY = 0                                                                # объявляем константу для обозначения уровня EASY
    MEDIUM = 1                                                              # объявляем константу для обозначения уровня MEDIUM
    HARD = 2                                                                # объявляем константу для обозначения уровня HARD

print("***Игра 'Угадай число'***")                                          # 
print("Выберите уровень сложности:")                                        # выводим надпись
print("0 - Лёгкий")                                                         # для выбора
print("1 - Средний")                                                        # уровня сложности
print("2 - Сложный")                                                        # 
difficult = int(input("Введите уровень сложности: "))                       # считываем с клавиатуры число, соответствующее выбранному уровню сложности

comp_number = -1                                                            # объявляем переменную для хранения числа компьютера
hearts = -1                                                                 # объявляем переменную для хранения количества попыток

EASY_DIFFICULT_MAX_RANGE = 10                                               # объявляем константу для хранения максимального числа диапазона
MEDIUM_DIFFICULT_MAX_RANGE = 100                                            # объявляем константу для хранения максимального числа диапазона
HARD_DIFFICULT_MAX_RANGE = 1000                                             # объявляем константу для хранения максимального числа диапазона

EASY_DIFFICULT_MAX_HEARTS = 3                                               # объявляем константу для хранения максимального числа сердец
MEDIUM_DIFFICULT_MAX_HEARTS = 5                                             # объявляем константу для хранения максимального числа сердец
HARD_DIFFICULT_MAX_HEARTS = 8                                               # объявляем константу для хранения максимального числа сердец


if difficult == GameDifficulty.EASY:                                        # если выбрана сложность EASY
    comp_number = random.randint(1, EASY_DIFFICULT_MAX_RANGE)               #     генерируем число от 1 до 10
    hearts = EASY_DIFFICULT_MAX_HEARTS                                      #     задаём количество попыток равным 3
elif difficult == GameDifficulty.MEDIUM:                                    # если выбрана сложность MEDIUM
    comp_number = random.randint(1, MEDIUM_DIFFICULT_MAX_RANGE)             #     генерируем число от 1 до 100
    hearts = MEDIUM_DIFFICULT_MAX_HEARTS                                    #     задаём количество попыток равным 5
elif difficult == GameDifficulty.HARD:                                      # если выбрана сложность HARD
    comp_number = random.randint(1, HARD_DIFFICULT_MAX_RANGE)               #     генерируем число от 1 до 100
    hearts = HARD_DIFFICULT_MAX_HEARTS                                      #     задаём количество попыток равным 8

max_hearts = hearts
print()                                                                     # 
print('=====================')                                              # выводим отступ и отделяем вступление от самой игры
print()                                                                     # 
while hearts > 0:                                                           # пока количество попыток больше нуля
    player_number = int(input("Введите число: "))                           #     считываем число игрока в переменную player_number
    hearts -= 1                                                             #     отнимаем 1 попытку
    if comp_number == player_number:                                        #     если число компьютера равно чисулу игрока
        print(f"Ура! Вы угадали число за {max_hearts - hearts} попыток")    #         выводим надпись о победе
        break                                                               #         досрочно завершаем цикл 
    elif comp_number > player_number:                                       #     иначе если число компьютера больше, чем число игрока
        print("Моё число больше")                                           #         выводим подсказку, что загаданное число больше
    elif comp_number < player_number:                                       #     иначе если число компьютера меньше, чем число игрока
        print("Моё число меньше")                                           #         выводим подсказку, что загаданное число меньше
else:                                                                       # если цикл завершился без преждевременного выхода, т.е. кончились попытки
    print(f"Увы, но Вы проиграли! Число было {comp_number}")                # выводим надпись о проигрыше