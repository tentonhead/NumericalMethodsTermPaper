import math

import numpy as np


ln = np.log
exp = np.exp


def f(x):
    y = 0.5*x + ln(x - 2) - 0.5
    return y

def df_dx(x):
    y = 0.5 + 1/(x-2)
    return y

def g(x):
    y = 2 + exp(0.5 - 0.5*x)
    #y = (0.5 - ln(x - 2))
    return y
