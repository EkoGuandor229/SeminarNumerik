import numpy as np
from scipy import integrate

# toleranz = 1.49e-08

func = lambda x: np.sqrt(1 - x ** 2)
nodes = [2, 3, 4, 5, 10, 20, 50, 100]
for node in nodes:
    x = np.linspace(-1, 1, node)
    y = func(x)
    print(f"Number of nodes: {node}")
    print(f"Gauss-Legendre : {integrate.quadrature(func, -1, 1, maxiter=node)}")
    print(f"Trapezoidal Rule: {integrate.trapz(y, x)}")
    print(f"Simpson's Rule : {integrate.simps(y, x)}")
    print()

