import scipy.integrate as spi

# Define the function
def f(x):
    return x**2 - x - 2

# Define the limits of integration
a = 1
b = 3

# Numerical integration
integral, error = spi.quad(f, a, b)
print(f"The integral of f from {a} to {b} is approximately {integral}")
