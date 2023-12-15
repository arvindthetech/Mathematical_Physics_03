#Determine the nth roots of a complex number and represent it In Cartesian and polar form.

import cmath
a = float(input("Enter the real part(a):"))
b = float(input("Enter the imaginary part(b):"))
n = int(input("Enter the value of n:"))
z = complex(a,b)
r = abs(z)
theta = cmath.phase(z)

roots = []
for k in range(n):
        root_polar = cmath.rect(r ** (1/n), (theta + 2 * cmath.pi * k) / n)
        roots.append(root_polar)

for k, root_polar in enumerate(roots):
        root_cartesian = complex(root_polar.real, root_polar.imag)
        print(f"Root {k+1} (Cartesian): {root_cartesian}")
        print(f"Root {k+1} (Polar): {abs(root_polar):.2f} * (cos({cmath.phase(root_polar):.2f}) + i * sin({cmath.phase(root_polar):.2f}))")

