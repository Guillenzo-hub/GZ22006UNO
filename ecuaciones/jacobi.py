import numpy as np

def jacobi(A, b):
    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float)
    n = len(b)
    x0 = None
    tol = 1e-6
    max_iter = 1000


    if x0 is None:
        x0 = np.zeros(n)

    x = x0.copy()

    for it in range(max_iter):
        x_new = np.zeros_like(x)
        for i in range(n):
            s = sum(A[i][j] * x[j] for j in range(n) if j != i)
            x_new[i] = (b[i] - s) / A[i][i]
        if np.linalg.norm(x_new - x, ord=np.inf) < tol:
            return x_new
        x = x_new

    raise ValueError("El método de Jacobi no convergió en el número máximo de iteraciones.")
