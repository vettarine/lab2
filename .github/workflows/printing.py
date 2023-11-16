from sorting import cocktail_sort


def print_salute():
    print("Шейкерная сортировка. Вариант 1.")
    print("Работу выполнили студенты 424 группы: Бертова Альбина, Миронова Таисия, Середенко Ульяна")

def print_array(array):
    print("Оригинальный массив: ", array)
    print("Отсортированный массив: ", cocktail_sort(array))
