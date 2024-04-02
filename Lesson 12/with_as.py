# 1 вариант
file = open("top secret.txt", 'a+', encoding = "UTF-8")
print(file.read())
file.close()

# 2 вариант
# with open() as переменная:
    # тело
    # менеджера
    # контекста

with open("top secret.txt", 'a+', encoding = "UTF-8") as file:
    text = file.read()