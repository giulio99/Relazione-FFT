import numpy as np
import matplotlib 
import matplotlib.pyplot as plt
import pylab
import pandas as pd

url = "https://raw.githubusercontent.com/giulio99/Relazione-FFT/master/dati%20prof/sin31.txt"
df = pd.read_csv(url, sep=" ",header=None)

df.columns =['time', 'voltage']

t= np.array(df.time)
v= np.array(df.voltage) 

w=v**2
##low frequency noise


amp=max(v)-min(v)
off=np.mean(v)
low_noise=amp/2*np.sin(t/40000)+off
'''
plt.figure(5)
plt.plot(t,low_noise)
plt.plot(t, v)
plt.title('Signal with noise')
plt.ylabel('Voltage (V)')
plt.xlabel('Time (s)')
'''

## Adding noise using target SNR

# Set a target SNR
target_snr_db = 20
# Calculate signal power and convert to dB 
sig_avg_watts = np.mean(w)
sig_avg_db = 10 * np.log10(sig_avg_watts)
# Calculate noise according to [2] then convert to watts
noise_avg_db = sig_avg_db - target_snr_db
noise_avg_watts = 10 ** (noise_avg_db / 10)
# Generate an sample of white noise
mean_noise = 0
noise_volts = np.random.normal(mean_noise, np.sqrt(noise_avg_watts), len(w))
# Noise up the original signal
y_volts1 = v + noise_volts+low_noise
'''
# Plot signal with noise
plt.figure(1)
plt.subplot(2,1,1)
plt.plot(t, y_volts1)
plt.title('Signal with noise')
plt.ylabel('Voltage (V)')
plt.xlabel('Time (s)')

# Plot in dB
y_watts1 = y_volts1 ** 2
y_db1 = 10 * np.log10(y_watts1)
plt.subplot(2,1,2)
plt.plot(t, 10* np.log10(y_volts1**2))
plt.title('Signal with noise (dB)')
plt.ylabel('Power (dB)')
plt.xlabel('Time (s)')
plt.show()
'''
## Adding noise using a target noise power

# Set a target channel noise power to something very noisy
target_noise_db =60

# Convert to linear Watt units
target_noise_watts = 10 ** (target_noise_db / 10)

# Generate noise samples
mean_noise = 0
noise_volts = np.random.normal(mean_noise, np.sqrt(target_noise_watts), len(w))

# Noise up the original signal (again) and plot
y_volts2 = v + noise_volts+low_noise

# Plot signal with noise
due=plt.figure(2)
plt.subplot(2,1,1)
plt.plot(t, y_volts2)
plt.title('Signal with noise')
plt.ylabel('Voltage (V)')
plt.xlabel('Time (s)')

# Plot in dB
y_watts2 = y_volts2 ** 2
y_db2 = 10 * np.log10(y_watts2)
plt.subplot(2,1,2)
plt.plot(t, 10* np.log10(y_volts2**2))
plt.title('Signal with noise')
plt.ylabel('Power (dB)')
plt.xlabel('Time (s)')
plt.show()

##FFT

V=np.fft.rfft(y_volts2)
#modulo
A=abs(np.fft.rfft(y_volts2))
#spettro di potenza
S=(abs(np.fft.rfft(y_volts2)))**2
#Dt efficace
Dt=np.zeros(len(t))
for i in range (len(t)-1):
    Dt[i]=t[i+1]-t[i]
Dtef=np.mean(Dt) #periodo medio
Df=1/(t[len(t)-1]-t[0]) #intervallo totale di tempo
fmax=1/(2*Dtef) #frequenza media
r=fmax/Df
nb=int(r) #numero di punti (ampiezza intervallo/lunghezza intervallo)
#frequenze
f=np.linspace(0,fmax,nb+1)


pylab.errorbar(f,A,linestyle = '-', color = 'blue', marker = '')
pylab.rc('font',size=18)
pylab.xlabel('f [Hz]')
pylab.ylabel('Ampiezza [a.u.]')
pylab.title('Ampiezza')
pylab.minorticks_on()
plt.show()

pylab.semilogy(f,A,linestyle = '-', color = 'blue', marker = '')
pylab.rc('font',size=18)
pylab.xlabel('f [Hz]')
pylab.ylabel('A [a.u.]')
pylab.title('Ampiezza in semilog(y)')
pylab.minorticks_on()
plt.show()

plt.figure(4)



