import random as rd


def rock_paper_scissors():
    pl_ch = int(input('\nВводи свой знак(1 - камень, 2 - ножницы, 3 - бумага, 4 - выйти в меню): '))
    pc_ch = rd.randint(1, 3)

    if pl_ch in (1,2,3):
        if (pl_ch == 3 and pc_ch == 1) or (pl_ch == 1 and pc_ch == 2) or (pl_ch == 2 and pc_ch == 3):
            print(f'Победил, чертяка. Мой знак {pc_ch}')
        elif pl_ch == pc_ch:
            print('Ничья')
        else:
            print(f'Проебал. Мой знак {pc_ch}')
        rock_paper_scissors()

    elif pl_ch == 4:
        mainMenu()

    else:
        print('Еблан? Выбери число от 1 до 4-х')
        rock_paper_scissors()


def guess_the_number():
    pl_num = int(input('\nОтгадай число от 1 до 10(0 - меню): '))
    pc_num = rd.randint(1, 10)

    if pl_num == 0:
        mainMenu()
    else:
        if pc_num == pl_num:
            print('ЕБАТЬ УГАДАЛ')
        else:
            print(f'Не угадал. ЛОХ. Число {pc_num}')
        guess_the_number()


def mainMenu():
    game = int(input('Здарова\n1 - Камень, Ножницы, Бумага\n2 - Лохотрон(исправить)\n3 - Выйти\nВыбирай: '))

    if game == 1:
        rock_paper_scissors()
    elif game == 2:
        guess_the_number()
    elif game == 3:
        quit()
    else:
        print('Такой игры нет, выбирай из того что есть, дружок')


mainMenu()