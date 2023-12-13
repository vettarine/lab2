# cocktail sort

from array_generating import array_generating
from printing import print_array, print_salute
from sorting import cocktail_sort
from file_work import file_save, file_load
from cheker import check_int
from tests import *
from database_work import *


db_create('arrays.db')

test1()


"""
test1()
test2()
test3()
test4('test1.txt', 100, 1)
test4('test2.txt', 1000, 2)
test4('test3.txt', 10000, 3)
test5('test1.txt', 1)
test5('test2.txt', 2)
test5('test3.txt', 3)
"""

"""
print_salute()
num = check_int(input("Введите количество чисел для сортировки: "))
array = array_generating(num)
print_array(array, "Оригинальный массив: ")
sorted_array = cocktail_sort(array)
print_array(sorted_array, "Отсортированный массив: ")
file_save(sorted_array)
"""