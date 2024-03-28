# раскатать тесто ________
# намазать тесто ________ соусом
# ________
# выложить ________
# запекать в духовке на ________ градусов ________ минут

# шаблон функций/процедур/методов
# def название([параметры]):
    # тело
    # функции


def make_pizza(
               dough_thickness = "толсто",
               sause_type = "томатный",
               use_cheese : bool = True,
               topings : list = [],
               baking_temperature : int = 200,
               baking_time_in_minutes : int = 7
               ):
    print("===========Готовим пиццу===========")
    print(f"Раскатываем тесто {dough_thickness}")
    print(f"Намазываем тесто {sause_type} соусом")
    print(f"Выкладываем сыр" if use_cheese else "Убераем сыр подальше")
    print(f"Выкладываем {topings}")
    print(f"Запекаем в духовке на {baking_temperature} градусов {baking_time_in_minutes} минут")
    print("===========Пицца готова===========")

make_pizza()
make_pizza(
    dough_thickness = "тонкое",
    sause_type = "кетчонез",
    topings = ["ветчина", "грибы"],
    baking_temperature = 180,
    baking_time_in_minutes = 8
    )

# как вариант для развития пиццерии
pizzas = {
    "пеперони" : {
        "dough_thickness" : "тонкое",
        "sause_type" : "томатный",
        "topings" : ["ветчина", "грибы"],
        "baking_temperature" : 180,
        "baking_time_in_minutes" : 8
    }
}
