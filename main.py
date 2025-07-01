import numpy as np

from assignment import f, df_dx, g, e, Table, counters, reset
from bisection import bisection
from secant import secant
from newton import newton
from fixed_point import fixed_point


if __name__ == '__main__':
    print("Hi, Term Paper!")
    l, r = 2.1, 3.0
    x0 = 2.5
    ε  = 1e-6

    x_bisection   = bisection(f, l, r, ε)
    print(counters)
    counters = reset(counters)
    x_secant      = secant(f, df_dx, x0, ε)
    print(counters)
    counters = reset(counters)
    x_newton      = newton(f, df_dx, x0, ε)
    print(counters)
    counters = reset(counters)
    x_fixed_point = fixed_point(g, x0, ε)
    print(counters)

    methods_names = ["bisection", "secant", "Newton", "fixed_point"]
    x = [x_bisection, x_secant, x_fixed_point, x_newton] 

    for i in range(4):
        print(f"Hi, {methods_names[i]}'s method!")
        print(len(x[i]), x[i][-1])
        xi = x[i]
        yi = f(xi)
        ki = np.arange(len(xi))
        εi = e(xi)
        ti = Table([ki, xi, εi, yi],
                   ["k", "x", "|x_k - x_k-1|", "f(x_k)"], precision=7)
        ti.print_tsv(methods_names[i]+".tsv")
