from sympy import *
import numpy as np


a = 0
b = 1

n = 3

s, x = var('s x')

f = 0.5 / sqrt(x)

alpha = [x, x**3, x**5]

beta = [-0.6 * s**0, 0.6**3 * s**2 / factorial(3), -0.6**5 * s**4 / factorial(5)]

f_i = []
u = []
A = np.zeros((n, n))
C = np.zeros((n, n))

for i in range(n):
    f_i.append(float(integrate(beta[i] * f.subs({x: s}), (s, a, b))))

for i in range(n):
    for j in range(n):
        A[j][i] = integrate(alpha[j].subs({x: s}) * beta[i].subs({x: s}), (s, a, b))

for i in range(n):
    for j in range(n):
        C[j][i] = np.array(float(int(i == j) - A[i][j]))

C = np.linalg.solve(C, f_i)

u.append(f)
for i in range(n):
    u.append(sum([C[i] * alpha[i]]))

for i in u:
    print(i, end=" ")