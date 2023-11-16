# cocktail sort

from array_generating import array_generating
from printing import print_array, print_salute


print_salute()
num = int(input("Введите количество чисел для сортировки: "))
array = array_generating(num)
print_array(array)
