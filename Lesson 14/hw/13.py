import random

# Функция для чтения имен или фамилий из файла
def read_names_from_file(file_path):
    with open(file_path, encoding='utf-8') as file:
        return [line.strip() for line in file.readlines()]

# Генерация уникального имени и фамилии
def generate_unique_name(first_names, last_names):
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)
    first_names.remove(first_name)
    last_names.remove(last_name)
    return first_name + " " + last_name

# Генерация случайной скорости
def generate_random_speed(min_speed, max_speed):
    return random.uniform(min_speed, max_speed)

# Рассчитываем время, за которое участник пробежит дистанцию
def calculate_time(distance, speed):
    return distance / speed

# Основная программа
first_names = read_names_from_file('first_names.txt')  # Путь к файлу с именами
last_names = read_names_from_file('last_names.txt')    # Путь к файлу с фамилиями
distance = 402  # Дистанция забега в метрах
MIN_SPEED = 2   # Минимальная скорость участника в м/с
MAX_SPEED = 12  # Максимальная скорость участника в м/с

runners = []
for _ in range(3):
    name = generate_unique_name(first_names, last_names)
    speed = generate_random_speed(MIN_SPEED, MAX_SPEED)
    time = calculate_time(distance, speed)
    runners.append((name, speed, time))

# Сортируем участников по времени
runners.sort(key=lambda x: x[2])

# Выводим победителя
winner_name, winner_speed, winner_time = runners[0]
print(f"Победитель в забеге синих аватаров: {winner_name}, время: {winner_time:.2f} секунд")

# Выводим результаты остальных участников
for name, speed, time in runners[1:]:
    print(f"Лузер: {name}, время: {time:.2f} секунд")
    print("Он совсем не молодец!")
