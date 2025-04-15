import numpy as np

def descomposicion_lu(A, b):
    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float)
    n = len(A)

    L = np.zeros((n, n))
    U = np.zeros((n, n))

    for i in range(n):
        L[i][i] = 1
        for j in range(i, n):
            U[i][j] = A[i][j] - sum(L[i][k]*U[k][j] for k in range(i))
        for j in range(i+1, n):
            if U[i][i] == 0:
                raise ValueError("División por cero en la descomposición LU.")
            L[j][i] = (A[j][i] - sum(L[j][k]*U[k][i] for k in range(i))) / U[i][i]

    y = np.zeros(n)
    for i in range(n):
        y[i] = b[i] - sum(L[i][j]*y[j] for j in range(i))

    x = np.zeros(n)
    for i in reversed(range(n)):
        if U[i][i] == 0:
            raise ValueError("División por cero en la sustitución hacia atrás.")
        x[i] = (y[i] - sum(U[i][j]*x[j] for j in range(i+1, n))) / U[i][i]

    return x
