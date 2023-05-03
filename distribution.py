import matplotlib.pyplot as plt 
import numpy as np 

T = np.arange(0,101,1)
Cv_by_R_ = np.zeros(101)
Cv_by_R = Cv_by_R_ + 1
fig, ax = plt.subplots(2,2)
fig.suptitle("Specific Heat Laws")
ax[0,0].plot(T,Cv_by_R)
y1 = Cv_by_R
x1_ = T
x1 = x1_/max(x1_)
ax[0,0].set_xlabel("T (K)")
ax[0,0].set_ylabel(r"$\frac{C_V}{3R}$")
ax[0,0].set_title("Duolong-Petit Law")
ax[0,0].grid()

x = np.linspace(0,4,10000)
one_by_x = 1/x 
Cv_by_R = (one_by_x*one_by_x*np.exp(one_by_x))/((np.exp(one_by_x)-1)*(np.exp(one_by_x)-1))
ax[0,1].plot(x,Cv_by_R)
y2 = Cv_by_R
x2_ = x
x2 = x2_/max(x2_)
ax[0,1].set_xlabel(r"$\frac{T}{\theta_E}$")
ax[0,1].set_ylabel(r"$\frac{C_V}{3R}$")
ax[0,1].set_title("Einstein's Specific heat law")
ax[0,1].grid()


from scipy.integrate import quad

def function(n):
    return (np.exp(n)*(n**4))/((np.exp(n)-1)**2)
def integral(x):
    integral,error=quad(function,0,x)
    return integral
def Debye(x):
    return 3*(x**3)*integral(1/x)

x=np.linspace(0,10,10000)
Cv_by_3R=[]
for i in x:
    Cv_by_3R.append(Debye(i))
ax[1,0].plot(x,Cv_by_3R)
y3 = Cv_by_3R
x3_ = x
x3 = x3_/max(x3_)
ax[1,0].set_xlabel(r"$\frac{T}{\theta_D}$")
ax[1,0].set_ylabel(r"$\frac{C_V}{3R}$")
ax[1,0].set_title("Debye's Specific heat law")
ax[1,0].grid()

ax[1,1].plot(x1,y1,label="Duolong-Petit Model")
ax[1,1].plot(x2,y2,label="Einstein Model")
ax[1,1].plot(x3,y3,label="Debye Model")
ax[1,1].grid()
ax[1,1].set_xlabel("Dimensionless Temperature parameter")
ax[1,1].set_ylabel(r"$\frac{C_V}{3R}$")
ax[1,1].set_title("Superimposed")
ax[1,1].legend()
plt.show()
