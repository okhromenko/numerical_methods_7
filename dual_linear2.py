from prettytable import PrettyTable

def table_output(cons, b, z, text):
    table = PrettyTable()
    # table.field_names = ["y1", "y2", "y3", "y4", "y5", "y6", "y7", "y8", "s1", "s2", "s3", "s4", "s5", "s6",
    #                      "r1", "r2", "r3", "r4", "r5", "r6", "b"]
    table.field_names = ["y1", "y2", "y3", "y4", "y5", "y6", "s1", "s2", "s3", "s4", "s5", "s6", "s75", "s8",
                         "r1", "r2", "r3", "r4", "r5", "r6", "r7", "r8","b"]
    print(text)
    for i in range(len(cons)):
        table.add_row(
            [cons[i][0], cons[i][1], cons[i][2], cons[i][3], cons[i][4], cons[i][5], cons[i][6], cons[i][7], cons[i][8],
             cons[i][9], cons[i][10], cons[i][11], cons[i][12], cons[i][13], cons[i][14], cons[i][15], cons[i][16], cons[i][17], cons[i][18], cons[i][19],
             cons[i][20], cons[i][21],b[i]])
    table.add_row([z[0], z[1], z[2], z[3], z[4], z[5], z[6], z[7], z[8], z[9], z[10], z[11], z[12], z[13], z[14],  z[15], z[16], z[17], z[18], z[19],
                   z[20], z[21], b[len(b) - 1]])
    print(table)


def dual(cons, z, b):
    # cons = [[3, 6, 3, 5, 4, 2, 5, 7, -1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    #         [5, 2, 6, 3, 8, 4, 2, 9, 0, -1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    #         [4, 8, 5, 2, 4, 7, 4, 6, 0, 0, -1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    #         [6, 2, 7, 3, 8, 2, 5, 1, 0, 0, 0, -1, 0, 0, 0, 0, 0, 1, 0, 0],
    #         [2, 9, 4, 5, 4, 1, 7, 3, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 1, 0],
    #         [1, 3, 6, 3, 5, 2, 1, 2, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 1]
    #         ]
    # b = [1, 8, 5, 7, 9, 3, -33]
    # z = [-21, -30, -31, -21, -33, -18, -24, -28, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0]


    cons = [[12, 16, 13,  0,  5, 12, -1, 0, 0, 0, 0, 0,0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
            [15,  9, 15, 17, 11, 16, 0, -1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
            [6,  7,  5, 11, 12, 14, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [16, 15, 12, 15,  4, 15, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
            [12, 16,  1, 11, 11, 13, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
            [7, 12, 11,  6, 18, 12, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [3, 11,  4, 12, 11, 13, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 1, 0],
            [17, 13, 10, 17, 17, 16, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 1]
            ]

    b = [1, 1, 1, 1, 1, 1, 1, 1, -8]
    z = [-88, -99, -71, -89, -89, -111, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]
    table_output(cons, b, z, 'Начальная симплекс таблица:')

    basis = [False] * len(z)
    for i in range(13, 20):
        basis[i] = True
    letters = ['y1', 'y2', 'y3', 'y4', 'y5', 'y6', 's1', 's2', 's3', 's4', 's5', 's6', 's7', 's8',
               'r1', 'r2', 'r3', 'r4', 'r5', 'r6', 'r7', 'r8']
    print('Текущий базис:', end='\t')
    for i in range(len(basis)):
        if basis[i]:
            print(letters[i], end=' ')
    print()
    step = 0
    while True:
        step += 1

        sign = 1
        for i in range(len(z)):
            if round(z[i], 4) < 0:
                sign = -1
        if sign > 0:
            break

        min_number = z[0]
        min_column = 0
        for i in range(len(z)):
            if z[i] < min_number:
                min_number = z[i]
                min_column = i

        min_row = -1
        for i in range(len(cons)):
            xi = cons[i][min_column]
            if xi == 0:
                continue
            if xi < 0:
                continue
            if min_row == -1:
                b_min = b[i] / xi
                min_row = i
            else:
                if (b[i] / xi) < b_min:
                    b_min = b[i] / xi
                    min_row = i

        basis[min_column] = True
        for i in range(len(cons[min_row])):
            if cons[min_row][i] == 1 and basis[i] == True and i != min_column:
                basis[i] = False

        divider = cons[min_row][min_column]
        for i in range(len(cons[min_row])):
            cons[min_row][i] = cons[min_row][i] / divider
        b[min_row] = b[min_row] / divider

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

        print('Текущий базис:', end='\t')
        for i in range(len(basis)):
            if basis[i]:
                print(letters[i], end=' ')
        print()

    table_output(cons, b, z, 'Конечная симплекс таблица:')
    print('Конечный базис:', end='\t')
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
    print('\nОтвет: ', end="")
    print(basis)
    print(f'Z = {7 * basis[0] + 13 * basis[1]}')
    print('\n')