import numpy as np
from scipy import integrate

# Warnungen werden erzeugt, wenn mit der gewählten Anzahl
# Stützstellen die Toleranz  tol=1.49e-08 nicht erreicht werden kann

# Zu integrierende Funktion
func = lambda x: np.sqrt(1 - x ** 2)

# Anzahl Stützstellen
nodes = [2, 3, 4, 5, 6, 10, 20, 50, 100]

# Quadraturen mit node = Anzahl Stützstellen
for node in nodes:
    x = np.linspace(-1, 1, node)
    y = func(x)
    print(f"Number of nodes: {node}")
    # Berechnung mit Gauss-Quadratur
    print(f"Gauss-Legendre : {integrate.quadrature(func, -1, 1, maxiter=node)}")
    # Berechnung mit Trepezformel
    print(f"Trapezoidal Rule: {integrate.trapz(y, x)}")
    # Berechnung mit Simpsonscher Regel
    print(f"Simpson's Rule : {integrate.simps(y, x)}")
    print()

