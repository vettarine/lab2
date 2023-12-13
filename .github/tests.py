from time import time
from array_generating import array_generating
from random import randint
from file_work import file_save_default, file_load
from  sorting import cocktail_sort


def test1():
    start_time = time()
    array = []
    for i in range(100):
        try:
            array = (array_generating(randint(10, 50)))
            file_save_default(array, 1)
        except:
            print("error test 1")
    end_time = time()
    print("test 1 completed, time: ", end_time - start_time)


def test2():
    start_time = time()
    array = []
    for i in range(1000):
        try:
            array = (array_generating(randint(10, 50)))
            file_save_default(array, 2)
        except:
            print("error test 2")
    end_time = time()
    print("test 2 completed, time: ", end_time - start_time)


def test3():
    start_time = time()
    array = []
    for i in range(10000):
        try:
            array = (array_generating(randint(10, 50)))
            file_save_default(array, 3)
        except:
            print("error test 3")
    end_time = time()
    print("test 3 completed, time: ", end_time - start_time)


def test4(file, amount, index): # тест с сортировкой
    start_time = time()
    try:
        array = file_load(file)
        for i in range(100):
            num = randint(0, amount - 1)
            array[num] = cocktail_sort(array[num])
    except:
        print("error test 4." + str(index))
    end_time = time()
    full_time = end_time - start_time
    avg_time = full_time / 100
    print("test 4." + str(index) + " completed, time: ", full_time, "\naverage time for each array: ", avg_time)


def test5(file, index):
    start_time = time()
    try:
        with open(file, 'r+') as f:
            f.truncate(0)
    except:
        print("error test 5." + str(index))
    end_time = time()
    full_time = end_time - start_time
    print("test 5." + str(index) + " completed, time: ", full_time)