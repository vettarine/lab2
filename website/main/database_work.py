import sqlite3
from .array_generating import array_character_development


def db_create(database):
    global cursor, con
    con = sqlite3.connect(database)
    cursor = con.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS array \
                    (id INTEGER PRIMARY KEY, \
                    items TEXT)"
                    )

    cursor.execute("CREATE TABLE IF NOT EXISTS array_sorted \
                        (id INTEGER PRIMARY KEY, \
                        items TEXT)"
                   )

# массивы будут в каждой строке типа '1 2 3 4 5' строкой


def db_input(index, array): # добавление массивчика в бдшку
    cursor.execute("INSERT INTO array (id, items) VALUES (?, ?)", (index, array_character_development(array))) # сиквел запрос
    con.commit()


def db_output(index): # считывание массивчика из бдшки
    cursor.execute("SELECT items FROM array WHERE id = " + str(index))  # сиквел запрос
    return cursor.fetchall()[0][0] # возвращает массив в массиве в общем чтобы строка была надо [0][0]


def db_input_sorted(index, array): # добавление отсортированного массивчика в бдшку
    cursor.execute("INSERT INTO array_sorted (id, items) VALUES (?, ?)", (index, array_character_development(array[index])))
    con.commit()


def db_delete(): # тут будет удаление всей таблицы чтобы не втыкала
    cursor.execute("DELETE FROM array")
    con.commit()
