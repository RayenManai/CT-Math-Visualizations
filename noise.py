#The following is a visualization for a possible technique to reduce noise: this is done by applying a Filter.


import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Generate a noisy signal
x = np.linspace(-10, 10, 1000)
y = 2 * np.sin(2 * x) + 1.5 * np.sin(2 * x) + np.random.normal(0, 0.1, size=1000)

#define the used Filter
kernel_weights = signal.gaussian(51, std=7)
plt.show()


# Normalize the kernel weights so that their sum is 1
kernel_weights /= np.sum(kernel_weights)

# Convolve the signal with the kernel
y_convolved = np.convolve(y, kernel_weights, mode='same')

# Plot the original signal and the convolved signal in one graph
plt.plot(x, y, label='Original signal')
plt.plot(x, y_convolved, label='Filtered signal')
plt.legend()
plt.show()

#plot the applied Filter
plt.plot(kernel_weights, label='Filter')
plt.legend()
plt.show()


# Plot the original signal and the convolved signal in separate graphs
plt.subplot(1, 2, 1)
plt.plot(x, y, label='Original signal')
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(x, y_convolved, label='Filtered signal')
plt.legend()
plt.show()
