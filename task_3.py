def reversal(x):
    x1 = ''
    for i in range(len(x) - 1, -1, -1):
        x1 += x[i]
    return x1

n = input('Введите первое число: ')
m = input('Введите второе число: ')

n_mdf = int(reversal(n))
m_mdf = int(reversal(m))

print(f'Первое число наоборот: {n_mdf}\nВторое число наоборот: {m_mdf}')
print(f'Сумма: {n_mdf + m_mdf}')
print(f'Сумма наоборот: {int(n) + int(m)}')