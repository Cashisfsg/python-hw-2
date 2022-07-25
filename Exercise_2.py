def transformStr(str):
    try:
        if len(str) > 5:
            str = str[0:5] + '...'
        if str[0] in ['u', 'U']:
            str = str.upper()
        elif str[0] in ['l', 'L']:
            str = str.lower()
        print(str)
        return 1

    except IndexError:
        print('Строка должна содержать хотя бы 1 символ')
        return -1

if __name__ == '__main__':
    transformStr(input('Введите текст: '))