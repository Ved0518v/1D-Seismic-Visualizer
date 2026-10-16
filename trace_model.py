import numpy as np
import matplotlib.pyplot as plt

# 1. Create the Soundwave (Ricker Wavelet)
frequency = 30.0  # Dominant frequency in Hz
time_wavelet = np.arange(-0.05, 0.05, 0.002)
pft2 = (np.pi * frequency * time_wavelet)**2
wavelet = (1 - 2 * pft2) * np.exp(-pft2)

# 2. Simulate the Earth (Reflection Coefficients)
depth_samples = 250
rc = np.zeros(depth_samples)
rc[50] = 0.5   # Entering hard limestone
rc[100] = -0.4 # Entering porous sandstone (potential reservoir)
rc[180] = 0.3  # Entering another hard layer

# 3. Create the Seismic Trace (Convolution)
trace = np.convolve(rc, wavelet, mode='same')

# 4. Plot the "Wiggle Trace"
fig, ax = plt.subplots(figsize=(4, 8))
y_axis = np.arange(depth_samples)

ax.plot(trace, y_axis, color='black', linewidth=1)
ax.fill_betweenx(y_axis, 0, trace, where=(trace > 0), color='black')

ax.invert_yaxis()
ax.set_title("1D Seismic Wiggle Trace", fontweight='bold')
ax.set_xlabel("Amplitude")
ax.set_ylabel("Depth Sample")
ax.axvline(0, color='grey', linestyle='--', alpha=0.5)

plt.tight_layout()
plt.show()