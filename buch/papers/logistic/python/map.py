import numpy as np
import matplotlib.pyplot as plt

def logistic(r, x):
    return r * x * (1 - x)

n = 50000
r = np.linspace(0, 4.0, n)
x = np.ones(n) * 0.5

for i in range(0, 1000):
    x = logistic(r, x)

for i in range(0, 250):
    x = logistic(r, x)
    plt.plot(r, x, ',k', alpha=0.05)

fig = plt.gcf()
fig.set_size_inches(6.4, 3.8)

plt.xlim(0.0, 4.1)
plt.ylim(-0.025, 1.025)
plt.xlabel("λ")
plt.ylabel("$x_n$ wenn $n \\rightarrow \infty$")
plt.tight_layout()
plt.savefig("../figures/map.png", dpi=300)
