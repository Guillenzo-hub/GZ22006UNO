import numpy as np

def gauss_jordan(A, b):
    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float).reshape(-1, 1)
    n = len(b)
    aug = np.hstack([A, b])

    for i in range(n):
        aug[i] = aug[i] / aug[i][i]
        for j in range(n):
            if i != j:
                aug[j] = aug[j] - aug[j][i] * aug[i]

    return aug[:, -1]
