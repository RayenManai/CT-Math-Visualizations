#This is a visualization to the Fourier Transform: this allows you to generate signals with different frequencies and amplitudes and then check that in the frequency Domain after applying the Fourier Transform.


import numpy as np
from scipy.fft import fft, rfft
from scipy.fft import fftfreq, rfftfreq
import matplotlib.pyplot as plt


# Building a class to generate Signals with different frequencies and amplitudes


class Signal:
 
    def __init__(self, amplitude=1, frequency=10, duration=1, sampling_rate=100.0):
        self.amplitude = amplitude
        self.frequency = frequency
        self.duration = duration
        self.sampling_rate = sampling_rate
        self.time_step = 1.0/self.sampling_rate
        self.time_axis = np.arange(0, self.duration, self.time_step)

    # Generate sine wave
    def sine(self):
        return self.amplitude*np.sin(2*np.pi*self.frequency*self.time_axis)


# Generate three different signals 
signal_1 = Signal(amplitude=2, frequency=1, sampling_rate=200, duration=2)
sine_1 = signal_1.sine()
signal_2 = Signal(amplitude=1, frequency=20, sampling_rate=200, duration=2)
sine_2 = signal_2.sine()
signal_3 = Signal(amplitude=0.3, frequency=10, sampling_rate=200, duration=2)
sine_3 = signal_3.sine()

# Sum the three signals 
signal = sine_1 + sine_2 + sine_3

# Plot the result signal
plt.plot(signal_1.time_axis, signal, 'b')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.title('Mixed Signal')
plt.show()


N = len(signal)
sampling_rate = 200.0  

#plot the spectrum
plt.plot(rfftfreq(N, d=1/sampling_rate), 2*np.abs(rfft(signal))/N)
plt.title('Spectrum')
plt.xlim(xmin=0, xmax=60)
plt.xlabel('Frequency[Hz]')
plt.ylabel('Amplitude')
plt.show()
