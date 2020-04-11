#MODULAZIONE DI SENI REALI

import numpy as np
import matplotlib 
import matplotlib.pyplot as plt
import plotly.offline as ply
import pandas
import pylab

#Modulazione di ampiezza

T1,V1= np.loadtxt('https://raw.githubusercontent.com/giulio99/Relazione-FFT/master/dati%20prof/sin30.txt', unpack=True)

T2,V2= np.loadtxt('https://raw.githubusercontent.com/giulio99/Relazione-FFT/master/dati%20prof/sin33.txt', unpack=True)

plt.errorbar(T1,V1, linestyle='',marker='.',color='red')
plt.errorbar(T2,V2, linestyle='',marker='.',color='black')
plt.xlabel('t [s]')
plt.ylabel('V [a.u.]')
plt.show()

v1=np.mean(V1)
v2=np.mean(V2)

x=V1-v1
y=V2-v2

plt.errorbar(T1,x, linestyle='',marker='.',color='red')
plt.errorbar(T2,y, linestyle='',marker='.',color='black')
plt.xlabel('t [s]')
plt.ylabel('V [a.u.]')
plt.show()

h=np.max(x)-np.min(x)

M=1
def mod(x,y):
    return (x/M)*y
g=mod(x,y)

h2=np.max(g)-np.min(g)

plt.errorbar(T2,g/(h2/2), linestyle='-',marker='',color='red')
plt.errorbar(T2,y/(h/2), linestyle='-',linewidth=3,marker='',color='blue')
plt.show()

