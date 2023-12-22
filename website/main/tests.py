from time import time
from .file_work import *
from .database_work import db_delete


def test_generate(amount):  # генерим 100 массивчиков и закидываем в бд
    start_time = time()
    try:
        file_save_db(amount)
    except:
        output = "error in generating test for " + str(amount) + " arrays"
        return output
    end_time = time()
    full_time = round(((end_time - start_time) * 1000), 4)

    output = "generating test for " + str(amount) + " arrays completed, time: " + str(full_time) + " ms"
    return output


def test_sort(amount):  # тут надо будет считать с бд 100 рандомных массивов и отсортировать
    start_time = time()
    try:
        for i in range(100):
            file_load_db(amount)  # amount - количество массивов в бд (100, 1000, 10000)
    except:
        output = "error in sorting test for " + str(amount) + " arrays"
        return output
    end_time = time()
    full_time = round(((end_time - start_time) * 1000), 4)
    avg_time = round((full_time / 100), 4)
    output = "sorting test for " + str(amount) + " arrays completed, time: " + str(full_time) + " ms" + \
             "\naverage time for each array: " + str(avg_time) + " ms"
    return output


def test_delete(amount):
    start_time = time()
    try:
        db_delete()
    except:
        output = "error in deleting test for " + str(amount) + " arrays"
        return output
    end_time = time()
    full_time = round(((end_time - start_time) * 1000), 4)
    output = "deleting test for " + str(amount) + " arrays completed, time: " + str(full_time) + " ms"
    return output
