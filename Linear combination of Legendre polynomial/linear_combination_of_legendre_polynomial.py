#Representation of a function as a linear combination of Legendre polynomial.

import numpy as np
from scipy.special import legendre

def legendre_poly(n, x):
    if n == 0:
        return np.ones_like(x)
    elif n == 1:
        return x
    else:
        Pnm2 = np.ones_like(x)
        Pnm1 = x
        for k in range(2, n + 1):
            Pn = ((2 * k - 1) * x *Pnm1 - (k - 1) * Pnm2) / k
            Pnm2, Pnm1 = Pnm1, Pn
        return Pn
    
def gauss_legendre_quadrature(f, a, b, degree):
    x, w = np.polynomial.legendre.leggauss(degree)

    x_scaled = 0.5 * (b - a) * 0.5 * (b + a)
    w_scaled = 0.5 * (b - a) * w

    integral = np.sum(w_scaled * f(x_scaled))
    return integral

def function_to_represent(x):
    return np.sin(x) 

a = -1
b = 1
degree = 5

coefficients = [gauss_legendre_quadrature(lambda x: function_to_represent(x) * legendre_poly(n, x), a, b, degree)
                for n in range(degree + 1)]

def integrate_with_legendre_poly(x):
    result = 0
    for n, coefficient in enumerate(coefficients):
        legendre_poly1 = legendre_poly(n, x)
        result += coefficient * legendre_poly1
    return result

result = gauss_legendre_quadrature(integrate_with_legendre_poly, a, b, degree)

print(f"Approximate integral of sin(x) using Legendre Polynomials:", result)