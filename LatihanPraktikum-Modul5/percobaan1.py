import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1, 8])
ypoints = np.array([3, 10])

plt.title('Plot Satu Garis')
plt.xlabel('Nilai X')
plt.ylabel('Nilai Y')

plt.plot(xpoints, ypoints)
plt.show()