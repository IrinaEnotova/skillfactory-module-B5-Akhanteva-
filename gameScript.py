# Крестики-нолики

# Приветствие + правила

print('-------------------------------------------------------------------------')
print('Привет! Зови друга и сыграй в крестики-нолики!')
print('ЦЕЛЬ игры - первым заполнить ряд по вертикали, горизонтали или диагонали')
print('Если все клетки заполнены, и никому не удалось заполнить ряд - НИЧЬЯ.')
print('-------------------------------------------------------------------------')

confirmation = input('Готовы? \nВведите Y для начала игры, N, если передумали. \n').upper()
field = [['-', '-', '-'],
        ['-', '-', '-'],
        ['-', '-', '-']]
user = 'x'
step = 0

# Определение функций
def create_field(field):
    print('  0 1 2')
    for i in range(len(field)):
        print(str(i), *field[i])

def enter_coord(field):
    while True:
        coord = input('Введите координаты клетки в формате "X Y" \n').split()
        if len(coord) != 2:
            print('ВНИМАНИЕ! Введите две координаты через пробел')
            continue
        if not(coord[0].isdigit() and coord[1].isdigit()):
            print('ВНИМАНИЕ! Введите числа')
            continue
        x, y = map(int, coord)
        if not(0 <= x <= 2 and 0 <= y <= 2):
            print('ВНИМАНИЕ! Введите числа от 0 до 2')
            continue
        if field[x][y] != '-':
            print('ВНИМАНИЕ! Выбранная клетка занята')
            continue
        break
    return x, y

def check_each_line(item1, item2, item3, user):
    if item1 == user and item2 == user and item3 == user:
        return True

def find_winner(field, user):
    for i in range(3):
        if check_each_line(field[i][0], field[i][1], field[i][2], user) or \
            check_each_line(field[0][i], field[1][i], field[2][i], user) or \
            check_each_line(field[0][0], field[1][1], field[2][2], user) or \
            check_each_line(field[2][0], field[2][1], field[2][2], user):
            return True
    return False

while True:
    if confirmation == 'N':
        print('-------------------------------------------------------------------------')
        print('Приходи поиграть потом! Пока!')
        print('-------------------------------------------------------------------------')
        break
    elif confirmation != 'N' and confirmation != 'Y':
        confirmation = input('Сыграем? Введи Y или N \n').upper()
        continue
    else:
        print('-------------------------------------------------------------------------')
        print('Начинаем с крестиков!')
        print('-------------------------------------------------------------------------')

        while True:
            if step == 9:
                print('-------------------------------------------------------------------------')
                print('НИЧЬЯ! Попробуйте еще раз!')
                print('-------------------------------------------------------------------------')
                break
            if find_winner(field, user):
                print('-------------------------------------------------------------------------')
                print('ВЫИГРАЛ', user, '!')
                print('-------------------------------------------------------------------------')
                break
            if step % 2 == 0:
                user = 'x'
            else:
                user = 'o'
            create_field(field)
            x, y = enter_coord(field)
            field[x][y] = user
            step += 1
    print('-------------------------------------------------------------------------')
    print('Классная игра! Запускай игру еще раз!')
    print('-------------------------------------------------------------------------')
    break
