def check_int(n):
    """Check if the input is int"""
    is_digit = True
    for i in n:
        if i not in '0123456789':
            is_digit = False
            print('Некорректный ввод')
            quit()

    if is_digit:
        if int(n) > 0:
            return int(n)
        else:
            print('Некорректный ввод')
            quit()
