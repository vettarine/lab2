# cocktail sort

def cocktail_sort(sort_array):
    for i in range(len(sort_array) - 1, 0, -1):
        is_swapped = False

        for j in range(i, 0, -1):
            if sort_array[j] < sort_array[j - 1]:
                sort_array[j], sort_array[j - 1] = sort_array[j - 1], sort_array[j]
                is_swapped = True

        for j in range(i):
            if sort_array[j] > sort_array[j + 1]:
                sort_array[j], sort_array[j + 1] = sort_array[j + 1], sort_array[j]
                is_swapped = True

        if not is_swapped:
            return sort_array


array = [15, 37, 69, 26, 78]
print(cocktail_sort(array))
print('yazaebalas')
