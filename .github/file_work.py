from database_work import db_input, db_output
from array_generating import array_generating
from random import randint
from sorting import *


def file_save(array):
    """Saving the array in a file"""
    path = input("Сохранить файл в:  ")
    with open(path, 'w') as f:
        for i in range(len(array)):
            f.write(str(array[i]) + ' ')


def file_save_db(n): # тут будем генерировать n массивов и сохранять их сразу в бдшку
    for i in range(n):
        array = array_generating(randint(10, 50))
        db_input(i, array)


def file_load_db(amount): # тут будем грузить 1 рандомный массив из бд и сортировать
    index = randint(0, amount - 1) # amount - количество массивов
    array = db_output(index).split()
    return cocktail_sort(array)


def file_save_default(array, index): # тут сохранение матрицы с массивами в файл
    with open('test' + str(index) + '.txt', 'a') as f:
        for i in range(len(array)):
            f.write(str(array[i]) + ' ')
        f.write('\n')


def file_save_db_txt(index): # сохранение в бд но через сохраненный файл
    array = file_load('test' + str(index) + '.txt')
    for j in range(len(array)):
        db_input(j, array[j])


def file_load(file): # я горжусь этой функцией (выгрузка массивов из файла)
    array = []
    i = 0
    with open(file, 'r') as f:
        for line in f:
            temp_array = line.split()
            array.append([])
            for a in temp_array:
                array[i].append((int(a)))
            i += 1
    return array



