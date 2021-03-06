import numpy as np
import matplotlib 
import matplotlib.pyplot as plt
import pylab as py 

t,v = py.loadtxt('datiharmC=0.47.txt', unpack=True)

t=t/10e6
plt.figure(1)
plt.subplot(2,1,1)
#plt.title('Oscillatore smorzato RLC', fontsize=16)
plt.xlabel('$t$ [s]')
plt.ylabel('V(t)[digit]')


plt.errorbar(t, v, linestyle='', color='red', marker='.')


plt.subplot(2,1,2)
plt.xlabel('$f$ [Hz]')
plt.ylabel(r'$\bar{V}$(f)[arb.un.]')

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
plt.errorbar(f, amp, linestyle='-', color='blue', marker='')
plt.semilogy()

plt.show()

