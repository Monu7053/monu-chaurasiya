import numpy as np 
import matplotlib.pyplot as plt 
from scipy import constants as const

l0 = pow(10,-10)
nu = np.logspace(10,30,100)
c = const.c 
G = np.pi*pow(2*l0/c,3)*pow(nu,2) 
fig, (ax1,ax2,ax3) = plt.subplots(1,3)
fig.suptitle("Plot is without dimension")
ax1.plot(nu,G,marker='.')
ax1.grid()
ax1.set(xlabel=r"$\nu$", ylabel=r"$G(\nu)$",title="For complete range of frequencies",xscale="log")
ax2.plot(np.log(nu),np.log(G),marker='.')
ax2.grid()
ax2.set(xlabel=r"$log_{10}(\nu)$", ylabel=r"$log_{10}G(\nu)$",title="For complete range of frequencies")
nu_visible = np.linspace(4*pow(10,14),8*pow(10,14),100)
G = np.pi*pow(2*l0/c,3)*pow(nu_visible,2)
ax3.plot(nu_visible,G,marker='.')
ax3.grid()
ax3.set(xlabel=r"$\nu$", ylabel=r"$G(\nu)$",title="For visible range of frequencies")
plt.show()