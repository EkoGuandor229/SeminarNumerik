import numpy as np
import matplotlib.pyplot as plt

def logistic(r, x):
    return r * x * (1-x)



def plot(r, ax, x0):
    x = np.arange(0, 13, 1)
    y = np.ones_like(x) * x0
    yexp = np.ones_like(x) * x0
    for i in range(1, len(x)):
        y[i] = logistic(r, y[i-1])
        yexp[i] = r*yexp[i-1]
    ax.plot(x, y, ".-", label=str("λ = "+str(r)), color="red")
    ax.plot(x, yexp, "--", color="blue", alpha=0.6)
    ax.set_xlim(0, len(x)-1)
    ax.set_ylim(0, 1.0)
    ax.set_xticks(x[::2])
    ax.legend(loc="upper left")
    ax.set_xlabel("Jahr n")
    ax.grid()

fig, axs = plt.subplots(1,3,sharey=True,figsize=(9,3))
axs[0].set_ylabel("Population x")

plot(0.8, axs[0], 0.5)
plot(1.8, axs[1], 0.025)
plot(2.8, axs[2], 0.025)

plt.tight_layout()
plt.savefig("../figures/pop_logistic.pdf")
plt.show()
