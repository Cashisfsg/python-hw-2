def commonStr(str):
    print(''.join([i if i in set(str[0]) else '' for i in set(str[1])]))
    return 1

if __name__ == '__main__':
    commonStr([input(f'Введите строку {i+1}: ') for i in range(2)])