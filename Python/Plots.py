import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon


def func(x):
    return np.sqrt(1 - x ** 2)


a, b = -1, 1  # integral limits
x = np.linspace(-1, 1, 1000)
y = func(x)

fig = plt.figure()
ax1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
ax1.plot(x, y, 'r', linewidth=2)
ax1.set_title(r"$I = \int_{-1}^{1}\sqrt{(1-x^2)}\,dx$")
ax1.spines["top"].set_visible(False)
ax1.spines["right"].set_visible(False)
ax1.text(0.0, -0.15, "$x$")
ax1.text(-1.3, 0.5, "$y$")
# ax1.fill_between(x, y, where=None, interpolate=False, facecolor="grey")
xpos = [0.661209386, -0.6612093865, -0.2386191861, 0.2386191861, -0.9324695142, 0.9324695142]
for pos in xpos:
    ax1.vlines(pos, ymin=0, ymax=func(pos), linestyles="--")

plt.show()
