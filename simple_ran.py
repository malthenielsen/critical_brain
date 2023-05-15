import numpy as np
from matplotlib import pyplot as plt
plt.style.use('science')
from scipy.signal import find_peaks

ran = np.load('ran.npy')
aa = np.load('AA.npy')
fig, ax = plt.subplots(1,1, figsize = (10,8))
raster = []
for i in range(1):
    dran = np.diff(ran[:,i])
    dran = np.where(dran < 0 , 1, 0)
    inds, _ = find_peaks(dran, height = 0)
    T = np.diff(inds)
    #  ax.hist(T, bins = 100, histtype = 'step', color = 'black', alpha = .1)
    raster.append(dran)

raster = np.vstack(raster)
#  ax.imshow(raster, cmap = 'binary', aspect = 'auto', vmin = 0, vmax = 1, interpolation = 'None')
#  ax2 = ax.twinx()
ax.plot(raster.sum(axis = 0)/np.max(raster.sum(axis = 0))- aa[1:]/np.max(aa))
#  ax2.plot(aa, color = 'red', alpha = .5)
#  ax.plot(dran)
plt.show()

