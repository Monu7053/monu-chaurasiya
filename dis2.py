import matplotlib.pyplot as plt 
import numpy as np 

fig, (ax1, ax2) = plt.subplots(1,2)
fig.suptitle("Density of States")

y = np.zeros(101)
x = np.arange(0,101,1)
x0 = (x[0]+x[-1])/2
for i in range(0,len(y)):
	if x[i] == x0:
		y[i] = 1
ax1.plot(x,y)
ax1.set_ylabel(r"$\frac{G(\nu)}{N_Af}$")
ax1.set_xlabel(r"$\frac{\nu}{\nu_{\epsilon}}$")
ax1.set_title("DOS : Einstein's theory")
ax1.grid()

x = np.linspace(0,1,100)
y = x**2
ax2.plot(x,y)
ax2.set_ylabel(r"$\frac{G(\nu)}{N_Af}$")
ax2.set_xlabel(r"$\frac{\nu}{\nu_{\epsilon}}$")
ax2.set_title("DOS : Debye's theory")
ax2.grid()
plt.show()