import numpy as np
from prettytable import PrettyTable
from simplex_method2 import simplex
from dual_linear2 import dual

cons = [[3, 5, 4, 6, 2, 1, 1, 0, 0, 0, 0, 0, 0, 0],
        [6, 2, 8, 2, 9, 3, 0, 1, 0, 0, 0, 0, 0, 0],
        [3, 6, 5, 7, 4, 6, 0, 0, 1, 0, 0, 0, 0, 0],
        [5, 3, 2, 3, 5, 3, 0, 0, 0, 1, 0, 0, 0, 0],
        [4, 8, 4, 8, 4, 5, 0, 0, 0, 0, 1, 0, 0, 0],
        [2, 4, 7, 2, 1, 2, 0, 0, 0, 0, 0, 1, 0, 0],
        [5, 2, 4, 5, 7, 1, 0, 0, 0, 0, 0, 0, 1, 0],
        [7, 9, 6, 1, 3, 2, 0, 0, 0, 0, 0, 0, 0, 1]]
#
# print(np.transpose(cons))
#
z = [-1, -8, -5, -7, -9, -3, 0, 0, 0, 0, 0, 0, 0, 0]  # initial function
b = [3, 6, 5, 2, 7, 2, 1, 4, 0]  # правые части

# cons = [[12, 15, 6, 16, 12, 7, 3, 17, 1, 0, 0, 0, 0, 0],
#             [16, 9, 7, 15, 16, 12, 11, 13, 0, 1, 0, 0, 0, 0],
#             [13, 15, 5, 12, 1, 11, 4, 10, 0, 0, 1, 0, 0, 0],
#             [0, 17, 11, 15, 11, 6, 12, 17, 0, 0, 0, 1, 0, 0],
#             [5, 11, 12, 4, 11, 18, 11, 17, 0, 0, 0, 0, 1, 0],
#             [12, 16, 14, 15, 13, 12, 13, 16, 0, 0, 0, 0, 0, 1]
#             ]

# cons = [[4, 1, 5, 13, 4, 11, 12, 14, 1, 0, 0, 0, 0, 0],
#             [17, 7, 14, 3, 11, 18, 15, 12, 0, 1, 0, 0, 0, 0],
#             [6, 19, 11, 5, 13, 7, 17, 12, 0, 0, 1, 0, 0, 0],
#             [18, 13, 16, 15, 12, 15, 11, 14, 0, 0, 0, 1, 0, 0],
#             [9, 15, 14, 8, 16, 2, 15, 9, 0, 0, 0, 0, 1, 0],
#             [13, 8, 3, 14, 19, 7, 17, 8, 0, 0, 0, 0, 0, 1]
#             ]

# cons = [[16, 20, 7, 26, 31, 10, 6, 5, 1, 0, 0, 0, 0, 0],
#             [2, 26, 36, 19, 4, 15, 34, 35, 0, 1, 0, 0, 0, 0],
#             [24, 18, 12, 7, 17, 14, 2, 17, 0, 0, 1, 0, 0, 0],
#             [18, 13, 11, 20, 19, 41, 24, 6, 0, 0, 0, 1, 0, 0],
#             [39, 22, 25, 33, 16, 12, 16, 31, 0, 0, 0, 0, 1, 0],
#             [18, 6, 36, 20, 1, 19, 37, 20, 0, 0, 0, 0, 0, 1]
#             ]

# z = [-1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0]  # initial function
# b = [1, 1, 1, 1, 1, 1, 0]  # правые части


# cons = [[18, 17, 9, 3, 3, 15, 11, 6,  1, 0, 0, 0, 0, 0],
#             [14, 13, 1, 4, 11, 0, 10, 7, 0, 1, 0, 0, 0, 0],
#             [4, 16, 4, 16, 2, 13, 15, 4, 0, 0, 1, 0, 0, 0],
#             [7, 12, 5, 5, 6, 10, 10, 4, 0, 0, 0, 1, 0, 0],
#             [5, 12, 11, 0, 15, 15, 4, 9,  0, 0, 0, 0, 1, 0],
#             [7, 13, 6, 14, 2, 6, 7, 3, 0, 0, 0, 0, 0, 1]
#             ]
#
# z = [-1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0]  # initial function
# b = [1, 1, 1, 1, 1, 1, 0]  # правые части

# cons = [[18, 17, 17, 16, 15, 7, 11, 18, 1, 0, 0, 0, 0, 0],
#             [14, 13, 1, 4, 14, 10, 10, 7, 0, 1, 0, 0, 0, 0],
#             [15, 1, 4, 16, 2, 13, 15, 4, 0, 0, 1, 0, 0, 0],
#             [7, 12, 5, 10, 6, 10, 10, 4, 0, 0, 0, 1, 0, 0],
#             [12, 12, 11, 0, 15, 16, 3, 19, 0, 0, 0, 0, 1, 0],
#             [13, 5, 6, 14, 16, 6, 7, 3, 0, 0, 0, 0, 0, 1]
#             ]
#
# z = [-1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0]  # initial function
# b = [1, 1, 1, 1, 1, 1, 0]  # правые части

#
# cons = [[1, 1, 0, 1],
#         [2, 0, 1, -1]]  # initial ogranicheniya table
# z = [-1, 2, -2, 1]  # initial function
# b = [7, 13, 0]  # правые части

print('\n1)Симплекс метод')
print('2)Двойственная задача\n')



while True:
    n = 2
    if n == 1:
        simplex(cons, z, b)
        break
    if n == 2:
        dual(cons, z, b)
        break
print('\ndone')
