#Solving a definite integral by gauss legendre quadrature method. Application representation of a function as linear combination legendre polynomial.

import numpy as np
import matplotlib.pyplot as plt
from scipy.special import legendre

#define the intervel for which you want to plot the legendre polynomial

x_min = -1.0
x_max = 1.0

#create an array of x-value with in interval

x = np.linspace(x_min,x_max,1000)

#plot the cos(x)
plt.figure(figsize=(10,5))
plt.plot(x,np.cos(x),label="cos(x)",linewidth=2)

#choose the degree of gauss-legendre quadrature
degree = 4

#calculate the node(x) and weights(w)using numpy for the intervel [-1.1]
x_guass,w = np.polynomial.legendre.leggauss(degree)

#define the function to be integrate(cos(x))
def function_to_integrate(x):
    return np.cos(x)

#calculate the integral using guass legendre quadrature

integral = sum(w*function_to_integrate(x_guass))

print(f"Approximate integral of cos(x) over [-1,1]:{integral}")

#plot the legendre polynomials
num_polynomial = 5

for i in range(num_polynomial):
    legendre_poly = legendre(i)
    plt.plot(x,legendre_poly(x),label=f"legendre{i}(x)")

plt.title("Legendre Polynomial vs cos(x)")
plt.xlabel("x")
plt.legend()
plt.grid(True)
plt.show()