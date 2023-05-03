import numpy as np 
import matplotlib.pyplot as plt
import random
import pandas as pd
import math

# (a) : 

# (a) i. : 
def coin():
	return random.randint(0,1)

# (a) ii. : 
def system(nc):
	micro = []
	for i in range(0,nc):
		output = coin()
		micro.append(output)
	macro = sum(micro)
	return micro, macro

# (a) iii. : 
def ensemble(nt,nc):
	microstates = []
	macrostates = []
	for i in range(0,nt):
		micro, macro = system(nc)
		microstates.append(micro)
		macrostates.append(macro)
	return macrostates,microstates 

# (b) :

# (b) i. A.
micro, macro = system(100)
print(micro, macro)
# (b) i. B.
micro, macro = system(10)
print(micro, macro)
# (b) i. C.
micro, macro = system(1)
print(micro, macro)

# (c) : 

# (c) i. Trials variation plot : 

def graph1(nt,nc):
	for k in range(1,6):
		macrostates, microstates = ensemble(pow(nt,k)*nc,nc)
		frequencies = []
		heads = []
		for i in range(0,nc+1):
			heads.append(i)
			frequencies.append(macrostates.count(i))
		frequencies = np.array(frequencies)
		probability = frequencies/(pow(nt,k)*nc)
		plt.plot(heads, probability,marker='.',label=f"Nt={pow(nt,k)*nc}")
	plt.xlabel("# of heads")
	plt.ylabel("probability")
	plt.title(f"# of heads vs probability for {nc} coins")
	plt.grid()
	xval = np.arange(0,nc+1,1)
	Px=[]
	for i in range(0,len(xval)):
		Px.append(math.comb(nc,xval[i])*pow(0.5,xval[i])*pow(0.5,nc-xval[i]))
	plt.plot(xval,Px,label="Binomial Overlay",linestyle='dashed')
	plt.legend()
	plt.show()

nc = [5,10]
for i in range(0,len(nc)):
	graph1(10,nc[i])

# (c) ii. Coin variation plot : 
def graph2(nt,nc):
	for k in range(1,11):
		macrostates, microstates = ensemble(nt,k)
		frequencies = []
		heads = []
		for i in range(0,k+1):
			heads.append(i)
			frequencies.append(macrostates.count(i))
		frequencies = np.array(frequencies)
		probability = frequencies/nt
		plt.plot(heads, probability,marker='.',label=f"Nc={k}")
	plt.xlabel("# of heads")
	plt.ylabel("probability")
	plt.title("# of heads vs probability")
	plt.grid()
	plt.legend()
	plt.show()

graph2(10000,2)

# (c) iii. Cummulative plot : 
def graph3(nt,nc):
	microstates = []
	macrostates = []
	for i in range(0,nt):
		micro, macro = system(nc)
		microstates.append(micro)
		macrostates.append(macro)
	for i in range(1,nt+1):
		nr = 0
		Nrs = []
		Drs = []
		for j in range(0,i):
			nr = nr + macrostates[j]
			Nrs.append(nr)
			dr = (j+1)*nc
			Drs.append(dr)
	Nrs = np.array(Nrs)
	Drs = np.array(Drs)
	CF = Nrs/Drs
	trials = np.arange(0,nt,1)
	trials = trials + 1
	CF_t = 1 - CF
	plt.plot(trials,CF, label="Cumulative frequency of heads")
	plt.plot(trials,CF_t, label="Cumulative frequency of tails")
	plt.xlabel("# of trials")
	plt.ylabel("Cumulative frequency")
	plt.title(f"No of trails vs Cumulative frequency upto {nt} trials")
	plt.grid()
	plt.legend()
	plt.show()

nc = 3
nt = [500,10000]
for i in range(0,len(nt)):
	graph3(nt[i],nc)