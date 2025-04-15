import numpy as np

def cramer(A, b):
    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float)
    detA = np.linalg.det(A)
    if detA == 0:
        raise ValueError("El sistema no tiene solución única.")
    n = len(b)
    x = np.zeros(n)
    for i in range(n):
        Ai = A.copy()
        Ai[:, i] = b
        x[i] = np.linalg.det(Ai) / detA
    return x
