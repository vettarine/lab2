from time import time
from website.main.file_work import *
from website.main.database_work import db_delete


def test_generate(amount): # генерим 100 массивчиков и закидываем в бд
    start_time = time()
    index = len(str(amount // 100))
    try:
        file_save_db(amount)
    except:
        print("error test 1")
    end_time = time()
    full_time = end_time - start_time
    print("test " + str(index) + " completed, time: ", full_time)




def test_sort(amount): # тут надо будет считать с бд 100 рандомных массивов и отсортировать
    start_time = time()
    index = len(str(amount // 100))
    try:
        for i in range(100):
            file_load_db(amount) # amount - количество массивов в бд (100, 1000, 10000)
    except:
        print("error test 4." + str(index))
    end_time = time()
    full_time = end_time - start_time
    avg_time = full_time / 100
    print("test 4." + str(index) + " completed, time: ", full_time, "\naverage time for each array: ", avg_time)


def test_delete(amount):
    start_time = time()
    index = len(str(amount // 100))
    try:
        db_delete()
    except:
        print("error test 5." + str(index))
    end_time = time()
    full_time = end_time - start_time
    print("test 5." + str(index) + " completed, time: ", full_time)
