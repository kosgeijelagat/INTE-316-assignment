import sympy as sp

x = sp.symbols('x')
f = x**3 + 2*x**2 + x + 1
f_prime = sp.diff(f, x)
print(f_prime)
