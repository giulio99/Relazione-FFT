import numpy as np
import matplotlib as mplt
import matplotlib.pyplot as plt


t, x=np.loadtxt('nomefile.txt', unpack=True)

plt.plot(t,x)
plt.show()











