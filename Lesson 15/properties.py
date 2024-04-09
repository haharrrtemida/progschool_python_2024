class Person:
    city = ""
    def __init__(self, name : str, age : int) -> None:
        self.__name = name
        self.__age = age

    def __get_age(self):
        return self.__age
    
    def __set_age(self, value):
        # if type(value) is int:
        if isinstance(value, int) and value >= 0:
            self.__age = value
        else:
            raise TypeError("Возраст должен задаваться целым числом")
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        if isinstance(value, str):
            self.__name = value
        else:
            raise TypeError("Имя должно задаваться строкой")

    age = property(__get_age, __set_age)
"""
    getter  – get (получить)
    setter  – set (задать)
    deleter – delete (удалить)
"""

h1 = Person("Николай", 27)
h1.age = 15
print(h1.age)

h1.name = "Владимир"
print(h1.name)