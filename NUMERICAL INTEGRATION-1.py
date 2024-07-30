import scipy.integrate as spi
import numpy as np

def integrand(x):
    return x**2

result, error = spi.quad(integrand, 0, 1)
print(result)
