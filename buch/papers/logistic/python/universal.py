import numpy as np
import matplotlib.pyplot as plt

def fcos(r, x):
    return r * np.cos(x)

def fcosh(r, x):
    return r*(2-np.cosh(x))

def plot(ax, f, n, m, xlim, ylim):
    r = np.linspace(*xlim, n)
    x = np.ones(n) * 0.1

    for i in range(0, 1000):
        x = f(r, x)

    for i in range(0, m):
        x = f(r, x)
        ax.plot(r, x, ',k', alpha=0.05)
    
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    ax.set_xlabel("$\lambda$")

fig, axs = plt.subplots(2,2,figsize=(6.4, 3.8))

plot(axs[0,1], fcos, xlim=(0, 6), ylim=(-6,6), n=20000, m=100)
plot(axs[1,1], fcosh, xlim=(0, 1.8), ylim=(-2,2), n=25000, m=100)

x = np.linspace(-2, 2, 1000)
y = fcos(1.0, x)
axs[0,0].plot([-10, 10], [0, 0], "-k", alpha=0.5)
axs[0,0].plot([0, 0], [-10, 10], "-k", alpha=0.5)
axs[0,0].plot(x, y, "-b", label="$\lambda \cdot cos(x)$ mit $\lambda=1.0$")
axs[0,0].legend(loc="upper left")
axs[0,0].grid()
axs[0,0].set_xlim(x[0], x[-1])
axs[0,0].set_ylim(-1, 2)
axs[0,0].set_xlabel("$x$")

x = np.linspace(-2, 2, 1000)
y = fcosh(1.0, x)
axs[1,0].plot([-10, 10], [0, 0], "-k", alpha=0.5)
axs[1,0].plot([0, 0], [-10, 10], "-k", alpha=0.5)
axs[1,0].plot(x, y, "-b", label="$\lambda \cdot (2-cosh(x))$ mit $\lambda=1.0$")
axs[1,0].legend(loc="upper left")
axs[1,0].grid()
axs[1,0].set_xlim(x[0], x[-1])
axs[1,0].set_ylim(-1, 2)
axs[1,0].set_xlabel("$x$")

plt.tight_layout()
plt.savefig("../figures/universal.png", dpi=300, bbox_inches="tight")
