#MODULAZIONE DI SENI REALI

import numpy as np
import matplotlib 
import matplotlib.pyplot as plt
import plotly.offline as ply
import pandas
import pylab

#Modulazione di frequenza

T1,V1= np.loadtxt('https://raw.githubusercontent.com/giulio99/Relazione-FFT/master/dati%20prof/sin30.txt', unpack=True)

T2,V2= np.loadtxt('https://raw.githubusercontent.com/giulio99/Relazione-FFT/master/dati%20prof/sin32.txt', unpack=True)

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

#t=np.arcsin(x/(h/2))

#provo a trasformare
#trasformato
Vt=np.fft.rfft(x)
#modulo
A=abs(np.fft.rfft(x))
#Dt efficace
Dt=np.zeros(len(T1))
for i in range (len(T1)-1):
    Dt[i]=T1[i+1]-T1[i]
Dtef=np.mean(Dt) #periodo medio
Df=1/(T1[len(T1)-1]-T1[0]) #intervallo totale di tempo
fmax=1/(2*Dtef) #frequenza media
r=fmax/Df
nb=int(r) #numero di punti (ampiezza intervallo/lunghezza intervallo)
#frequenze
f=np.linspace(0,fmax,nb+1)

Am=np.max(A)

for i in range (len(f)):
    if (A[i]==Am):
        j=i
        
F=f[j]

def mod(f,y):
    return np.sin(f*T1 + np.pi*y)
    
g=mod(F,y)

h2=np.max(g)-np.min(g)

plt.errorbar(T2,g/(h2/2), linestyle='-',marker='.',color='red')
plt.errorbar(T2,y/(h/2), linestyle='-',linewidth=2,marker='',color='blue')
plt.show()



