import numpy as np
import matplotlib.pyplot as plt

def f(r, x):
    return x*r*(1 - x)

def plot(r, ax, x0):
    
    # plot web
    webx = np.zeros(1000)
    weby = np.zeros(1000)
    webx[0] = x0
    weby[0] = 0.0
    webx[1] = webx[0]
    weby[1] = f(r, webx[0])
    for i in range(2, len(webx), 2):
        webx[i] = weby[i-1]
        weby[i] = weby[i-1]
        webx[i+1] = webx[i]
        weby[i+1] = f(r, webx[i])
    ax.plot(webx, weby, "-r")

    # plot points and tangent lines
    x_n = np.zeros(10000)
    x_n[0] = x0
    for i in range(1, len(x_n)):
        x = x_n[i-1]
        x_n[i] = x*r*(1 - x)
    period = 0
    y = x_n[-1]
    for i in range(1, 65):
        yy = x_n[len(x_n)-1-i]
        rel_err = 1-(yy/y if (y>yy) else y/yy)
        if(rel_err < 1E-6):
            yy2 = x_n[len(x_n)-1-i*2]
            rel_err2 = 1-(yy2/y if (y>yy2) else y/yy2)
            if(rel_err2 < 1E-6):
                yy3 = x_n[len(x_n)-1-i*3]
                rel_err3 = 1-(yy3/y if (y>yy3) else y/yy3)
                if(rel_err3 < 1E-6):
                    period = i
                    break
    points = x_n[-1-period:-1]
    ax.plot(points, points, "ob", markersize=3)
    for i in range(0, len(points)):
        px = points[i]
        xa = px-0.000001
        xb = px+0.000001
        ya = f(r, xa)
        yb = f(r, xb)
        m = (yb-ya)/(xb-xa)
        print(px)
        a = np.arctan(m)
        tl = 0.24
        ax.plot([px-tl*np.cos(a), px+tl*np.cos(a)], [px-tl*np.sin(a), px+tl*np.sin(a)], "--", color="blue")
    ax.set_aspect(1)
    
    # plot f(x)
    x = np.linspace(-1, 2.0, 1000)
    y = x*r*(1 - x)
    ax.plot(x, y, "-b", label=str("f(x) mit λ = "+str(r)))
    ax.plot([0, 1], [0, 1], "-k")
    
    ax.set_xlim(0.0, 1.0)
    ax.set_ylim(0.0, 1.0)
    ax.legend(loc="upper left")
    ax.grid()

fig, axs = plt.subplots(1,3,sharey=True,figsize=(9,3))

plot(0.8, axs[0], 0.3)
plot(1.8, axs[1], 0.3)
plot(2.8, axs[2], 0.3)

plt.tight_layout()
plt.savefig("../figures/web_1.pdf")
plt.show()
