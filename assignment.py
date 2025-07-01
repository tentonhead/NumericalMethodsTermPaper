import numpy as np


ln = np.log
exp = np.exp

counters = {"f":0, "f'":0, "g":0}
def reset(c):
    for key in c:
        c[key] = 0
    return c

def f(x):
    counters["f"] += 1
    y = 0.5*x + ln(x - 2) - 0.5
    return y

def df_dx(x):
    counters["f'"] += 1
    y = 0.5 + 1/(x-2)
    return y

def g(x):
    counters["g"] += 1
    y = 2 + exp(0.5 - 0.5*x)
    #y = (0.5 - ln(x - 2))
    return y

def e(x):
    return ["-"] + [abs(x[i] - x[i-1]) for i in range(1, len(x))]

def fmt(v, p):
    if isinstance(v, (float, int)):
        return f"{v:.{p}f}"
    return str(v)

class Table():
    def __init__(self, columns, labels, precision=3):
        self.data  = columns
        self.names = labels

        self.columns = len(self.data)
        self.rows    = len(self.data[0])
        self.precision = precision

    def print_tsv(self, file_name):
        header = ""
        for i in range(self.columns-1):
            h = self.names[i]
            header += h +'\t'
        header += self.names[-1] + '\n'

        rows = ""
        p = self.precision
        for r in range(self.rows):
            for c in range(self.columns-1):
                cell = self.data[c][r]
                rows += fmt(cell, p) + '\t'
            rows += fmt(self.data[-1][r], p) + '\n'
        body = header + rows
        file = open(file_name, "w")
        file.write(body)
        file.close()


