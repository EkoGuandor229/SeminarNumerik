#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 09:39:35 2020

@author: midori
"""
import matplotlib.pyplot as plt
import numpy as np
import scipy.signal
from matplotlib.animation import FuncAnimation
from sspade import *


def plotpolezero(z,p,L,M,ax=None):
    if ax is None:
        fig = plt.figure(figsize=(8,11))
        ax = fig.add_subplot(1,1,1, aspect='equal')
        #fig.tight_layout()
        ax.set_xlabel('Reale Achse',fontsize=16)
        ax.set_ylabel('Imaginäre Achse',fontsize=16)
    ax.grid(True)
    ax.plot(np.real(z),np.imag(z),'ok',markersize=3,mfc='none')
    ax.plot(np.real(p),np.imag(p),'xk',markersize=3, label='p={},q={}'.format(L,M))
    ax.legend(fontsize=14)
    return ax

ax=None
for q in [25,50,75,100,125,150,175,200]:
    pe = PadeExponential(q,q)
    zeros, poles, k = pe.zpk
    ax=plotpolezero(zeros,poles,q,q,ax)
plt.savefig("bilder/poles1.pdf")

ax=None  
for q in [10,20,30,40]:
    pe = PadeExponential(q,40)
    zeros, poles, k = pe.zpk
    ax=plotpolezero(zeros,poles,q,40,ax)
plt.savefig("bilder/poles2.pdf")
    
ax=None  
for p in [10,20,30,40]:
    pe = PadeExponential(40,p)
    zeros, poles, k = pe.zpk
    ax=plotpolezero(zeros,poles,40,p,ax)
plt.savefig("bilder/poles3.pdf")


ax=None 
de = PadeExponential(190,200)
zeros, poles, k = de.zpk
ax=plotpolezero(zeros,poles,190,200,ax)
plt.savefig("bilder/poles4.pdf")