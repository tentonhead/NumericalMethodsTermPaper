import sys

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

def e(x):
    return ["-"] + [abs(x[i] - x[i-1]) for i in range(1, len(x))]

class Table():
    def __init__(self, columns, labels):
        self.data  = columns
        self.names = labels

        self.columns = len(self.data)
        self.rows    = len(self.data[0])

    def print_tsv(self, file_name):
        header = ""
        for i in range(self.columns-1):
            h = self.names[i]
            header += h +'\t'
        header += self.names[-1] + '\n'

        rows = ""
        for r in range(self.rows):
            for c in range(self.columns-1):
                rows += str(self.data[c][r]) + '\t' 
            rows += str(self.data[-1][r]) + '\n'
        body = header + rows
        file = open(file_name, "w")
        file.write(body)
        file.close()


