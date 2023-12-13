def file_save(array):
    """Saving the array in a file"""
    path = input("Сохранить файл в:  ")
    with open(path, 'w') as f:
        for i in range(len(array)):
            f.write(str(array[i]) + ' ')

def file_save_default(array, i):
    with open('test' + str(i) + '.txt', 'a') as f:
        for i in range(len(array)):
            f.write(str(array[i]) + ' ')
        f.write('\n')

def file_load(file): # я горжусь этой функцией
    array = []
    i = 0
    with open(file, 'r') as f:
        for line in f:
            temp_array = line.split()
            array.append([])
            for a in temp_array:
                array[i].append((int(a)))
            i += 1
    return array

def array_character_development(array):
    list = ''
    for a in array:
        list += str(a) + ' '
    list = list[:-1]
    return list

