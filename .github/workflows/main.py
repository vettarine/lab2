# cocktail sort

def cocktail_sort(array):
    for i in range(len(array) - 1, 0, -1):
        is_swapped = False

        for j in range(i, 0, -1):
            if array[j] < array[j - 1]:
                array[j], array[j - 1] = array[j - 1], array[j]
                is_swapped = True

        for j in range(i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                is_swapped = True

        if not is_swapped:
            return array


array = [15, 37, 69, 26, 78]
print(cocktail_sort(array))
print('yazaebalas')
