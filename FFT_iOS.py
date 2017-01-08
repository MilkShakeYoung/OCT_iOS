from pylab import *
import matplotlib.pyplot as plt
import numpy as np
# Replace "File_Name" to any .csv file in your dropbox account
I = np.loadtxt(open("NKT_15us_3thou.csv","rb"),delimiter=",",skiprows=0)
S = np.fft.fft(I, I.size)
Signal = np.abs(fftshift(S / abs(S).max()))
peak_range = np.arange(1023,1100,1)
plot(Signal[peak_range])
plt.show()
