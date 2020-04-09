import numpy as np
import matplotlib.pyplot as plt
import pylab as py

t,v=np.loadtxt('Sin14.txt', unpack=True)

#Calcolo quantità interessanti
teff=0
for i in range(len(t)-1):
    teff+=t[i+1]-t[i]
    
teff=(teff/len(t))
fmax=1/(2*teff)
df=1/(t[len(t)-1]-t[0])
r=int(fmax/df)

#Spettro delle frequenze
amp=abs(np.fft.rfft(v))
spr=amp**2

#Frequenze
f=np.linspace(0,fmax,r+1)

plt.errorbar(f,spr,ls='', color='red',marker='+')
plt.show()
