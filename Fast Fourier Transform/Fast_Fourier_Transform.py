#Fast Fourier Transform of given function in tabulated or mathematical form e.g. function exp (-x^2).

import numpy as np
import matplotlib.pyplot as plt

#defin the function e^(-x^2).
def original_fun(x):
    return np.exp(-x**2)

#Number of points for the tabulated function.
num_points = 1000
x_values = np.linspace(-10, 10, num_points)
y_values = original_fun(x_values)

#perform the fast fourier transform(FFT).
fft_result = np.fft.fft(y_values)
freq = np.fft.fftfreq(num_points, x_values[1] - x_values[0])

#Plot the original function.
plt.figure(figsize=(12,6))
plt.subplot(2,1,1)
plt.plot(x_values,y_values,label="Original Function")
plt.title("Original Function: exp(-x^2)")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()

#Plot the fourier Transform
plt.subplot(2,1,2)
plt.plot(freq, np.abs(fft_result),label="FFT of the Function")
plt.title("Fourier Transform")
plt.xlabel("Frequency")
plt.ylabel("Amplitude")
plt.legend()
plt.tight_layout()
plt.show()