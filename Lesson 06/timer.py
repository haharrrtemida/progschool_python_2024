import time

seconds = int(input("Время: "))
while seconds > 0:
    print(seconds)
    time.sleep(1)
    seconds -= 1
    if seconds == 5:
        break
else:
    print("Время вышло!")