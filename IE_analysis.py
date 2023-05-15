import numpy as np
from matplotlib import pyplot as plt
plt.style.use('science')
import time

#  start = time.time()
data_bin = np.fromfile("results.bin", dtype = np.int8)
data = data_bin.reshape(-1,1000)
#  end = time.time()
#  print(end - start)


#  start = time.time()
#  data = np.genfromtxt('results.txt', delimiter = ',')
#  data = np.nan_to_num(data, 0)
#  end = time.time()
#  print(end - start)

#  inn = data[:,-1]
#  print(inn)
data = data[:,:-2]
fig, ax = plt.subplots(1,1, figsize = (8,6))
#  ax.plot(data.sum(axis =1))
#  ax.plot(inn)
#  ax.hist(data.sum(axis =1), bins = 100)
freq, bins = np.histogram(data.sum(axis = 1), bins = np.arange(100))
#  bins = np.arange(0,14,1)
bins = bins[1:]

ax.scatter(bins, freq)
ax.set_yscale('log')
ax.set_xscale('log')


#  ax.imshow(data)
plt.show()

