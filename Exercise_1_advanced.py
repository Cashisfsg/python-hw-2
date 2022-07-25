def sumNum(num):
    try:
        if not len(num):
            raise IndexError

        while len(num) > 1:
            num = str(sum([int(i) for i in num]))
        print(f'Результат вычислений: {num}')
        return 1

    except IndexError:
        print('Число должно содержать хотя бы 1 цифру')
        return -1

    except ValueError:
        print('Не корректно заданное значение')
        return -1

if __name__ == '__main__':
    sumNum(input('Введите число: '))