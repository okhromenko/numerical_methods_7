import math
import numpy as np

A = np.array([
    [175, 92, 131, 91, 161, 147],
    [92, 104, 136, 55, 115, 119],
    [131, 36, 200, 77, 168, 199],
    [91, 55, 77, 52, 94, 84],
    [161, 115, 168, 94, 196, 176],
    [147, 119, 199, 84, 176, 232]])

b = np.array([2,
     1,
     1,
     6,
     2,
     4])

x_0 = np.array([1,
       3,
       1,
       1,
       2,
       3])

epsilon = 10 ** -6
lambda_ = 10 ** -4
K = 0

def f(x):
    return 0.5 * np.transpose(x) @ A @ x + b @ x

def pos_defined(x):
    return np.all(np.linalg.eigvals(x) > 0)

def f_derivative(A, b, x):
    A_t = np.transpose(A)
    return 0.5 * (A + A_t) @ x + b

def gradDescent(A, b, x_0, epsilon, lambda_):
    count = 1
    if pos_defined(A):
        x_pr = x_0.copy()
        x = x_pr - lambda_ * f_derivative(A, b, x_pr)
        while np.linalg.norm(x - x_pr) > epsilon:
            x_pr = x
            x = x_pr - lambda_ * f_derivative(A, b, x_pr)
            count += 1
        print(x)
        print(f(x))
    # P = -np.linalg.inv(A) @ b
    # print(P)
    # delta = np.abs(P - x)
    # print(delta, f(x), f(P))



gradDescent(A, b, x_0, epsilon, lambda_)

