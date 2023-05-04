import numpy as np 
import matplotlib.pyplot as plt 
from scipy import constants as const
from scipy.integrate import quad
from scipy.stats import linregress

k = const.k
h = const.h
c = const.c

def fp(x):
    return pow(x,3)/(np.exp(x) - 1)
Ip, error = quad(fp, 0, np.inf)
print("\n =========================================================================== \n")
print("The result of the integration is:", Ip) 
print("Value of (π^4)/15 is :",pow(np.pi,4)/15)
for i in range(0,13):
	if round(Ip,13-i) == round(pow(np.pi,4)/15,13-i):
		print(f"They are equal upto {10-i} decimal places")
		break
def C(T):
	return 8*np.pi*pow(k*T,4)/pow(h*c,3)

T = np.arange(100,10000,500)
CT = C(T)
FT = Ip*(c/4)*CT
fig, (ax1,ax2) = plt.subplots(1,2) 
ax1.plot(T,FT)
ax1.set(xlabel=r"$T$",ylabel=r"$F$",title=r"$T$ vs $F$")
ax1.grid()

lnT = np.log(T)
lnF = np.log(FT)
ax2.scatter(lnT,lnF,marker='.',c='k')
ax2.set(xlabel=r"$\lnT$",ylabel=r"$\lnF$",title=r"$\lnT$ vs $\lnF$")
ax2.grid()

result = linregress(lnT,lnF)
ax2.scatter([0],[result[1]],c='r',label='intercept')
σ1 = np.exp(result[1])
print("Value of σ from the graph, using the intercept :",σ1)
σ2 = (2*pow(np.pi,5)*pow(k,4))/(15*pow(h,3)*pow(c,2))
print("Value of σ using the value of constants :",σ2)
for i in range(0,25):
	if round(σ1,25-i) == round(σ2,25-i):
		print(f"They are equal upto {25-i} decimal places")
		break
x_arr = np.linspace(0,lnT[-1],100)
y_arr = result[0]*x_arr + result[1]
ax2.plot(x_arr,y_arr)
plt.show()