#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 16:25:13 2020

@author: midori
"""


import matplotlib.pyplot as plt
import numpy as np
import scipy.signal
from matplotlib.animation import FuncAnimation
from sspade import *
import math

def pade_coeffs(p,q):
    '''
    Calculate the numerator and denominator
    polynomial coefficients of the Pade
    approximation to e^-x
    '''
    n = max(p,q)
    c = 1
    d = 1
    clist = [c]
    dlist = [d]
    for k in range(1,n+1):
        c *= -1.0*(p-k+1)/(p+q-k+1)/k
        if k <= p:
            clist.append(c)
        d *= 1.0*(q-k+1)/(p+q-k+1)/k
        if k <= q:
            dlist.append(d)
    return np.array(clist[::-1]),np.array(dlist[::-1])


t = np.arange(0,3,0.001)
x = t
fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(1,1,1)
ax.set_xlabel('t')
ax.plot(t,t>=1,'--k')
#taylor = 1/(1 +x+x**2/2+x**3/2/3 + x**4 / math.factorial(4)+ x**5/math.factorial(5) + x**6/math.factorial(6)) 
taylor = [1,6,30,120,360,720,720]
tay = [720,0,0,0,0,0,0]
for q in [2,3]:
    for p in np.arange(1,q+1):
        pcoeffs, qcoeffs = pade_coeffs(p,q)
        P = np.poly1d(pcoeffs)
        Q = np.poly1d(qcoeffs)
        print(P)
        print(Q)
        H = scipy.signal.lti(P,Q)
        _,y = H.step(T=t)
        ax.plot(t,y,label='p=%d,q=%d' % (p,q))
        ax.legend(loc='best', labelspacing=0)
#<matplotlib.legend.Legend at 0x105479e10>
        plt.show()
print(pcoeffs, qcoeffs)

#H = scipy.signal.lti(taylor,tay)
#print(H)
#_,y = H.step(T=t)
#ax.plot(t,y,label="Taylor")
#ax.legend(loc='best', labelspacing=0)
plt.show()
plt.savefig("bilder/padelow{}{}.pdf".format(3,3))