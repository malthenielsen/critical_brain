import numpy as np
from matplotlib import pyplot as plt
plt.style.use('science')

def update(lat, i, j):
    i += 1
    j += 1
    lat[i,j] -= 4
    lat[i+1,j] += 1
    lat[i-1,j] += 1
    lat[i,j+1] += 1
    lat[i,j-1] += 1
    return lat

def unison_shuffled_copies(a, b):
    p = np.random.permutation(len(a))
    return a[p], b[p]

def one_iteration(lat):
    idx_i, idx_j = np.where(lat > 3)
    #  print(idx_i, idx_j)
    idx_i, idx_j = unison_shuffled_copies(idx_i, idx_j)
    lat = np.pad(lat, 1) 
    for i in range(len(idx_i)):
        lat = update(lat, idx_i[i], idx_j[i])
    lat = lat[1:-1, 1:-1]
    return lat, bool(len(idx_i)), 4*len(idx_i)

def runner(N, steps):
    ran_i, ran_j = np.random.randint(0,N,2*100).reshape(2,100)

    lat = np.random.randint(0,4,N*N).reshape(N,N)
    avalanche_array = np.zeros(steps)
    ran_array = np.zeros((steps, 100))

    for i in range(steps):
        drop_i, drop_j = np.random.randint(0,N,2)
        lat[drop_i, drop_j] += 1 
        ongoing = True
        avalanche_size = 0
        while ongoing:
            lat, ongoing, avalanche = one_iteration(lat)
            avalanche_size += avalanche
        avalanche_array[i] = avalanche_size
        for j in range(100):
            ran_array[i,j] = lat[ran_i[j], ran_j[j]]
    #  plt.plot(ran_array)
    np.save('ran', ran_array)
    np.save('AA', avalanche_array)
    #  plt.show()


    return avalanche_array[2500:]

aa = runner(50, 50000)
#  bins = np.linspace(0,5000,1000)
#  freq, bins = np.histogram(aa, bins = bins)
#  bins = (bins[1:] + bins[:-1])/2
#  plt.plot(bins/(50**2), freq)
#
#  aa = runner(30, 50000)
#  freq, bins = np.histogram(aa, bins = bins)
#  bins = (bins[1:] + bins[:-1])/2
#  plt.plot(bins/(30**2), freq)
#
#  aa = runner(20, 50000)
#  freq, bins = np.histogram(aa, bins = bins)
#  bins = (bins[1:] + bins[:-1])/2
#  plt.plot(bins/(20**2), freq)
#  plt.show()
