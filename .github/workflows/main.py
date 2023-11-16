# cocktail sort

from random import randint
from sorting import cocktail_sort


print("Шейкерная сортировка. Вариант 1.")
print("Работу выполнили студенты 424 группы: Бертова Альбина, Миронова Таисия, Середенко Ульяна")
num = int(input("Введите количество чисел для сортировки: "))
array = []

for i in range(num): # заполнение массива случайными числами
    array.append(randint(10, 100))

print("Оригинальный массив: ", array)
print("Отсортированный массив: ", cocktail_sort(array))

