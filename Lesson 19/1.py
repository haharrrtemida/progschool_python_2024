import sqlite3

with sqlite3.connect('test.db') as con:
    cursor = con.cursor()

    name = input()

    result = cursor.execute(f"""SELECT photo FROM ARTISTS where NAME = \"{name}\"""")
    photo = result.fetchone();

    with open("test.png", mode = "wb") as file:
        file.write(photo[0])
    