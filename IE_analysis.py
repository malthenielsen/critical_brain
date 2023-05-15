import numpy as np
from matplotlib import pyplot as plt
plt.style.use('science')


data = np.genfromtxt('results.txt', delimiter = ',')
data = np.nan_to_num(data, 0)
inn = data[:,-1]
#  print(inn)
data = data[:,:-2]
fig, ax = plt.subplots(1,1, figsize = (8,6))
#  ax.plot(data.sum(axis =1))
#  ax.plot(inn)
#  ax.hist(data.sum(axis =1), bins = np.arange(0,15,1))
freq, bins = np.histogram(data.sum(axis = 1), bins = np.arange(0,15,1))
bins = np.arange(0,14,1)

ax.scatter(bins, freq)
ax.set_yscale('log')
ax.set_xscale('log')


#  ax.imshow(data)
plt.show()

