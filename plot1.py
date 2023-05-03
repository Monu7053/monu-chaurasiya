import matplotlib.pyplot as plt 
import numpy as np 
import scipy.constants as const

def fMB(x):
	A = 1
	fMB_arr = A*np.exp(-x)
	return fMB_arr

def fBE(x,alpha):
	fBE_arr = 1/(np.exp(x+alpha)-1)
	return fBE_arr

def fFD(x):
	alpha = 0
	fFD_arr = 1/(np.exp(x+alpha)+1)
	return fFD_arr

x = np.linspace(-5,5,100)

fMB_arr = fMB(x)
fig, ax = plt.subplots(nrows=2, ncols=2)
fig.suptitle("Various Distribution functions")

ax[0,0].plot(x,fMB_arr)
ax[0,0].grid()
ax[0,0].set_xlabel(r"$\frac{\epsilon}{k_BT}$")
ax[0,0].set_ylabel(r"$f_{MB}$")
ax[0,0].set_title("Maxwell Boltzmann Distribution")


alpha = -1
x_BE = np.linspace(-alpha+pow(10,-2),5,100)
fBE_arr = fBE(x_BE,alpha)
ax[1,0].plot(x_BE,fBE_arr)
ax[1,0].grid()
ax[1,0].set_xlabel(r"$\frac{\epsilon}{k_BT}$")
ax[1,0].set_ylabel(r"$f_{BE}$")
ax[1,0].set_title("Bose Einstein Distribution")

fFD_arr = fFD(x)
ax[0,1].plot(x,fFD_arr)
ax[0,1].grid()
ax[0,1].set_xlabel(r"$\frac{\epsilon}{k_BT}$")
ax[0,1].set_ylabel(r"$f_{FD}$")
ax[0,1].set_title("Fermi Dirac Distribution")

# norm1 = max(fMB_arr)
# fMB_arr = fMB_arr/norm1
# norm2 = max(fBE_arr)
# fBE_arr = fBE_arr/norm2
ax[1,1].plot(x,fMB_arr,label="Maxwell Boltzmann")
ax[1,1].plot(x_BE,fBE_arr,label="Bose Einstein")
ax[1,1].plot(x,fFD_arr,label="Fermi Dirac")
ax[1,1].set_xlabel(r"$\frac{\epsilon}{k_BT}$")
ax[1,1].set_ylabel(r"$f$")
ax[1,1].legend()
ax[1,1].grid()
ax[1,1].set_title("All Distributions")
plt.show()

