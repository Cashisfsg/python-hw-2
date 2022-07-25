def oddOrEven(num):
    try:
        num = int(num)
        print(f'Число {num} является {"нечётным" if num % 2 else "чётным"}')
        return 1

    except ValueError:
        print('Не корректно введеное значение')
        return -1

if __name__ == '__main__':
    oddOrEven(input('Введите число: '))
