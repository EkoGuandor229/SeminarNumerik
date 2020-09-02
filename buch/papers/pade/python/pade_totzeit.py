#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 21:53:04 2020

@author: midori
"""
import matplotlib.pyplot as plt
import numpy as np
import math


fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(1,1,1)
x = np.arange(-6,6,0.0005)
ax.semilogy(x,np.exp(-x),'--',label='e^-x')
ax.grid('on')

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

def argbox(y,ymin,ymax,imin,imax):
    ''' 
    find limits (we hope)
    where y[i] is between ymin and ymax 
    '''
    ii = np.argwhere(np.logical_and(y>ymin,y<ymax))
    ii = ii[ii >= imin]
    ii = ii[ii <= imax]
    return np.min(ii),np.max(ii)

nx = len(x)
xmin = min(x)
xmax = max(x)
xlim = (xmin,xmax)
ylim = (1e-5,1e5)
taylor = 1/(1 +x+x**2/2+x**3/2/3 + x**4 / math.factorial(4)+ x**5/math.factorial(5) + x**6/math.factorial(6)) 
for p in [1,2,3]:
    for q in [1,2,3]:
        pcoeffs, qcoeffs = pade_coeffs(p,q)
        P = np.poly1d(pcoeffs)
        Q = np.poly1d(qcoeffs)
        num = P(x)
        den = Q(x)
        wert = num/den
        for i in range(len(wert)):
            if i < len(wert)/2:
                if wert[i]<10**-5:
                    wert[i] = 10**5
            else:
                if wert[i]>10**5:
                    wert[i] = 10**-5
            
                    
        #wert[wert<10**-5]=10**5
        ax.semilogy(x,wert,label='P=%d, Q=%d' % (p,q))
        # now label the end lines
        it = argbox(wert, ylim[0], ylim[1], 0, nx/2)[0]
        atend = it == 0
        xt = x[it] * (0.99 if atend else 1)
        yt = P(xt)/Q(xt) if atend else ylim[1]*0.95
        ax.text(xt,yt,' (%d,%d)' % (p,q), va='top',
                rotation='horizontal' if atend else -90.0)
        it = argbox(wert, ylim[0], ylim[1], nx/2, nx)[1]
        atend = it == (nx-1)
        xt = x[it] * (0.99 if atend else 1)
        yt = P(xt)/Q(xt) if atend else ylim[0]*1.2
        ax.text(xt,yt,'(%d,%d)' % (p,q), va='bottom',
                ha='right' if atend else 'left',
                rotation='horizontal' if atend else -90.0)
ax.text(-5,0.03,'Taylor 6.er Ordnung', va='bottom',
                ha='right' if atend else 'left',
                rotation=30.0)
ax.semilogy(x,taylor,label='Taylor n=6')
ax.set_xlim(xlim)
ax.set_ylim(ylim)
ax.set_xlabel('x')
ax.set_ylabel('y = f(x)')
ax.legend(labelspacing=0)
plt.savefig("bilder/totzeit.pdf")
#<matplotlib.legend.Legend at 0x107935810>