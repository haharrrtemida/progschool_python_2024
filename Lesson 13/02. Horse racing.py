# иподром
import random
import time

# лошади
    # Имя (слово1 слово2)
    # Скорость
def generate_random_name() -> str:
    with open("first_name.txt", encoding = "UTF-8") as first_file:
        first_names = first_file.readlines()
    with open("second_name.txt", encoding = "UTF-8") as second_file:
        second_names = second_file.readlines()

    first_name = random.choice(first_names).replace("\n", "")
    second_name = random.choice(second_names).replace("\n", "")
    return " ".join([first_name, second_name])

class Horse:
    name = "Лошадь"
    speed = 3

    def __init__(self) -> None:
        self.name = generate_random_name()
        self.speed = random.randint(1, 5)

    def __str__(self) -> str:
        return self.name

class Race:
    ID = 0
    race_length = 0
    date = "00.00.00"
    prize = 0
    coating_type = ""
    horses = []
    race_finished = False
    horses_positions = {}

    def __init__(self, race_length, date, prize, coating_type, horses_count) -> None:
        self.ID = Race.ID
        Race.ID += 1

        self.race_length = race_length
        self.date = date
        self.prize = prize
        self.coating_type = coating_type
        self.horses = self.generate_horses(horses_count)

    def generate_horses(self, count : int) -> list[Horse]:
        horses = []
        for _ in range(count):
            horse = Horse()
            horses.append(horse)
            self.horses_positions[horse] = 0
        return horses
    
    def start_race(self):
        self.race_loop()

    def race_loop(self):
        while not self.race_finished:
            for horse in self.horses:
                self.horses_positions[horse] += horse.speed
                if self.horses_positions[horse] >= self.race_length:
                    self.race_finished = True
            
            if self.race_finished:
                winner = sorted(self.horses_positions.items(), key=lambda horse: horse[1], reverse=True)[0]
                print(f"Поздравляем {winner[0]} c победой!")
            for i, horse in enumerate(self.horses_positions, start=1):
                print(f"{i}. {horse.name} прошёл {self.horses_positions[horse]}")
            time.sleep(2)
            print()
                





# забег
    # номер
    # длина трассы
    # день
    # призовой фонд
    # тип покрытия
    # лошади []

race = Race(10, "10.10.24", 5000, "Grass", 5)
race.start_race()