import numpy as  np
import matplotlib.pyplot as plt
import random
import pandas as pd
import math

def coin():
    outcome=random.randint(0,1) #1=HEADS 0=TAILS
    return outcome

def system(Nc):
    l1=[] #microstates
    for i in range(0,Nc):
        out=coin()
        l1.append(out)
    l2=sum(l1)   # sum will give the no. of heads, l2= macrostates
    return(l1,l2)
 
def ensemble(Nt,Nc):
    microstates=[];macrostates=[]
    for i in range(0,Nt):
        micro,macro=system(Nc)
        microstates.append(micro)
        macrostates.append(macro)
    return microstates,macrostates

fig, (ax1, ax2, ax3) = plt.subplots(nrows=1, ncols=3)
fig.suptitle("No.of heads vs probability(fixed Nc)")
def graph(Nc,axis):
    Nt=np.array([10,50,100,500,1000])*Nc
    for k in Nt:
        a1,a2=ensemble(k,Nc)
        freq=[];heads=[]
        for i in range(0,Nc+1):
            heads.append(i)
            freq.append(a2.count(i))
        prob=np.array(freq)
        probability=prob/k
        axis.plot(heads,probability,marker=".",label=f"Nt={k/Nc}"+str("Nc"))
    xval = np.arange(0,Nc+1,1)
    Px=[]
    for i in range(0,len(xval)):
        Px.append(math.comb(Nc,xval[i])*pow(0.5,xval[i])*pow(0.5,Nc-xval[i]))
    axis.plot(xval,Px,label="Binomial",linestyle='dashed',c="black")
    axis.set_xlabel("No.of heads")
    axis.set_ylabel("probability")
    axis.set_title("Nc="+str(Nc))
    axis.grid()
    axis.legend()

graph(Nc=5,axis=ax1)
graph(Nc=10,axis=ax2)
graph(Nc=100,axis=ax3)
plt.show()

def graph2(Nt):
    for k in range(1,11):
        a1,a2=ensemble(Nt,k)
        freq=[];heads=[]
        for i in range(0,k+1):
            heads.append(i)
            freq.append(a2.count(i))
        prob=np.array(freq)
        probability=prob/Nt
        plt.plot(heads,probability,marker=".",label=f"Nc={k}")

    plt.xlabel("No.of heads")
    plt.ylabel("probability")
    plt.title("No.of heads vs probability(fixed Nt=100)")
    plt.grid()
    plt.legend()
    plt.show()

graph2(Nt=100)

fig2, (ax1, ax2) = plt.subplots(nrows=1, ncols=2)
fig2.suptitle("No. of trials vs Cummulative frequency")

def graph3(Nt,Nc,axis):
	microstates = []
	macrostates = []
	for i in range(0,Nt):
		micro, macro = system(Nc)
		microstates.append(micro)
		macrostates.append(macro)
	for i in range(1,Nt+1):
		nr = 0
		Nrs = []
		Drs = []
		for j in range(0,i):
			nr = nr + macrostates[j]
			Nrs.append(nr)
			dr = (j+1)*Nc
			Drs.append(dr)
	Nrs = np.array(Nrs)
	Drs = np.array(Drs)
	CF = Nrs/Drs
	trials = np.arange(0,Nt,1)
	trials = trials + 1
	CF_t = 1 - CF
	axis.plot(trials,CF,label='P(head)')
	axis.plot(trials,CF_t,label='P(tail)')
	axis.set_xlabel("No. of trials")
	axis.set_ylabel("Cummulative frequency")
	axis.set_title("Nt="+str(Nt))
	axis.grid()
	axis.legend()

graph3(Nt=500,Nc=3,axis=ax1)
graph3(Nt=10000,Nc=3,axis=ax2)
plt.show()