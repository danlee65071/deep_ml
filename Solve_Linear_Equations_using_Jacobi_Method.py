import numpy as np


def solve_jacobi(A: np.ndarray, b: np.ndarray, n: int) -> list:
    diag_A = np.diag(A)
    not_diag_A = A - np.diag(diag_A)
    x = np.zeros(len(b))
    x_hold = np.zeros(len(b))
    for _ in range(n):
        for i in range(A.shape[0]):
            x_hold[i] = (1 / diag_A[i]) * (b[i] - sum(not_diag_A[i] * x))
        x = x_hold.copy()
    return np.round(x, 4).tolist()


A = np.array([[5, -2, 3], [-3, 9, 1], [2, -1, -7]])
b = np.array([-1, 2, 3])
n = 2
print(solve_jacobi(A, b, n))
