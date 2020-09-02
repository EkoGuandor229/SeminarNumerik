#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 24 16:07:49 2020

@author: crenda
"""
import matplotlib.pyplot as plt
import numpy as np
import scipy.signal
from matplotlib.animation import FuncAnimation
from sspade import *


t = np.arange(0,2,0.001)
fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(1,1,1)
ax.set_xlabel('t')
ax.plot(t,t>=1,'--k')
for q in [20,60,80,120]:
    p = q#-4
    pe = PadeExponential(p,q)
    zeros, poles, k = pe.zpk
    H = pe.lti_sscascade
    _,y = scipy.signal.step2(H,T=t)
    ax.plot(t,y,label='p=%d, q=%d' % (p,q))
ax.grid('on')
ax.legend(loc='best', labelspacing=0)
ax.set_ylim(-0.1,1.1);
plt.savefig("bilder/padehigh1.pdf")

fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(1,1,1)
ax.set_xlabel('t')
ax.plot(t,t>=1,'--k')
for p in [200,190]:
    q= 200
    pe = PadeExponential(p,q)
    zeros, poles, k = pe.zpk
    H = pe.lti_sscascade
    _,y = scipy.signal.step2(H,T=t)
    ax.plot(t,y,label='p=%d, q=%d' % (p,q))
ax.grid('on')
ax.legend(loc='best', labelspacing=0)
ax.set_ylim(-0.1,1.1);
plt.savefig("bilder/padehigh2.pdf")
pe = PadeExponential(2,2)
print(PadeExponential(2,1))
print(pe.lti_sscascade)


# t = np.arange(0,2,0.001)
# fig = plt.figure(figsize=(10,6))
# ax = fig.add_subplot(1,1,1)
# ax.set_xlabel('t')
# ax.plot(t,t>=1,'--k')
# for q in [20,60,100]:
#     pe = PadeExponential(q,q)
#     zeros, poles, k = pe.zpk
#     H = pe.lti_sscascade
#     _,y = scipy.signal.step2(H,T=t)
#     ax.plot(t,y,label='p=q=%d' % q)
# ax.grid('on')
# ax.legend(loc='best', labelspacing=0)
# ax.set_ylim(-0.1,1.1);

# #<matplotlib.legend.Legend at 0x1087c7b10>
# a = 0.05  # 5% of the delay goes to Bessel, the rest to Pade
# n = 100   # order of the whole system
# m = 10    # order of the Bessel filter
# peb = Bessel(m,1.0/a)
# Hb = peb.lti_sscascade
# pe= PadeExponential(n-m,n-m,1/(1-a))
# Hp=pe.lti_sscascade
# H1 = cascade(Hb,Hp)
# # System #1: cascaded Bessel + Pade
# t = np.arange(0,2,0.001)

# # System #2: Pade only
# pe2=PadeExponential(n-m,n)
# H2=pe2.lti_sscascade
# # System #3: Bessel only
# H3=Bessel(n).lti_sscascade

# fig,ax=plt.subplots()
# xdata, ydata = [], []
# ln, = plt.plot([], [])
# ax=[fig.add_subplot(2,1,k+1) for k in range(2)]   

# # High Pade plots
# _,y = scipy.signal.step2(H2,T=t)

# plt.style.use("ggplot")

# plt.plot(t,y,label='Pade %d,%d' % (pe2.p,pe2.q))
# plt.legend()
# plt.savefig("bilder/pade.pdf")
# _,y = scipy.signal.step2(H1,T=t)
# plt.plot(t,y,label='bilder/Bessel %d $\\rightarrow$ Pade %d,%d.pdf' % (m,pe.p,pe.q),color="red")
# plt.legend()
# plt.savefig("bilder/PadeBessel.pdf")

# _,y = scipy.signal.step2(H3,T=t)
# plt.plot(t,y,label='bilder/Bessel %d.pdf' % n,color="magenta")
# plt.legend()
# plt.savefig("bilder/Bessel.png",dpi=1200)


##-------------------------------------------------------




# t = np.arange(0,3,0.001)
# fig = plt.figure(figsize=(10,6))
# ax = fig.add_subplot(1,1,1)
# ax.set_xlabel('t')
# ax.plot(t,t>=1,'--k')
# for q in [1,2,3]:
#     for p in np.arange(1,q+1):
#         pcoeffs, qcoeffs = pade_coeffs(p,q)
#         P = np.poly1d(pcoeffs)
#         Q = np.poly1d(qcoeffs)
#         H = scipy.signal.lti(P,Q)
#         _,y = H.step(T=t)
#         ax.plot(t,y,label='p=%d,q=%d' % (p,q))
#         ax.legend(loc='best', labelspacing=0)
# #<matplotlib.legend.Legend at 0x105479e10>
#         plt.show()
# plt.savefig("bilder/padelow{}{}.pdf".format(3,3))

##-----------------------------------------------------------




# for label, H in [
#                  ('Pade %d,%d' % (pe2.p,pe2.q), H2),
#                  ('Bessel %d $\\rightarrow$ Pade %d,%d' % (m,pe.p,pe.q), H1),
#                  ('Bessel %d' % n, H3)
#                 ]:
#     _,y = scipy.signal.step2(H,T=t)
#     #ax.plot(t,y,label=label)

    
   
#     def init():
#         ax.set_xlim(0.6,1.5)
#         ax.legend(loc='best')
#         ax.set_ylim(-0.1,1.1)
#         return ln,

#     def update(frame):
#         xdata.append(frame)
#         ydata.append(y(frame))
#         ln.set_data(xdata, ydata)
#         return ln,
#     ani = FuncAnimation(fig, update, frames=np.linspace(0, 2*np.pi, 128),
#                     init_func=init, blit=True)
#     plt.show()
#     ani.save("animation.mp4",fps=60,dpi=600)



    
# ax=[fig.add_subplot(2,1,k+1) for k in range(2)]
    
# for label, H in [
#                  ('Pade %d,%d' % (pe2.p,pe2.q), H2),
#                  ('Bessel %d $\\rightarrow$ Pade %d,%d' % (m,pe.p,pe.q), H1),
#                  ('Bessel %d' % n, H3)
#                 ]:
#     _,y = scipy.signal.step2(H,T=t)
#     for axk in ax: 
#         axk.plot(t,y,label=label)

# for k in range(2):
#     if k > 0:
#         axk.set_xlim(0.9,1.1)
#     ax[k].legend(loc='best')
#     ax[k].set_ylim(-0.1,1.1)