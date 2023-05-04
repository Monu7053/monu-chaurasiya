import matplotlib.pyplot as plt 
import numpy as np 
import scipy.constants as const 

kB = const.Boltzmann 
e = const.e 

fig, (ax1,ax2,ax3) = plt.subplots(nrows=1,ncols=3)
fig.suptitle("Variation of distribution with energy, for different temperatures")

def fermi_dirac(e_energy,ef,T):
	fFD_arr = 1/(np.exp((e_energy-ef)/(kB*T))+1)
	return fFD_arr

ef = e # in Joules
e_energy = np.linspace(-5,5,1000) # in eV
e_energy = e_energy*e # in Joules
T = [10,100,1000,5000]
for i in range(0,len(T)):
	fFD_arr = fermi_dirac(e_energy,ef,T[i])
	ax1.plot(e_energy/e,fFD_arr,label=f"{T[i]} K")
ax1.grid()
ax1.set_xlabel(r"$\epsilon$ in eV")
ax1.set_ylabel(r"$f_{FD}$")
ax1.legend()
ax1.set_title("fermi_dirac")
#plt.show() 

def bose_einstein(e_energy,mu,T):
	fBE_arr = 1/(np.exp((e_energy-mu)/(kB*T))-1)
	return fBE_arr 

mu = e # in Joules
e_energy = np.linspace(mu*(1+pow(10,-3))/e,1.5,100000) # in eV
e_energy = e_energy*e # in Joules
T = [10,100,1000,5000]
for i in range(0,len(T)):
	fBE_arr = bose_einstein(e_energy,mu,T[i])
	ax2.plot(e_energy/e,fBE_arr,label=f"{T[i]} K")
ax2.grid()
ax2.set_xlabel(r"$\epsilon$ in eV")
ax2.set_ylabel(r"$f_{BE}$")
ax2.legend()
ax2.set_ylim(-5,100)
ax2.set_title("bose_einstein")
#plt.show() 

def maxwell_boltzmann(e_energy,T):
	fMB_arr = np.exp(-e_energy/(kB*T))
	return fMB_arr

ef = e # in Joules
e_energy = np.linspace(0,5,1000) # in eV
e_energy = e_energy*e # in Joules
T = [10,500,1000,5000]
for i in range(0,len(T)):
	fMB_arr = maxwell_boltzmann(e_energy,T[i])
	ax3.plot(e_energy/e,fMB_arr,label=f"{T[i]} K")
ax3.grid()
ax3.set_xlabel(r"$\epsilon$ in eV")
ax3.set_ylabel(r"$f_{MB}$")
ax3.legend()
ax3.set_title("maxwell_boltzmann")
plt.show() 
