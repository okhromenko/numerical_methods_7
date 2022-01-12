from prettytable import PrettyTable


def table_output(cons, b, z, text):
    table = PrettyTable()
    table.field_names = ["x1", "x2", "x3", "x4", "x5", "x6", "x7", "x8", "x9", "x10", "x11", "x12", "x13", "x14", "b"]
    print(text)
    for i in range(len(cons)):
        table.add_row([cons[i][0], cons[i][1], cons[i][2], cons[i][3], cons[i][4], cons[i][5], cons[i][6], cons[i][7], cons[i][8],
                       cons[i][9], cons[i][10], cons[i][11], cons[i][12], cons[i][13], b[i]])
    table.add_row([z[0], z[1], z[2], z[3], z[4], z[5], z[6], z[7], z[8], z[9], z[10], z[11], z[12], z[13], b[len(b) - 1]])
    print(table)


def simplex(cons, z, b):
    table_output(cons, b, z, 'Начальная симплекс таблица:')

    basis = [0] * len(z)
    for i in range(6, 14):
        basis[i] = True
    letters = ['x1', 'x2', 'x3', 'x4', 'x5', 'x6', 'x7', 'x8', 'x9', 'x10', 'x11', 'x12', 'x13', 'x14']
    print('Текущий базис:', end='\t')
    for i in range(len(basis)):
        if basis[i]:
            print(letters[i], end=' ')
    print()

    step = 0
    while True:
        step += 1
        # проверяем надо ли что-то делать
        sign = 1
        for i in range(len(z)):
            if z[i] < 0:
                sign = -1
        if sign > 0:
            break
        # ищем опорный столбец
        min_number = z[0]
        min_column = 0
        for i in range(len(z)):
            if z[i] < min_number:
                min_number = z[i]
                min_column = i
        # ищем опорный элемент
        min_row = -1
        for i in range(len(cons)):
            xi = cons[i][min_column]
            if xi == 0:
                continue
            if b[i] / xi < 0:
                continue
            if min_row == -1:
                b_min = b[i] / xi
                min_row = i
            else:
                if (b[i] / xi) < b_min:
                    b_min = b[i] / xi
                    min_row = i
        # меняем базиз
        basis[min_column] = True
        for i in range(len(cons[min_row])):
            if cons[min_row][i] == 1 and basis[i] == True and i != min_column:
                basis[i] = 0
        # делаем так чтобы опорный элемент равнялся единице
        divider = cons[min_row][min_column]
        for i in range(len(cons[min_row])):
            cons[min_row][i] = cons[min_row][i] / divider
        b[min_row] = b[min_row] / divider
        # делаем так чтобы в опорном столбце были все нули кроме опорного элемента
        for i in range(len(cons)):
            if i == min_row:
                continue
            factor = cons[i][min_column] / cons[min_row][min_column]
            for j in range(len(cons[min_row])):
                a = cons[min_row][j] * factor
                cons[i][j] = cons[i][j] - a
            b[i] = b[i] - b[min_row] * factor
        factor = z[min_column] / cons[min_row][min_column]
        for i in range(len(z)):
            z[i] = z[i] - cons[min_row][i] * factor
        b[len(b) - 1] = b[len(b) - 1] - b[min_row] * factor
        table_output(cons, b, z, 'Шаг {}:'.format(step))
        # вывод базиса
        print('Текущий базис:', end='\t')
        for i in range(len(basis)):
            if basis[i]:
                print(letters[i], end=' ')
        print()
    table_output(cons, b, z, 'Конечная симплекс таблица:')
    for i in range(len(basis)):
        if basis[i]:
            print(letters[i], end=' ')
    print()
    for i in range(len(cons)):
        for j in range(len(cons[min_row])):
            if cons[i][j] == 1 and basis[j] == True:
                basis[j] = b[i]
    for i in range(len(basis)):
        if basis[i]:
            print(letters[i], '=', basis[i])
    print(basis)
    print('\nОтвет: ', end="")
    print('z(max) = z({},{},{},{},{},{}, {}, {}) = {}'.format(basis[0], basis[1], basis[2], basis[3], basis[4], basis[5], basis[6], basis[7], b[len(b) - 1]))
    print('\n')