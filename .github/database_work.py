import sqlite3
from file_work import array_character_development


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

# массивы будут в каждой строке типа [1&2&3&4&5]

def db_input(index, array):
    cursor.execute("INSERT INTO array (id, items) VALUES (?, ?)", (index, array_character_development(array)))
    con.commit()
