import math
import numpy as np

# a = [0, 0.01706036745406822, 0, 0, 0.005249343832020994, 0.058398950131233626, 0, 0.1456692913385828]
a = [0, 0, 0, 0, 0.02730706224972697, 0.0010238441936658241, 0.01591053876956679, 0.009555879140880963]
a_norm = 1 / np.linalg.norm(a)
print(a_norm)

t = 0
for i in a:
    print(i * 18.6)
    t = t + (i * 18.6)
print(t)

# cons_i = [[12, 15, 6, 16, 12, 7, 3, 17],
#             [16, 9, 7, 15, 16, 12, 11, 13],
#             [13, 15, 5, 12, 1, 11, 4, 10],
#             [0, 17, 11, 15, 11, 6, 12, 17],
#             [5, 11, 12, 4, 11, 18, 11, 17],
#             [12, 16, 14, 15, 13, 12, 13, 16]
#             ]
#
# cons_T = np.transpose(cons_i)
#
# print(cons_T)
# # for j in range(6):
# #     sum = 0
# #     for i in range(8):
# #         sum = sum + cons_T[i][j]
# #     print(sum)