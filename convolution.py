#This is just a simple visualization for the convolution as an option to cmobine two functions.

import numpy as np
import matplotlib.pyplot as plt

#generate two rectangular functions f and h
f = np.repeat([0., 2., 0.], 100)
h = np.repeat([0., 3., 0.], 100)

#compute the convolution: f*h
convolved = np.convolve(f, h, mode='same')

#plot the functions and the result of their convolution
fig, ax = plt.subplots(3, 1, sharex=True)
ax[0].plot(f, 'C2', label='f')
ax[1].plot(h, label='h')
ax[2].plot(convolved, 'C3', label='f * h')

for axx in ax:
    axx.legend()

plt.show()
