import numpy as np
import matplotlib.pyplot as plt
from numpy import newaxis
import matplotlib.colors

left = -2.0
right = 1.0
top = 1.0
bottom = -1.0

x = np.linspace(left, right, 2000)
y = np.linspace(bottom, top, 2000)
c = x[:,newaxis] + 1j*y[newaxis,:]
z = c

for i in range(0, 75):
    z = z**2 + c
m = 1 - (abs(z) < 2)
cmap = matplotlib.colors.LinearSegmentedColormap.from_list("", [(0,0,0,1),(0,0,0,0)])
plt.imshow(m.T, extent=[left, right, bottom, top], cmap=cmap)

for i in range(0, 200):
    z = z**2 + c
m = 1 - (abs(z) < 2)
cmap = matplotlib.colors.LinearSegmentedColormap.from_list("", [(1,0,0,1),(0,0,0,0)])
plt.imshow(m.T, extent=[left, right, bottom, top], cmap=cmap)

plt.xlim(left-1, right+1)
plt.ylim(bottom, top)
plt.gca().set_aspect(1)
plt.grid(alpha=0.25, color="k")
plt.yticks(np.arange(bottom,top+0.5,0.5))
plt.xticks(np.arange(left-1,right+1+0.5,0.5))
plt.tight_layout()
plt.xlabel("Re(c)")
plt.ylabel("Im(c)")
plt.savefig("../figures/mandel.png", dpi=300, bbox_inches="tight")
