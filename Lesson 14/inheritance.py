class Animal:
    sound = ""

    def __init__(self, name) -> None:
        self.name = name


    def eat(self, food : str):
        print(f"{self.name}: Съел {food}")

    def drink(self):
        print(f"{self.name}: Испил водицы")

    def sleep(self):
        print(f"{self.name}: Хрррр....")

    def make_sound(self):
        print("Животное говорит")

class Cat(Animal):
    sound = "Мяу"

    def __init__(self, name, fur_color) -> None:
        super().__init__(name)
        self.fur_color = fur_color
    
    def make_sound(self):
        print(f"{self.name}: {Cat.sound}")
        super().make_sound()

class Dog(Animal):
    sound = "Гав"
    
    def make_sound(self):
        print(f"{self.name}: {Dog.sound}")


class Parrot(Animal):
    sound = "Чирик"

    def make_sound(self):
        print(f"{self.name}: {Parrot.sound}")
    
    def __str__(self) -> str:
        return f"Это попугай {self.name}"


cat = Cat("Мышь", "Белый")
dog = Dog("Рекс")
parrot = Parrot("Кеша")

cat.make_sound()
dog.make_sound()
parrot.make_sound()

print(parrot)