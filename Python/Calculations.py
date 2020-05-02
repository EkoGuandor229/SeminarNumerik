import numpy as np
from scipy import integrate

func = lambda x: np.sqrt(1 - x ** 2)
intervals = [2, 3, 4, 5, 10, 100, 1000, 10000]

for interval in intervals:
    x = np.linspace(-1, 1, num=interval)
    y = func(x)
    solution = integrate.simps(y, x)
    print(solution)

print()
for i in range(0, 100):
    print(str(i) + ": " + str(integrate.quadrature(func, -1, 1, maxiter=i)))
