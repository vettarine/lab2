from database_work import db_input

def file_save(array):
    """Saving the array in a file"""
    path = input("Сохранить файл в:  ")
    with open(path, 'w') as f:
        for i in range(len(array)):
            f.write(str(array[i]) + ' ')

def file_save_default(array, index):
    with open('test' + str(index) + '.txt', 'a') as f:
        for i in range(len(array)):
            f.write(str(array[i]) + ' ')
        f.write('\n')


def file_save_db(index):
    array = file_load('test' + str(index) + '.txt')
    for j in range(len(array)):
        db_input(j, array[j])

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



