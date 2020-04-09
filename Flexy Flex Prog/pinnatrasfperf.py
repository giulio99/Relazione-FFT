#SIMULAZIONE DI UNA PINNA PERFETTA CON TRASFORMATA

import numpy as np
import matplotlib 
import matplotlib.pyplot as plt
import plotly.offline as ply
import pandas
import pylab

#crea un array da 1 a 10000 con un numero si e uno no, quindi partendo da 1 tutti i dispari
dispari=np.arange(1, 10000, 2)
#array contenente le frequenze delle onde in entrata
f=500
w=2*np.pi*f

#valori del condensatore e della resistenza, con il calcolo delle relative frequenze di taglio
C=10**-7
R=3300
ft=1/(2*np.pi*R*C)
wt=2*np.pi*ft

#calcola i coefficienti della serie di fourier per una quadra
ck=2/(dispari*np.pi)
#crea una array vuoto(1000 in questo caso) da vedere come un 'array di array', dove andranno le y a seconda delle varie frequenze
y=np.empty(1000)

#cicli for per le serie di fourier
x=np.linspace(0, 4/f,1000)#crea un array di mille punti in un intervallo di 4 periodi a seconda della frequenza
for i in range(len(x)):
#calcola Ak e fi attenuazione e sfasamento a seconda della frequenza, poi somma tutti i termini della serie di fourier e li
        # introduce nella corretta riga della matrice y
    Ak=1/np.sqrt(1+((w*dispari)/wt)**2)
    fi=np.arctan(-(w*dispari)/wt)
    a=(ck*Ak*np.sin(w*dispari*x[i] + fi)).sum()
    y[i]=a
pylab.subplot(2,1,1)
plt.plot(x,y,linestyle='-',color='red')
plb.xlabel('t [ms]')
plb.ylabel('V [a.u.]')


#trasformato
Vt=np.fft.rfft(y)
#modulo
A=abs(np.fft.rfft(y))
#spettro di potenza
S=(abs(np.fft.rfft(y)))**2
#Dt efficace
Dt=np.zeros(len(x))
for i in range (len(x)-1):
    Dt[i]=x[i+1]-x[i]
Dtef=np.mean(Dt) #periodo medio
Df=1/(x[len(x)-1]-x[0]) #intervallo totale di tempo
fmax=1/(2*Dtef) #frequenza media
r=fmax/Df
nb=int(r) #numero di punti (ampiezza intervallo/lunghezza intervallo)
#frequenze
f=np.linspace(0,fmax,nb+1)
'''
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
'''
pylab.subplot(2,1,2)
pylab.semilogy(f,A,linestyle = '-', color = 'blue', marker = '')
pylab.rc('font',size=18)
pylab.xlabel('f [Hz]')
pylab.ylabel('A [a.u.]')
#pylab.title('Ampiezza in semilog(y)')
pylab.minorticks_on()
'''
pylab.semilogy(f,S,linestyle = '-', color = 'red', marker = '')
pylab.rc('font',size=18)
pylab.xlabel('f [Hz]')
pylab.ylabel('A [a.u.]')
#pylab.title('Spettro di potenza in semilog(y)')
pylab.minorticks_on()
'''
plt.show()