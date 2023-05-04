import numpy as np 
import matplotlib.pyplot as plt 
from scipy import constants as const
k = const.k
h = const.h
c = const.c
fig, (ax1,ax2) = plt.subplots(1,2)
x = np.linspace(0,12,100)
RJ = x*x 
ax1.plot(x,RJ,marker='.') 
ax1.set(xlabel=r"$x$", ylabel=r"$f_{RJ}(x)$",title=r"$f_{RJ}(x)$ vs x")
ax1.grid()
T = [6000,7500,9000]
for i in range(0,len(T)):
	sf = k*T[i]/h 
	e_star = k*T[i]
	l_star = h*c/e_star
	A = 8*np.pi*e_star/pow(l_star,3) 
	nu = sf*x 
	u = (A/sf)*RJ
	ax2.plot(nu,u,marker='.',label=f"{T[i]} K")
ax2.grid()
ax2.set(xlabel=r"$\nu$ (Hz)", ylabel=r"$u(\nu)$",title=r"$u(\nu)$ vs $\nu$ for Rayleigh Jeans law")
ax2.axvspan(4*pow(10,14),8*pow(10,14),facecolor='r', alpha=0.1,label="visible range")
ax2.legend()
plt.show()