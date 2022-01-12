import math
import numpy as np
import scipy
from scipy.optimize import minimize

A = np.matrix([
    [7, 4, -9, -2],
    [4, 11, -7, -8],
    [-9, -7, 6, 10],
    [-2, -8, 10, 3]])

b = np.array([3,
     7,
     5,
     2])

x_0 = np.array([-4,
       2,
       2,
       1])

r = 10

x_1 = -(np.linalg.inv(A)) @ b
x_diff = np.linalg.norm(x_0 - x_1)

def f(A, x, b):
    return 0.5 * np.dot(x * A, x) + np.dot(b, x)

def F(A, x, b, x_0, y, r):
    one = A @ x.T + b.T + 2 * y * (x.T - x_0.T)
    two = np.linalg.norm(x - x_0) ** 2 - r ** 2
    res = np.array([one[0, 0], one[0, 1], one[0, 2], one[0, 3], two])
    return res

def W(A, x, y):
    return np.matrix([[A[0, 0] + 2 * y, A[0, 1], A[0, 2], A[0, 3], 2 * (x[0] - x_0[0])],
                                [A[1, 0], A[1, 1] + 2 * y, A[1, 2], A[1, 3], 2 * (x[1] - x_0[1])],
                                [A[2, 0], A[2, 1], A[2, 2] + 2 * y, A[2, 3], 2 * (x[2] - x_0[2])],
                                [A[3, 0], A[3, 1], A[3, 2], A[3, 3] + 2 * y, 2 * (x[3] - x_0[3])],
                                [2 * (x[0] - x_0[0]), 2 * (x[1] - x_0[1]), 2 * (x[2] - x_0[2]), 2 * (x[3] - x_0[3]), 0]])

def Newton(count, x):
    for i in range(count):
        w = np.linalg.inv(W(A, x[:4], x[4]))
        x = x - np.array(w @ F(A, x[:4], b, x_0, x[4], r))[0]
    return x

def result():
    count = 100
    y = 0
    x_vec = []
    res_fun = []
    res = []

    for i in range(4):
        x_plus = np.concatenate((x_0, [y])).copy()
        x_plus[i] = x_plus[i] + r
        x_vec.append(x_plus)

    for i in range(4):
        x_minus = np.concatenate((x_0, [y])).copy()
        x_minus[i] = x_minus[i] - r
        x_vec.append(x_minus)

    for x in x_vec:
        res.append(Newton(count, x))

    for x in res:
        res_fun.append(f(A, x[:4], b))

    for i in res:
        print("res", i)
    print()

    for i in res_fun:
        print("res_fun", i)
    print()


result()
