import numpy as np

# Define the function
def f(x):
    return x**2 - x - 2

# Define the point at which to differentiate and the step size
x = 1.5
h = 1e-5

# Numerical differentiation (finite difference method)
df_dx = (f(x + h) - f(x - h)) / (2 * h)
print(f"The derivative of f at x = {x} is approximately {df_dx}")
