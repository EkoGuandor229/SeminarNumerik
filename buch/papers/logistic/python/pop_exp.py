import numpy as np
import matplotlib.pyplot as plt

def logistic(r, x):
    return r * x

def plot(r, ax, x0):
    x = np.arange(0, 13, 1)
    y = np.ones_like(x) * x0
    for i in range(1, len(x)):
        y[i] = logistic(r, y[i-1])
    ax.plot(x, y, ".-", label=str("λ = "+str(r)), color="blue")
    ax.set_xlim(0, len(x)-1)
    ax.set_ylim(0, 1.0)
    ax.set_xticks(x[::2])
    ax.legend(loc="upper left")
    ax.set_xlabel("Jahr n")
    ax.grid()

fig, axs = plt.subplots(1,3,sharey=True,figsize=(9,3))
axs[0].set_ylabel("Population x")

plot(0.75, axs[0], 0.5)
plot(1.0, axs[1], 0.2)
plot(1.25, axs[2], 0.05)

plt.tight_layout()
plt.savefig("../figures/pop_exp.pdf")
plt.show()
