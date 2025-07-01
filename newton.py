import numpy as np

from assignment import f


def newton(f, df_dx, x0, ε=1e-3, max_iter=100):
    x = [x0]
    for i in range(max_iter):
        x.append(0)
        x[i+1] = x[i] - f(x[i])/df_dx(x[i])

        if abs(x[i+1] - x[i]) < ε:
            return np.array(x)
    raise ValueError(f"Did not converge in {max_iter} iterations")

