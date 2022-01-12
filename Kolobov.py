import numpy as np

a = -1
b = 1

gamma_1 = 0
gamma_2 = 0

alfa_1 = 1
alfa_2 = 1

beta_1 = 0
beta_2 = 0

n = 4
k = 4

h = []
for i in range(k + 1):
    h.append((b - a) / k)

X = []
for i in range(k + 1):
    x = a + h[i] * i
    X.append(x)

def q(i):
    return(1 + X[i]**2)

def f(i):
    return -1

def mu(k):
    return h[k - 1] / (h[k] + h[k - 1])

A = np.zeros((k - 1))
B = np.zeros((k - 1))
C = np.zeros((k - 1))
F = np.zeros((k - 1))


V = np.ones((k + 1))

zn = (alfa_1 * h[0] - beta_1 * (1 - 1/3 * q(0) * h[0]**2))
if zn != 0:
    V[0] = (gamma_1 * h[0] + 1/6 * beta_1 * h[0]**2 * (2*f(0) + f(1))) / (alfa_1 * h[0] - beta_1 * (1 - 1/3 * q(0) * h[0]**2))

zn = (alfa_2 * h[n - 1] - beta_2 * (1 - 1/3 * q(n) * h[n - 1]**2))
if zn != 0:
    V[k] = (gamma_2 * h[n - 1] + 1/6 * beta_2 * h[n - 1]**2 * (f(n - 1) + 2*f(n))) / (alfa_2 * h[n - 1] - beta_2 * (1 - 1/3 * q(n) * h[n - 1]**2))

zn = (beta_1 * (1 + 1/6 * q(1) * h[0]**2))
if zn != 0:
    V[1] = (gamma_1 * h[0] + 1/6 * beta_1 * h[0]**2 * (2*f(0) + f(1))) / (beta_1 * (1 + 1/6 * q(1) * h[0]**2))

zn = (beta_2 * (-1 - 1/6 * q(n - 1) * h[n - 1]**2))
if zn != 0:
    V[1] = (gamma_1 * h[0] + 1 / 6 * beta_1 * h[0] ** 2 * (2 * f(0) + f(1))) / (beta_2 * (-1 - 1/6 * q(n - 1) * h[n - 1]**2))

for i in range(1, n):
    A[i - 1] = (1 - mu(i)) * (1 + (h[i - 1]) ** 2 / 6 * q(i - 1)) * V[i - 1]
    B[i - 1] = - (1 - h[i - 1]*h[i]/3 * q(i)) * V[i]
    C[i - 1] = mu(i) * (1 + h[i] ** 2 / 6 * q(i + 1)) * V[i + 1]
    F[i - 1] = (h[i - 1] * h[i])/6 * (mu(i) * f(i - 1) + 2 * f(i) + (1 - mu(i)) * f(i + 1))

def progonka(n, A, B, C, F):
    N = n - 1
    alpha = np.zeros((n))
    beta = np.zeros((n))

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
    print(' '.join([str(round(i, 2)) for i in U]))


progonka(n - 1, A, B, C, F)

