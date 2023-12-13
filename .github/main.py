# cocktail sort

from array_generating import array_generating
from printing import print_array, print_salute
from sorting import cocktail_sort
from file_work import file_save
from cheker import check_int


print_salute()
num = check_int(input("Введите количество чисел для сортировки: "))
array = array_generating(num)
print_array(array, "Оригинальный массив: ")
sorted_array = cocktail_sort(array)
print_array(sorted_array, "Отсортированный массив: ")
file_save(sorted_array)
