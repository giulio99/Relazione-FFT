import numpy as np
import matplotlib 
import matplotlib.pyplot as plt
import pylab as py 

t,v = py.loadtxt('longC=0.1f=4Hz(senza rettangolo).txt', unpack=True)

plt.figure(1)

plt.errorbar(t, v, linestyle='', color='red', marker='.')


plt.figure(2)
plt.title('Oscillatore smorzato RLC', fontsize=16)
plt.xlabel('$F$ [Hz]')
plt.ylabel('[a.u.]')
plt.grid()

amp=abs(np.fft.rfft(v))
spr=amp**2
tef=0

for i in range (len(t)-1):
    tef+=t[i+1]-t[i]
    
tef=(tef/len(t))

fmax=1/(2*tef) #tef tempo medio tra due punti qualsiasi
df=1/(t[len(t)-1]-t[0])
r=int(fmax/df)
f=np.linspace(0,fmax,r+1)
plt.errorbar(f, amp, linestyle='-', color='red', marker='')
plt.semilogy()


plt.show()