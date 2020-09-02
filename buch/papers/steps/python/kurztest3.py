# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import sympy as sym
from scipy import integrate

import numpy as np
import matplotlib.pyplot as plt
import rungeKutta as rk

def f(x, y):
    return np.e**y


def euler(x_vec, func_deriv, y0):
    y=[]
    y.append(y0)
    for i in range(len(x_vec)-1):
        h=x[i+1]-x[i]
        k1=func_deriv(x[i], y[i])
        y.append(y[i]+h*k1)
    return y

def euler_improved(x_vec, func_deriv, y0):
    y=[]
    y.append(y0)
    for i in range(len(x_vec)-1):
        h=x[i+1]-x[i]
        k1=func_deriv(x[i], y[i])
        k2=func_deriv(x[i]+h/2, y[i]+h*k1/2)
        y.append(y[i]+h*k2)
    return y

def rk_simplyfied(x_vec, func_deriv, y0):
    y=[]
    y.append(y0)
    for i in range(len(x_vec)-1):
        h=x[i+1]-x[i]
        k1=func_deriv(x[i], y[i])
        k2=func_deriv(x[i]+h/2, y[i]+h*k1)
        y.append(y[i]+h/2*(k1+k2))
    return y

def rk_4(x_vec, func_deriv, y0):
    y=[]
    y.append(y0)
    for i in range(len(x_vec)-1):
        h=x[i+1]-x[i]
        k1=func_deriv(x[i], y[i])
        k2=func_deriv(x[i]+h/2, y[i]+h*k1/2)
        k3=func_deriv(x[i]+h/2, y[i]+h*k2/2)
        k4=func_deriv(x[i]+h, y[i]+h*k3)
        y.append(y[i]+h/6*(k1+2*k2+2*k3+k4))
    return y

#----k euler steps------------------------

plt.figure()
x=np.arange(0, 1, 1e-3)
plt.plot(x, np.log((-1)/(np.array(x)-1)), '--', c='#8F8F8F',label='analytisch')

k=[0,1,2, 8]
for k in k:
    x=[i/(2**k) for i in range(2**k+1)]
    y=euler(x, f, 0)
    print(f'{2**k} euler steps: y({x[-1]})={y[-1]}')
    plt.plot(x, y, '.-', label=f'numerisch, {2**k} Steps')




plt.ylim(0, 12)
plt.title("euler steps, $y'=e^y$, $y(0)=0$")
plt.legend()
plt.grid()
plt.tight_layout()

#----k euler_improved steps

plt.figure()
x=np.arange(0, 1, 1e-3)
plt.plot(x, np.log((-1)/(np.array(x)-1)), '--', c='#8F8F8F',label='analytisch')

k=[0,1,2, 8]
for k in k:
    x=[i/(2**k) for i in range(2**k+1)]
    y=euler_improved(x, f, 0)
    print(f'{2**k} euler_improved steps: y({x[-1]})={y[-1]}')
    plt.plot(x, y, '.-', label=f'numerisch, {2**k} Steps')

plt.ylim(0, 12)
plt.title("improved euler steps, $y'=e^y$, $y(0)=0$")
plt.legend()
plt.grid()
plt.tight_layout()

#----k runge-kutta-simpyfied steps------------------------

plt.figure()
x=np.arange(0, 1, 1e-3)
plt.plot(x, np.log((-1)/(np.array(x)-1)), '--', c='#8F8F8F',label='analytisch')

k=[0,1,2, 8]
for k in k:
    x=[i/(2**k) for i in range(2**k+1)]
    y=rk_simplyfied(x, f, 0)
    print(f'{2**k} runge-kutta-simpyfied: y({x[-1]})={y[-1]}')
    plt.plot(x, y, '.-', label=f'numerisch, {2**k} Steps')

plt.ylim(0, 12)
plt.title("runge-kutta-simpyfied, $y'=e^y$, $y(0)=0$")
plt.legend()
plt.grid()
plt.tight_layout()



#----k runge kutta steps------------------------

plt.figure()
x=np.arange(0, 1, 1e-3)
plt.plot(x, np.log((-1)/(np.array(x)-1)), '--', c='#8F8F8F',label='analytisch')

k=[0,1,2]
for k in k:
    x=[i/(2**k) for i in range(2**k+1)]
    y=rk_4(x, f, 0)
    print(f'{2**k} runge kutta steps: y({x[-1]})={y[-1]}')
    plt.plot(x, y, '.-', label=f'numerisch, {2**k} Steps')

plt.ylim(0, 12)
plt.title("runge kutta steps, $y'=e^y$, $y(0)=0$")
plt.legend()
plt.grid()
plt.tight_layout()

#------------y(1-10^(-k)) with lib---------------

plt.figure()
x=np.arange(0, 1, 1e-6)
plt.plot(x, np.log((-1)/(np.array(x)-1)), '--', c='#8F8F8F',label='analytisch')

k=[0,1,2,3,6]
for k in k:
    x=(0, (1-10**(-k)))
    y=integrate.solve_ivp(f, x, (0,))
    print(f'solve_ivp: y({y.t[-1]})={y.y[0][-1]}')
    plt.plot(y.t, y.y[0, :], '.-', label=f'numerisch, {len(y.t)-1} Steps')

plt.ylim(0, 12)
plt.title("scipy.integrate.solve_ivp, $y'=e^y$, $y(0)=0$")
plt.legend()
plt.grid()
plt.tight_layout()


#-----------variable-step-size-(own design)------------------------------
t, y=rk.rk_system_nd_ssc_fehlberg(0, [np.array([0])], 1, f, hmin=1e-6, hmax=2, epsilon=1e-6, hstart=0.2)
# t, y=rk.rk_system_nd(0, [np.array([0])], 2, f, 0.1) # 10 steps

x=np.arange(0, 1, 1e-6)
fig, (ax1, ax2)=plt.subplots(1,2, figsize=(8, 5))
ax1.plot(x, np.log((-1)/(np.array(x)-1)), '--', c='#8F8F8F',label='analytisch')
ax1.plot(t, [y[0,0] for y in y], '.-', label='numerisch', c=(0.8, 0.2, 0, .5))
ax1.set_ylim(0, 12)
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_title("$y'=e^y$, $y(0)=0$")
ax1.legend()
ax1.grid()

ax2.set_xlim(0, len(t)-2)
#ax2.set_ylim(1e-6, 1)
ax2.semilogy((np.r_[t, t[-1]]-np.r_[0, t])[1:], '-C1', drawstyle='steps-post')
ax2.plot([t[i+1]-t[i] for i in range(len(t)-1)], '.C1')
ax2.set_xlabel('Schritt n')
ax2.set_ylabel('Schrittweite')
ax2.grid(which="both")
ax2.set_title("Schrittweitenverlauf")
fig.tight_layout()
fig.savefig('test3.pdf')
