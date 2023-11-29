import matplotlib.pyplot as plt
import numpy as np
from numpy import mean, std
from scipy.stats import norm

sample = np.random.normal(loc=50, scale=5, size=1000)

sample_mean = mean(sample)
sample_std = std(sample)
print('Mean=%.3f \nStandard Deviation=%.3f' % (sample_mean, sample_std))

dist = norm(sample_mean, sample_std)

values = np.linspace(30, 70, 1000)

probabilities = dist.pdf(values)

plt.figure(figsize=(8, 6))
plt.hist(sample, bins=10, density=True, alpha=0.6, color='blue', label='Sample Histogram')
plt.plot(values, probabilities, color='r', label='Distribusi Normal')

plt.title('Histogram Sample Data Normal')
plt.xlabel('Value')
plt.ylabel('Relative Frequency')

plt.legend()
plt.show()
