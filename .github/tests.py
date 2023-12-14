from time import time
from array_generating import array_generating
from random import randint
from file_work import *
from sorting import cocktail_sort
from database_work import db_delete


def test1(): # генерим 100 массивчиков и закидываем в бд
    start_time = time()
    num = 100
    try:
        file_save_db(num)
    except:
        print("error test 1")
    end_time = time()
    print("test 1 completed, time: ", end_time - start_time)


def test2(): # 1000
    start_time = time()
    num = 1000
    try:
        file_save_db(num)
    except:
        print("error test 2")
    end_time = time()
    print("test 2 completed, time: ", end_time - start_time)


def test3(): # 10000
    start_time = time()
    num = 10000
    try:
        file_save_db(num)
    except:
        print("error test 3")
    end_time = time()
    print("test 3 completed, time: ", end_time - start_time)


def test4(amount): # тут надо будет считать с бд 100 рандомных массивов и отсортировать
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


def test5(amount):
    start_time = time()
    index = len(str(amount // 100))
    try:
        db_delete()
    except:
        print("error test 5." + str(index))
    end_time = time()
    full_time = end_time - start_time
    print("test 5." + str(index) + " completed, time: ", full_time)
