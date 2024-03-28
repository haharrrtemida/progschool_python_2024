# класс
# шаблон
# class название:
    # тело
    # класса

class Cat:
    color = "белый"
    breed = "шотландец"
    name = "Мышь"
    age = 2.5
    
    def __init__(self, name = "Пусто", age = 0) -> None:
        self.name = name
        self.age = age

    def eat(self, food_name : str):
        print(f"{self.name}: Я съел(а) {food_name}")


    def __del__(self):
        print("Прощай жестокий мир....")

    def __add__(self, other_cat):
        new_cat = Cat()
        new_cat.breed = self.breed
        new_cat.color = other_cat.color
        return new_cat

    def __str__(self):
        return f"{self.name}, {self.age} лет, {self.color} {self.breed}"


mysh = Cat()
smoke = Cat("Дымок")

print(mysh.name)
print(smoke.name)

mysh.eat("рыбу")
smoke.eat("паштет")



smoke.weight = 3

# выведет вес Дымка, но будет ошибка на весе Мыши, 
# т.к. у этого объекта нет такого поля
# print(smoke.weight)
# print(mysh.weight)

# del smoke

kitty = mysh + smoke
print(kitty.color)
print(kitty.breed)

print(kitty)


input()
# Cat.eat("пюрешка")