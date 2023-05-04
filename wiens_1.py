import numpy as np 
import matplotlib.pyplot as plt 
from scipy import constants as const
from scipy.integrate import quad
import pandas as pd
# (a) :
k = const.k
h = const.h
c = const.c
fig, (ax1) = plt.subplots(1,1)
x = np.linspace(pow(10,-5),12,10000)
P = (x*x*x)/(np.exp(x)-1)
for i in range(0,len(x)):
	if P[i] == max(P):
		xp = x[i]
def fp(x):
    return pow(x,3)/(np.exp(x) - 1)

for i in range(0,len(x)):
	Ip1, error = quad(fp, x[0], x[i])
	Ip2, error = quad(fp, x[i], np.inf)
	if round(Ip1,3) == round(Ip2,3):
		xm = x[i]
		break
for i in range(0,len(x)):
	if x[i] == xm :
		ym = P[i]
ax1.scatter([xm],[ym],c='k',marker='o',label='Median value')
ax1.text(xm,ym,f"({round(xm,2)},{round(ym,2)})")
ax1.plot(x,P,label=f"Maximizes at x = {round(xm,2)}") 
ax1.scatter([xp],max(P),marker="o",c='r',label='Peak value')
ax1.text(xp+0.03,max(P)+0.01,f"({round(xp,2)},{round(max(P),2)})")
ax1.set(xlabel=r"$x$", ylabel=r"$f_{P}(x)$",title=r"$f_{P}(x)$ vs x")
ax1.legend()
ax1.grid()
plt.show()

# # (b) :
bp = (h*c)/(k*xp)
bm = (h*c)/(k*xm)
print("\n \n=========================================================================== \n")
print("bp = (h*c)/(k*x_p) =",bp)
print("And, bm = (h*c)/(k*xm) =", bm)
T = np.arange(500,10000,1000)
lam_p = bp/T 
lam_m = bm/T
data = {"Temp (K)" : T, "λ_p (nm)" : np.round(pow(10,9)*lam_p,2), "λ_m (nm)" : np.round(pow(10,9)*lam_m,2)}
df = pd.DataFrame(data)
print(df)