import numpy as np
import pandas as pd
import pylab as pl
from scipy.optimize import curve_fit


url = "https://raw.githubusercontent.com/giulio99/Relazione-FFT/master/dati%20prof/sin11.txt"
df = pd.read_csv(url, sep=" ",header=None)

df.columns =['time', 'voltage']

t1 = np.array(df.time)

V1 = np.array(df.voltage) 

print(t1)

print(V1)
