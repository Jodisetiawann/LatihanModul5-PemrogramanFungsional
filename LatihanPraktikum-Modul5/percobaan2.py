import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1, 2, 4, 6, 8, 10, 11]) 
ypoints = np.array([3, 2, 4, 2, 4, 2, 3])

apoints = np.array([1, 2, 4, 6, 8, 10, 11]) 
bpoints = np.array([3, 4, 2, 4, 2, 4, 3])


plt.figure(figsize=(5,5))
plt.plot(xpoints, ypoints, color='black')
plt.plot(apoints, bpoints, color='red')
plt.xlim([0, 15])
plt.ylim([0, 15])

plt.xlabel('Nilai X')
plt.ylabel('Nilai Y')

plt.show()