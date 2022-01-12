import numpy as np
import matplotlib.pyplot as plt

a = 0
b = 1

alpha_1 = 1
alpha_2 = 1

beta_1 = 0
beta_2 = 0

gamma_1 = 1
gamma_2 = np.exp(1) + 1

n = 4
k = n + 1

h = (b - a) / n

def q(i):
    return -1

def f(i):
    return -X[i]

def u(x):
    return x + np.exp(x)

def progonka(n, A, B, C, F):
    alpha = np.zeros((n))
    beta = np.zeros((n))
    N = n - 1

    alpha[1] = -C[0] / B[0]
    beta[1] = F[0] / B[0]

    for k in range(1, n - 1):
        alpha[k + 1] = -C[k] / (B[k] + A[k] * alpha[k])

    for k in range(1, n - 1):
        beta[k + 1] = (F[k] - A[k] * beta[k]) / (B[k] + A[k] * alpha[k])

    U = np.zeros((n))
    U[N] = (F[N] - A[N] * beta[N]) / (A[N] * alpha[N] + B[N])

    for k in range(N - 1, -1, -1):
        U[k] = alpha[k + 1] * U[k + 1] + beta[k + 1]

    return U

X = []
for i in range(k):
    X.append(a + h * i)

A = np.zeros((n - 1))
B = np.zeros((n - 1))
C = np.zeros((n - 1))
F = np.zeros((n - 1))

v = np.ones((k))

if alpha_1 != 0 or beta_1 != 0:
    v[0] = (2 * gamma_1 * h + 1/3 * beta_1 * h**2 * (2 * f(0) + f(1))) / \
           (2 * alpha_1 * h - beta_1 * (2 - 2 / 3 * q(0) * h**2))

if beta_1 != 0:
    v[1] = (2 * gamma_1 * h + 1/3 * beta_1 * h**2 * (2 * f(0) + f(1))) /\
           (beta_1 * (2 + 1/3 * q(1) * h**2))

if alpha_2 != 0 or beta_2 != 0:
    v[n] = (2 * gamma_2 * h + 1/3 * beta_2 * h**2 * (f(n - 1) + 2 * f(n))) / \
      (2 * alpha_2 * h - beta_2 * (2 - 2 / 3 * q(n) * h**2))

if beta_2 != 0:
    v[n - 1] = (2 * gamma_1 * h + 1 / 3 * beta_1 * h**2 * (2 * f(0) + f(1))) /\
               (beta_2 * (-2 - 1/3 * q(n - 1) * h**2))


for i in range(1, k - 1):
    A[i - 1] = (1 + (h**2)/6 * q(i - 1)) * v[i - 1]
    B[i - 1] = (2 * (h**2)/3 * q(i) - 2) * v[i]
    C[i - 1] = (1 + (h**2)/6 * q(i + 1)) * v[i + 1]


for i in range(1, k - 1):
    F[i - 1] = (h**2)/6 * (f(i - 1) + 4*f(i) + f(i + 1))

if gamma_1 != 0:
    F[0] = F[0] - A[0]
    A[0] = 0

if gamma_2 != 0:
    F[k - 3] = F[k - 3] - C[k - 3]
    C[k - 3] = 0

print(A)
print(B)
print(C)
print(F)

# if beta_1 != 0:
#     F[0] = F[0] - A[0]
#     A[0] = 0
#
# if beta_2 != 0:
#     F[k - 4] = F[k - 4] - C[k - 4]
#     C[k - 4] = 0


V = progonka(n - 1, A, B, C, F)

for i in range(1, k - 1):
    v[i] = V[i - 1]

Y_decision = []
for i in X:
    Y_decision.append(u(i))

# print(v)
# print(Y_decision)
# for i in range(n + 1):
#     print(np.abs(Y_decision[i] - v[i]))

# plt.plot(X, Y_decision, "o-", label="точное решение")
# plt.plot(X, v, "k-", label="программное решение")
# plt.legend()
# plt.grid()
# plt.show()