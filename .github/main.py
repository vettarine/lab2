# cocktail sort

from array_generating import array_generating
from printing import print_array, print_salute
from sorting import cocktail_sort


print_salute()
num = int(input("Введите количество чисел для сортировки: "))
array = array_generating(num)
print_array(array, "Оригинальный массив: ")
print_array(cocktail_sort(array), "Отсортированный массив: ")