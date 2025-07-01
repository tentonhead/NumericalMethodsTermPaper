import numpy as np

from assignment import f

def bisection(f, l, r, ε=10**-3):
    counter = 0
    c = np.nan
    x = []

    while abs(r - l)/2 > ε:
        c = (l + r)/2
        x.append(c)
        counter += 1
        if (f(l)*f(c)) < 0:
            r = c
        if (f(l)*f(c)) > 0:
            l = c
        else:
             continue
    return np.array(x)
