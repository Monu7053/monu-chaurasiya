import matplotlib.pyplot as plt 
import numpy as np 
import scipy.constants as const 

kB = const.Boltzmann 
e = const.e 

fig, (ax1,ax2,ax3) = plt.subplots(nrows=1,ncols=3)
fig.suptitle("Variation of with temperature, for different energies, for each distribution function")

def fermi_dirac(e_energy,ef,T):
	fFD_arr = 1/(np.exp((e_energy-ef)/(kB*T))+1)
	return fFD_arr

ef = 0 # in Joules
T = np.linspace(0,500000,1000) # in T
e_energy = np.array([0.5,1,5,10]) # in eV
e_energy = e_energy*e # in Joules
for i in range(0,len(e_energy)):
	fFD_arr = fermi_dirac(e_energy[i],ef,T)
	ax1.plot(T,fFD_arr,label=f"{e_energy[i]/e} eV")
ax1.grid()
ax1.set_xlabel(r"$T$ in K")
ax1.set_ylabel(r"$f_{FD}$")
ax1.legend()
ax1.set_title("fermi_dirac")
#plt.show() 

def maxwell_boltzmann(e_energy,T):
	fMB_arr = 1/np.exp(e_energy/(kB*T))
	return fMB_arr 

mu = 0 # in Joules
T = np.linspace(0,500000,1000) # in T
e_energy = np.array([0.5,1,2.5,5]) # in eV
e_energy = e_energy*e # in Joules
for i in range(0,len(e_energy)):
	fMB_arr = maxwell_boltzmann(e_energy[i],T)
	ax2.plot(T,fMB_arr,label=f"{e_energy[i]/e} eV")
ax2.grid()
ax2.set_xlabel(r"$T$ in K")
ax2.set_ylabel(r"$f_{MB}$")
ax2.legend()
ax2.set_title("maxwell_boltzmann")
#plt.show() 

def bose_einstein(e_energy,mu,T):
	fBE_arr = 1/(np.exp((e_energy-mu)/(kB*T))-1)
	return fBE_arr 

mu = 0 # in Joules
T = np.linspace(0,50000,1000) # in T
e_energy = np.array([1,2.5,5]) # in eV
e_energy = e_energy*e # in Joules
for i in range(0,len(e_energy)):
	fBE_arr = bose_einstein(e_energy[i],mu,T)
	ax3.plot(T,fBE_arr,label=f"{e_energy[i]/e} eV")
ax3.grid()
ax3.set_xlabel(r"$T$ in K")
ax3.set_ylabel(r"$f_{BE}$")
ax3.legend()
ax3.set_title("bose_einstein")

plt.show()