#MODULAZIONE DI SENI REALI

import numpy as np
import matplotlib 
import matplotlib.pyplot as plt
import plotly.offline as ply
import pandas
import pylab

#Modulazione di frequenza

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
plt.xlabel('t [$\mu$s]')
plt.ylabel('V [a.u.]')
plt.show()

h=np.max(x)-np.min(x)

M=1

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
    return np.sin(f*T1 + y/M)
    
g=mod(F,y)

h2=np.max(g)-np.min(g)

plt.errorbar(T2,g/(h2/2), linestyle='-',marker='.',color='red')
plt.errorbar(T2,y/(h/2), linestyle='-',linewidth=2,marker='',color='blue')
plt.xlabel('t [$\mu$s]')
plt.ylabel('V [a.u.]')
plt.show()

V=g
T=T2/1000000

#trasformato
Vt=np.fft.rfft(V)
#modulo
A=abs(np.fft.rfft(V))
#spettro di potenza
S=(abs(np.fft.rfft(V)))**2
#Dt efficace
Dt=np.zeros(len(T))
for i in range (len(T)-1):
    Dt[i]=T[i+1]-T[i]
Dtef=np.mean(Dt) #periodo medio
Df=1/(T[len(T)-1]-T[0]) #intervallo totale di tempo
fmax=1/(2*Dtef) #frequenza media
r=fmax/Df
nb=int(r) #numero di punti (ampiezza intervallo/lunghezza intervallo)
#frequenze
f=np.linspace(0,fmax,nb+1)
'''
pylab.errorbar(T,V,linestyle = '-', color = 'black', marker = '.')
pylab.rc('font',size=18)
pylab.xlabel('T [$\mu$s]')
pylab.ylabel('modulazione []')
pylab.minorticks_on()
plt.show()
'''
pylab.errorbar(f,A,linestyle = '-', color = 'blue', marker = '')
pylab.rc('font',size=18)
pylab.xlabel('f [Hz]')
pylab.ylabel('Ampiezza [a.u.]')
pylab.title('Trasformata della modulazione della frequenza')
pylab.minorticks_on()
plt.show()
'''
pylab.errorbar(f,S,linestyle = '-', color = 'red', marker = '')
pylab.rc('font',size=18)
pylab.xlabel('f [Hz]')
pylab.ylabel('Spettro di potenza [a.u.]')
pylab.title('Spettro di potenza della trasformata della modulazione della frequenza')
pylab.minorticks_on()
plt.show()
'''

pylab.semilogy(f,A,linestyle = '-', color = 'blue', marker = '')
pylab.rc('font',size=18)
pylab.xlabel('f [Hz]')
pylab.ylabel('A [a.u.]')
pylab.title('Ampiezza della trasformata  della modulazione della frequenza in semilog(y)')
pylab.minorticks_on()
plt.show()
'''
pylab.semilogy(f,S,linestyle = '-', color = 'red', marker = '')
pylab.rc('font',size=18)
pylab.xlabel('f [Hz]')
pylab.ylabel('A [a.u.]')
pylab.title('Spettro di potenza della trasformata della modulazione della frequenza in semilog(y)')
pylab.minorticks_on()
plt.show()
'''

