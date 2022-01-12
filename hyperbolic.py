import numpy as np

def g(x, t):
    return 0

def phi(x):
    return 0

def psi(x):
    return 0

def gamma_0(t):
    return -t**2

def gamma_1(t):
    return 2 * (t**2)


epsilon = 10 ** -5

l = T = 1
M = N = 10
a = 0.5
h = l / N

U = np.zeros((N + 1, M + 1))

x = []
for i in range(N + 1):
    x_el = i * h
    x.append(x_el)

t = []
for i in range(M + 1):
    t_el = i * h
    t.append(t_el)


for m in range(M + 1):
    U[m][0] = phi(x[m])

for n in range(N + 1):
    U[0][n] = gamma_0(t[n])
    U[M][n] = gamma_1(t[n])

for m in range(1, M):
    U[m][1] = U[m][0] + h * psi(x[m])


Value_1 = 0
Value_2 = 1

while (np.abs(Value_2 - Value_1) >= epsilon):
    Value_1 = np.max(U)
    for m in range(1, M):
        for n in range(1, N):
            U[m][n + 1] = 2 * U[m][n] - U[m][n - 1] +\
                          (a**2) * (U[m - 1][n] - U[m][n] + U[m + 1][n]) + (h**2) * g(x[m], t[n])
    Value_2 = np.max(U)

for i in U:
      for j in i:
          print("{:4f}".format(j), end=" ")
      print()
