#Computation of Discrete Fourier Transform (DFT) using complex numbers.

import numpy as np

def compute_dft(x):
    N = len(x)
    X = np.zeros(N, dtype = complex)
    for k in range(N):
        X[k] = sum(x[n]*np.exp(-2j * np.pi *k * n /N)
                   for n in range(N))
        return X
x = np.array([11, 2, 3, 4]) #Replace this with your input signal
X = compute_dft(x)
print("DFT Result:", X)