import numpy as np
import matplotlib.pyplot as plt

def logistic(r, x):
    return r * x * (1-x)

def plot(r, ax, x0):
    x = np.arange(0, 37, 1)
    y = np.ones_like(x) * x0
    for i in range(1, len(x)):
        y[i] = logistic(r, y[i-1])
    ax.plot(x, y, "-", label=str("λ = "+str(r)), color="red")
    ax.set_xlim(0, len(x)-1)
    ax.set_ylim(0, 1.0)
    ax.set_xticks(x[::6])
    ax.legend(loc="lower right")
    ax.set_xlabel("Jahr n")
    ax.grid()

fig, axs = plt.subplots(1,3,sharey=True,figsize=(9,3))
axs[0].set_ylabel("Population x")

plot(2.9, axs[0], 0.1)
plot(3.35, axs[1], 0.1)
plot(3.55, axs[2], 0.1)

plt.tight_layout()
plt.savefig("../figures/pop_logistic_2.pdf")
plt.show()
