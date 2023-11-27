# cocktail sort

from array_generating import array_generating
from printing import print_array, print_salute
from sorting import cocktail_sort
from file_work import file_save


print_salute()
num = int(input("Введите количество чисел для сортировки: "))
array = array_generating(num)
sorted_array = cocktail_sort(array)
print_array(array, "Оригинальный массив: ")
print_array(sorted_array, "Отсортированный массив: ")
file_save(sorted_array)
