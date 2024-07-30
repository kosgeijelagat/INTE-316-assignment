import numpy as np
import matplotlib.pyplot as plt

# Given data points
x = np.array([2.00, 3.25, 4.50])
y = np.array([4.25, 5.20, 7.15])

# Linear spline interpolation function
def linear_spline(x, y, x_new):
    y_new = np.zeros_like(x_new)
    for i in range(len(x) - 1):
        mask = (x_new >= x[i]) & (x_new <= x[i + 1])
        y_new[mask] = y[i] + (y[i + 1] - y[i]) / (x[i + 1] - x[i]) * (x_new[mask] - x[i])
    return y_new

# New x values for interpolation
x_new = np.linspace(2.00, 4.50, 100)
y_new = linear_spline(x, y, x_new)

# Plotting the results
plt.plot(x, y, 'o', label='Data points')
plt.plot(x_new, y_new, '-', label='Linear spline')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Linear Spline Interpolation')
plt.show()
