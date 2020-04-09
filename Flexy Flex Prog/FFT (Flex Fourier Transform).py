import numpy as np
import matplotlib 
import matplotlib.pyplot as plt
import plotly.offline as ply
import pylab
import pandas

T,V= np.loadtxt('https://raw.githubusercontent.com/flexyscotty/Relazione-FFT/master/Dati%20Lori%20Benf/transoscBB5.txt', unpack=True)
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

pylab.errorbar(T,V,linestyle = '-', color = 'black', marker = '.')
pylab.rc('font',size=18)
pylab.xlabel('T [$\mu$s]')
pylab.ylabel('V [mV]')
pylab.minorticks_on()
plt.show()
pylab.errorbar(f,A,linestyle = '-', color = 'blue', marker = '')
pylab.rc('font',size=18)
pylab.xlabel('f [Hz]')
pylab.ylabel('Ampiezza [a.u.]')
pylab.title('Ampiezza')
pylab.minorticks_on()
plt.show()
pylab.errorbar(f,S,linestyle = '-', color = 'red', marker = '')
pylab.rc('font',size=18)
pylab.xlabel('f [Hz]')
pylab.ylabel('Spettro di potenza [a.u.]')
pylab.title('Spettro di potenza')
pylab.minorticks_on()
plt.show()


pylab.semilogy(f,A,linestyle = '-', color = 'blue', marker = '')
pylab.rc('font',size=18)
pylab.xlabel('f [Hz]')
pylab.ylabel('A [a.u.]')
pylab.title('Ampiezza in semilog(y)')
pylab.minorticks_on()
plt.show()
pylab.semilogy(f,S,linestyle = '-', color = 'red', marker = '')
pylab.rc('font',size=18)
pylab.xlabel('f [Hz]')
pylab.ylabel('A [a.u.]')
pylab.title('Spettro di potenza in semilog(y)')
pylab.minorticks_on()
plt.show()
