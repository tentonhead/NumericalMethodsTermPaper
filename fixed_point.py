import numpy as np


def fixed_point(g, x0, ε=1e-3, max_iter=100):
    x = [x0]
    for i in range(max_iter):
        x.append(0)
        x[i+1] = g(x[i])

        if abs(x[i+1] - x[i]) < ε:
            return np.array(x)

        x[i] = x[i+1]
    raise ValueError(f"Did not converge in {max_iter} iterations")
