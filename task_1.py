def summ(x):
    s = 0
    while x > 0:
        s += x % 10
        x //= 10
    return s


def minn(x):
    m = x % 10
    x //= 10
    while x > 0:
        if x % 10 < m:
            m = x % 10
        x //= 10
    return m


def maxx(x):
    m = x % 10
    x //= 10
    while x > 0:
        if x % 10 > m:
            m = x % 10
        x //= 10
    return m


while True:
    print('1 - Сумма цифр\n2 - Максимальная цифра\n3 - Минимальная цифра')
    act = int(input('Выберете действие: '))
    num = int(input('Введите число: '))

    if act == 1:
        print(f'Сумма цифр числа {num} - {summ(num)}')

    elif act == 2:
        print(f'Максимальная цифра числа {num} - {maxx(num)}')

    elif act == 3:
        print(f'Минимальная цифра числа {num} - {minn(num)}')

    else:
        print('Такого действия нет')