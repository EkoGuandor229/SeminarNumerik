import numpy as np
import matplotlib.pyplot as plt

def logistic(r, x):
    return r * x * (1 - x)

def plot(ax, n, loops, box):
    rs = np.linspace(box["left"], box["right"], n)
    x = np.ones(n) * 0.5
    for i in range(0, loops[0]):
        x = logistic(rs, x)
    for i in range(0, loops[1]):
        x = logistic(rs, x)
        ax.plot(rs, x, ',k', alpha=0.05)

    ax.set_xlim(box["left"], box["right"])
    ax.set_ylim(box["bottom"], box["top"])
    ax.set_xlabel("$\lambda$")
    
fig, axs = plt.subplots(1,3,figsize=(9,3))

boxes = [
    {"left": 2.9, "right": 4.0, "bottom": 0.0,  "top": 1.0},
    {"left": 3.425, "right": 3.625, "bottom": 0.84-0.5*0.2/1.25,  "top": 0.84+0.5*0.2/1.4},
    # {"left": 3.75, "right": 3.9, "bottom": 0, "top": 1},
    {"left": 3.81, "right": 3.87, "bottom": 0.95-0.5*0.06/1.25,  "top": 0.95+0.5*0.06/1.4},
]

plot(axs[0], n=15000, loops=(1000,250), box=boxes[0])
plot(axs[1], n=30000, loops=(1000,250), box=boxes[1])
plot(axs[2], n=45000, loops=(1000,250), box=boxes[2])

axs[0].set_ylabel("$x_n$ wenn $n \\rightarrow \infty$")

def boxify(box):
    x = [box["left"], box["left"], box["right"], box["right"], box["left"]]
    y = [box["top"], box["bottom"], box["bottom"], box["top"], box["top"]]
    return (x, y)

x1, y1 = boxify(boxes[1])
x2, y2 = boxify(boxes[2])

axs[0].plot(x1, y1, "-r", linewidth=1)
axs[0].plot(x2, y2, "-r", linewidth=1)
plt.setp(axs[1].spines.values(), color="red")
plt.setp(axs[2].spines.values(), color="red")

plt.tight_layout()
plt.savefig("../figures/map_zoom.png", dpi=300)