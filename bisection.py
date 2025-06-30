import numpy as np
import matplotlib.pyplot as plt

#import labY as lab

from assignment import f

def bisection(f, l, r, ε=10**-3):
    counter = 0
    c = np.nan
    x = []

    while abs(r - l)/2 > ε:
        c = (l + r)/2
        x.append(c)
        #print(f"{counter} : {l} {c} {r}")
        counter += 1
        #print("f(l) =", f(l), "f(c) =", f(c))
        if (f(l)*f(c)) < 0:
            r = c
        if (f(l)*f(c)) > 0:
            l = c
        else:
             continue
    return x
