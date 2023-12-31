def cocktail_sort(sort_array):
    """Sort with cocktail sort method and return the array"""
    length = len(sort_array) # длина массива
    for i in range(length - 1, 0, -1):
        is_swapped = False  # цикл идет, пока элементы меняются местами (т.е. пока не стоят в нужном порядке)

        for j in range(i, 0, -1):  # сортировка с конца массива (меньший элемент к началу массива)
            if sort_array[j] < sort_array[j - 1]:
                sort_array[j], sort_array[j - 1] = sort_array[j - 1], sort_array[j]
                is_swapped = True  # элементы меняли местами или нет?

        for j in range(i):  # сортировка с начала массива (больший элемент к концу массива)
            if sort_array[j] > sort_array[j + 1]:
                sort_array[j], sort_array[j + 1] = sort_array[j + 1], sort_array[j]
                is_swapped = True  # элементы меняли местами или нет?

        if not is_swapped:  # если элементы не переставляли (все элементы в нужном порядке)
            return sort_array
