# cocktail sort

from tests import *
from website.main.database_work import *


db_create('arrays.db')
db_delete()

test_generate(100)
test_sort(100)
test_delete(100)



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