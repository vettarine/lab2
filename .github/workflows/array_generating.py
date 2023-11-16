from random import randint

def array_generating(num):
    array = []
    for i in range(num):  # заполнение массива случайными числами
        array.append(randint(10, 100))
    return array
