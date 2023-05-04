import numpy as np 
import matplotlib.pyplot as plt 
from scipy import constants as const
k = const.k
h = const.h
c = const.c
fig, (ax1,ax2) = plt.subplots(1,2)
x = np.linspace(pow(10,-5),12,1000)
P = (x*x*x)/(np.exp(x)-1)
for i in range(0,len(x)):
	if P[i] == max(P):
		maxval = x[i]
ax1.plot(x,P,marker='.',label=f"Maximizes at x = {round(maxval,2)}") 
ax1.set(xlabel=r"$x$", ylabel=r"$f_{P}(x)$",title=r"$f_{P}(x)$ vs x")
ax1.legend()
ax1.grid()
print((h*c)/(k*maxval))
T = [6000,7500,9000]
for i in range(0,len(T)):
	sf = k*T[i]/h 
	e_star = k*T[i]
	l_star = h*c/e_star
	A = 8*np.pi*e_star/pow(l_star,3) 
	nu = sf*x 
	u = (A/sf)*P
	for j in range(0,len(nu)):
		if u[j] == max(u):
			maxval = nu[j]
	ax2.plot(nu,u,marker='.',label=f"{T[i]} K, maximizes at {round(maxval/pow(10,12),2)} THz")
ax2.grid()
ax2.set(xlabel=r"$\nu$ (Hz)", ylabel=r"$u(\nu)$",title=r"$u(\nu)$ vs $\nu$ for Planck's Radiation Law")
ax2.axvspan(4*pow(10,14),8*pow(10,14),facecolor='r', alpha=0.1,label="visible range")
ax2.legend()
plt.show()