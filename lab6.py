import numpy as np
import matplotlib.pyplot as plt

k=8.617*10**(-5)
g=[1,1,1]
e=[0,1,2]

def part_function(g,e,t):
    value=[]
    for i in range(len(e)):
        temp=g[i]*np.exp((-e[i])/(k*t))
        value.append(temp)
    return sum(value)
    
t_1=np.linspace(0.1,5000,50)
t_2=np.linspace(5000,10**5,50)

z_low=[]
for i in t_1:
    z_low.append(part_function(g,e,i))
plt.plot(t_1,z_low , label="Low temperature")
plt.xlabel("Temperature")
plt.ylabel("Z")
plt.legend()
plt.title("Partition Function")
plt.grid()
plt.show()

z_high=[]
for i in t_2:
    z_high.append(part_function(g,e,i))
plt.plot(t_2,z_high,label="High temperature")
plt.xlabel("Temperature")
plt.ylabel("Z")
plt.grid()
plt.legend()
plt.title("Partition Function")
plt.show() 

def Frac_population(g,z,e,t):
    N = []
    for i in range(len(t)):
        n = (g*np.exp(-e/(k*t[i])))/z[i]
        N.append(n)
    return N
for i in range(len(e)):
    plt.plot(t_1,Frac_population(g[i],z_low,e[i],t_1) , label="state= "+str(i))
plt.xlabel("Temperature")
plt.ylabel("N_0/N")
plt.grid()
plt.legend()
plt.title("Fractional Population(Low Temperature)")
plt.show()

for i in range(len(e)):
    plt.plot(t_2,Frac_population(g[i],z_high,e[i],t_2) , label="state="+str(i))
plt.xlabel("Temperature")
plt.ylabel("N_0/N")
plt.grid()
plt.legend()
plt.title("Fractional Population(High Temperautre)")
plt.show()


def Total_Energy(g,e,z,t):
    value = []
    for i in range(len(e)):
        u = (g[i]*e[i]*np.exp(-e[i]/(k*t)))/(z)
        value.append(u)
    return sum(value)

u_1=[]
u_2=[]
for i in range(len(t_1)):
    u_1.append(Total_Energy(g,e,z_low[i],t_1[i]))
plt.plot(t_1,u_1 , label='Low temperature')
plt.xlabel("Temperature")
plt.ylabel("Energy")
plt.grid()
plt.legend()
plt.title("Total Energy")
plt.show()

for i in range(len(t_2)):
    u_2.append(Total_Energy(g,e,z_high[i],t_2[i])) 
plt.plot(t_2,u_2 , label='High temperature')
plt.xlabel("Temperature")
plt.ylabel("Energy")
plt.grid()
plt.legend()
plt.title("Total Energy")
plt.show()

def Entropy(z,U,t,N):
    value = []
    for i in range(len(t)):
        s = N*k*np.log(z[i])+(U[i]*N)/t[i]+N*k
        value.append(s)
    return value

N = 10**(5)
Entropy_low=Entropy(z_low,u_1,t_1,N)
plt.plot(t_1,Entropy_low,label="Low temperature")
plt.xlabel("Temperature")
plt.ylabel("S")
plt.title("Entropy ")
plt.grid()
plt.legend()
plt.show()

Entropy_high=Entropy(z_high,u_2,t_2,N)
plt.plot(t_2,Entropy_high,label="High temperature")
plt.xlabel("Temperature")
plt.ylabel("S")
plt.title("Entropy ")
plt.grid()
plt.legend()
plt.show()

def gibbs_energy(N,t,z):
    g_e=[]
    for i  in range(len(t)):
        temp=-N*k*t[i]*np.log(z[i])
        g_e.append(temp)
    return g_e

g_e_low=gibbs_energy(N,t_1,z_low)
g_e_high=gibbs_energy(N,t_2,z_high)

plt.plot(t_1,g_e_low)
plt.xlabel("Temperature")
plt.ylabel("G_Energy")
plt.title("Gibbs Free Energy")
plt.grid()
plt.show()


plt.plot(t_2,g_e_high)
plt.xlabel("Temperature")
plt.ylabel("G_Energy")
plt.title("Gibbs Free Energy")
plt.grid()
plt.show()