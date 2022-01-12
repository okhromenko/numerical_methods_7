import numpy as np
import matplotlib.pyplot as plt
from sympy import *

n = 3

a = 0
b = 1

u_0 = -0.5
u_1 = -1

n_x = 10
h = (b - a) / n_x

x = symbols('x')

P = 2 / (x - 2)
Q = (x - 2)
F = 1
u = 1 / (x - 2)

for i in range(1, n):
    C = [1] + list(symbols(' '.join('c{}'.format(i))))

phi_0 = -0.5 * (x + 1)
phi_1 = x ** 2 * (x - 1)
phi_2 = x * (x ** 2 - 1)

phi = np.array((phi_0, phi_1, phi_2))

for i in range(1, n):
    U = phi[0] + sum([phi[i] * C[i]])

def Galerkin_method():
    R = diff(U, x, 2) + P * diff(U, x) + Q * U - F

    R_ort = []
    for i in range(1, n):
        R_ort.append(R * phi[i])

    for i in R_ort:
        A = [integrate(i, (x, a, b))]
    result = solve(A, C)
    return U.subs(result)


def Collocation_method():
    x_col = [0.25, 0.5]
    R = diff(U, x, 2) + P * diff(U, x) + Q * U - F

    for i in x_col:
        A = [R.subs(x, i)]
    result = solve(A, C)
    return U.subs(result)


def Ritz_method():
    p = exp(integrate(P, (x, a, x)))
    q = p * Q
    f = p * F
    dJ = p * diff(U, x)**2 - q * U**2 + 2 * f * U
    J = integrate(dJ, (x, a, b))

    for i in range(1, n):
        A = [diff(J, C[i])]

    res = solve(A, C)
    return U.subs(res)


res1 = Collocation_method()
res2 = Ritz_method()
res3 = Galerkin_method()

X = []
for i in range(n_x):
    X.append(i * h)

Y_Ritz = []
Y_Collocation = []
Y_Galerkin = []
Y_decision = []
for i in X:
    Y_Ritz.append(res2.subs({x: i}))
    Y_Collocation.append(res1.subs({x: i}))
    Y_Galerkin.append(res3.subs({x: i}))
    Y_decision.append(u.subs({x: i}))


plt.axes([0, 0, 1, 1])
plt.plot(X, Y_decision, "o-", label='Точное решение')
plt.plot(X, Y_Collocation, "r-", label='метод коллокации')
plt.plot(X, Y_Ritz, "k-", label="метод Ритца")
plt.plot(X, Y_Galerkin, "b-", label='метод Галеркина')
plt.legend()
plt.grid()
plt.show()

for i in range(n_x):
    print(Y_decision[i], Y_Collocation[i], Y_Ritz[i], Y_Galerkin[i])

print("Погрешности")
print("метод коллокации       метод Ритца      метод Галеркина")
for i in range(n_x):
    print(abs(Y_decision[i] - Y_Collocation[i]), abs(Y_decision[i] - Y_Ritz[i]), abs(Y_decision[i] - Y_Galerkin[i]))