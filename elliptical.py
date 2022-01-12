import numpy as np

def g(x, y):
    return 0

def phi(x, y):
    return 4 * x + 3 * (y ** 2)


epsilon = 10 ** -5

a = b = 1
M = N = 10

h = a / N

U = np.zeros((N + 1, M + 1))

X = []
for i in range(N + 1):
    x = i * h
    X.append(x)

Y = []
for i in range(M + 1):
    y = i * h
    Y.append(y)


for m in range(M + 1):
    U[m][0] = phi(X[m], Y[0])
    U[m][N] = phi(X[m], Y[N])

for n in range(N + 1):
    U[0][n] = phi(X[0], Y[n])
    U[M][n] = phi(X[M], Y[n])


Value_1 = 0
Value_2 = 1

while (np.abs(Value_2 - Value_1) >= epsilon):
    Value_1 = np.max(U)
    for n in range(1, N):
        for m in range(1, M):
            U[n][m] = 0.25 * (U[n + 1][m] + U[n - 1][m]
                              + U[n][m + 1] + U[n][m - 1])
    Value_2 = np.max(U)

for i in U:
      for j in i:
          print("{:4f}".format(j), end=" ")
      print()
