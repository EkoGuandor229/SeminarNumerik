import numpy as np
import matplotlib.pyplot as plt

def f(r, x):
    return x*r*(1 - x)
    
def g(r, x):
    return f(r, f(r, x))

def h(r, x):
    return f(r, f(r, f(r, x)))

def plot(r, ax, x0, fun, fun2, tangets, name):
    
    # plot web
    webx = np.zeros(1000)
    weby = np.zeros(1000)
    webx[0] = x0
    weby[0] = 0.0
    webx[1] = webx[0]
    weby[1] = fun2(r, webx[0])
    for i in range(2, len(webx), 2):
        webx[i] = weby[i-1]
        weby[i] = weby[i-1]
        webx[i+1] = webx[i]
        weby[i+1] = fun2(r, webx[i])
    ax.plot(webx, weby, "-r")

    # plot points and tangent lines
    if(tangets):
        x_n = np.zeros(10000)
        x_n[0] = x0
        for i in range(1, len(x_n)):
            x = x_n[i-1]
            x_n[i] = fun2(r, x)
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
            ya = fun(r, xa)
            yb = fun(r, xb)
            m = (yb-ya)/(xb-xa)
            print(px)
            a = np.arctan(m)
            tl = 0.24
            ax.plot([px-tl*np.cos(a), px+tl*np.cos(a)], [px-tl*np.sin(a), px+tl*np.sin(a)], "--", color="blue")
    
    # plot f(x)
    x = np.linspace(-1, 2.0, 1000)
    y = fun(r, x)
    ax.plot(x, y, "-b", label=str(name + " mit λ = "+str(r)))
    ax.plot([-1, 2], [-1, 2], "-k")
    
    ax.set_aspect(1)
    ax.set_xlim(-0.1, 1.1)
    ax.set_ylim(0.0, 1.25)
    ax.legend(loc="upper left")
    ax.grid()

fig, axs = plt.subplots(1,3,sharey=True,figsize=(9,3.5))


# plot f(x)
x = np.linspace(-1, 2.0, 1000)
y = f(3.35, x)
axs[1].plot(x, y, "-b", alpha = 0.4)
y = f(3.835, x)
axs[2].plot(x, y, "-b", alpha = 0.4)

plot(3.35, axs[0], 0.24, f, f, False, "f(x)")
plot(3.35, axs[1], 0.24, g, f, True, "f(f(x))")
plot(3.835, axs[2], 0.25, h, f, True, "f(f(f(x)))")

plt.tight_layout()
plt.savefig("../figures/web_2.pdf")
plt.show()
