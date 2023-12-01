def file_save(array):
    """Saving the array in a file"""
    path = input("Сохранить файл в:  ")
    with open(path, 'w') as f:
        f.write(str(array))
