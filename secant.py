import numpy as np
import matplotlib.pyplot as plt

import labY as lab

from assignment import f, df_dx
from newton import newton


def secant(f, df_dx, x0, ε=1e-3, max_iter=100):
    x1 = x0 - f(x0)/df_dx(x0)
    x = [x0, x1]
    for i in range(1, max_iter):
        x.append(0)
        x[i+1] = x[i] - (f(x[i])*(x[i] - x[i-1]))/(f(x[i]) - f(x[i-1]))

        if abs(x[i+1] - x[i]) < ε:
            break
    return x
