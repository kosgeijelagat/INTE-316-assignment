import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline

# Generate some data
x = np.array([0, 1, 2, 3, 4, 5])
y = np.array([0, 1, 0, 1, 0, 1])

# Create a spline
spline = make_interp_spline(x, y)

# Generate new x values and interpolate
x_new = np.linspace(0, 5, 300)
y_new = spline(x_new)

# Plot the data and the spline
plt.scatter(x, y, label='Data')
plt.plot(x_new, y_new, label='Spline', color='red')
plt.legend()
plt.show()
