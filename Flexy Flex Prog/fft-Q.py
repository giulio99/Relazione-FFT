import numpy as np
import pylab as plt

#teff = 42.536 micro
#dteff = 2.374 micro 


t,v=np.loadtxt(r'C:\Users\GIULIO\Desktop\università\aa2019-2020\Laboratorio 2\esercizi obbligatori per casa\marzo\dati giulio\datibla_b.txt', unpack=True)

t=t/10e6
plt.figure(1)
plt.subplot(3,1,1)
#plt.title('Oscillatore smorzato RLC', fontsize=16)
plt.xlabel('$t$ [s]')
plt.ylabel('V(t)[digit]')


plt.errorbar(t, v, linestyle='', color='red', marker='.')


plt.subplot(3,1,2)
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
plt.errorbar(f[1:], amp[1:], linestyle='-', color='blue', marker='')

plt.subplot(3,1,3)
plt.errorbar(f[1:], spr[1:], linestyle='-', color='blue', marker='')

##Q SCHIFO
ampmax=max(amp[1:])
l=len(amp[1:])

for i in range(1,l):
    if (amp[i]==ampmax):
        fo=f[i]
        index=i
        break

HM=ampmax/2

support=abs(amp-HM)

punto1=min(support[:index])
punto2=min(support[index:])

for i in range(1,l):
    if (support[i]==punto1):
        f1=f[i]
        index1=i
    if (support[i]==punto2):
        f2=f[i]
        index2=i
        break

FWHM=f2-f1

Qamp=np.sqrt(3)*fo/FWHM

print('Q1=%f' %Qamp)

plt.show()





























