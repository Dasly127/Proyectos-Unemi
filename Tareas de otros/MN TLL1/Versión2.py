
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

# Interpolación de Lagrange
def lagrange_interpolation(x_values, y_values):
    n = len(x_values)
    x = sp.symbols('x')
    polynomial = 0

    for i in range(n):
        term = y_values[i]
        for j in range(n):
            if i != j:
                term *= (x - x_values[j]) / (x_values[i] - x_values[j])
        polynomial += term

    # Simplificar el polinomio
    polynomial = sp.simplify(polynomial)
    return polynomial

# Interpolación de Newton
def divided_differences(x_values, y_values):
    n = len(x_values)
    diff = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        diff[i][0] = y_values[i]

    for j in range(1, n):
        for i in range(n - j):
            diff[i][j] = (diff[i + 1][j - 1] - diff[i][j - 1]) / (x_values[i + j] - x_values[i])

    return [diff[0][i] for i in range(n)]

def newton_interpolation(x_values, y_values):
    n = len(x_values)
    x = sp.symbols('x')
    polynomial = 0
    coeffs = divided_differences(x_values, y_values)
    term = 1

    for i in range(n):
        polynomial += coeffs[i] * term
        if i < n - 1:
            term *= (x - x_values[i])

    # Simplificar el polinomio
    polynomial = sp.simplify(polynomial)
    return polynomial

# Interpolación Inversa de Lagrange
def lagrange_interpolation_inverse_polynomial(x_values, y_values):
    n = len(x_values)
    y = sp.symbols('y')
    polynomial = 0
    for i in range(n):
        term = x_values[i]
        for j in range(n):
            if i != j:
                term *= (y - y_values[j]) / (y_values[i] - y_values[j])
        polynomial += term

    # Simplificar el polinomio
    polynomial = sp.simplify(polynomial)
    return polynomial

# Interpolación Inversa de Newton
def newton_interpolation_inverse_polynomial(x_values, y_values):
    n = len(x_values)
    y = sp.symbols('y')
    polynomial = 0
    coeffs = divided_differences(x_values, y_values)
    term = 1

    for i in range(n):
        polynomial += coeffs[i] * term
        if i < n - 1:
            term *= (y - y_values[i])

    # Simplificar el polinomio
    polynomial = sp.simplify(polynomial)
    return polynomial

# Interpolación con Splines Lineales
def linear_spline(x, x_data, y_data):
    n = len(x_data)
    for i in range(n - 1):
        if x >= x_data[i] and x < x_data[i + 1]:
            m = (y_data[i + 1] - y_data[i]) / (x_data[i + 1] - x_data[i])
            return m * (x - x_data[i]) + y_data[i]
    return None

# Coeficientes de Splines Cúbicos
def cubic_spline_coefficients(x, y):
    n = len(x) - 1
    h = np.diff(x)
    alpha = np.zeros(n)

    for i in range(1, n):
        alpha[i] = (3/h[i])*(y[i+1]-y[i]) - (3/h[i-1])*(y[i]-y[i-1])

    l = np.ones(n+1)
    mu = np.zeros(n)
    z = np.zeros(n+1)

    for i in range(1, n):
        l[i] = 2*(x[i+1]-x[i-1]) - h[i-1]*mu[i-1]
        mu[i] = h[i]/l[i]
        z[i] = (alpha[i]-h[i-1]*z[i-1])/l[i]

    b = np.zeros(n)
    c = np.zeros(n+1)
    d = np.zeros(n)

    for i in range(n-1, -1, -1):
        c[i] = z[i] - mu[i]*c[i+1]
        b[i] = (y[i+1]-y[i])/h[i] - h[i]*(c[i+1]+2*c[i])/3
        d[i] = (c[i+1]-c[i])/(3*h[i])

    return y[:-1], b, c[:-1], d

def cubic_spline_eval(x, y, b, c, d, xx):
    n = len(x) - 1
    for i in range(n):
        if x[i] <= xx <= x[i+1]:
            dx = xx - x[i]
            return y[i] + b[i]*dx + c[i]*dx**2 + d[i]*dx**3
    return None

# Datos de ejemplo
x_values = [2, 3, 4, 5]
y_values = [1.20, 1.91, 2.41, 2.80]

# Polinomio de Lagrange
polynomial_lagrange = lagrange_interpolation(x_values, y_values)
print(f"Polinomio de Lagrange simplificado: {polynomial_lagrange}")

# Polinomio de Newton
polynomial_newton = newton_interpolation(x_values, y_values)
print(f"Polinomio de Newton simplificado: {polynomial_newton}")

# Polinomio de Interpolación Inversa de Lagrange
polynomial_inverse_lagrange = lagrange_interpolation_inverse_polynomial(x_values, y_values)
print(f"Polinomio de interpolación inversa de Lagrange simplificado: {polynomial_inverse_lagrange}")

# Polinomio de Interpolación Inversa de Newton
polynomial_inverse_newton = newton_interpolation_inverse_polynomial(x_values, y_values)
print(f"Polinomio de interpolación inversa de Newton simplificado: {polynomial_inverse_newton}")

# Evaluar y graficar interpolación de Lagrange
x_point = 3.3
y_interp = polynomial_lagrange.subs('x', x_point)
print(f"\nValor interpolado de Lagrange en {x_point}: {y_interp}")

# Evaluar y graficar interpolación de Newton
x_point = 3.5
y_interp_newton = polynomial_newton.subs('x', x_point)
print(f"Valor interpolado de Newton en {x_point}: {y_interp_newton}")

# Gráfica del polinomio de Lagrange
y_plot = np.linspace(min(y_values), max(y_values), 400)
x_plot_lagrange = [polynomial_lagrange.subs('x', val) for val in y_plot]

plt.figure(figsize=(10, 6))
plt.plot(y_plot, x_plot_lagrange, label='Interpolación Lagrange', color='blue')
plt.scatter(y_values, x_values, color='red', label='Puntos originales')
plt.title('Interpolación de Lagrange')
plt.xlabel('y')
plt.ylabel('x')
plt.legend()
plt.grid(True)
plt.show()

# Gráfica del polinomio de Newton
x_plot_newton = [polynomial_newton.subs('x', val) for val in y_plot]

plt.figure(figsize=(10, 6))
plt.plot(y_plot, x_plot_newton, label='Interpolación Newton', color='green')
plt.scatter(y_values, x_values, color='red', label='Puntos originales')
plt.title('Interpolación de Newton')
plt.xlabel('y')
plt.ylabel('x')
plt.legend()
plt.grid(True)
plt.show()

# Interpolación con Splines Lineales
x_data = np.array([3, 4.5, 7, 9])
y_data = np.array([2.5, 1, 2.5, 0.5])

x_val = 5
y_val = linear_spline(x_val, x_data, y_data)
print(f"El valor de la función en x = {x_val} (Spline Lineal) es y = {y_val}")

# Gráfica de Splines Lineales
x_plot_spline = np.linspace(min(x_data), max(x_data), 400)
y_plot_spline = [linear_spline(x, x_data, y_data) for x in x_plot_spline]

plt.figure(figsize=(10, 6))
plt.plot(x_data, y_data, 'o', label='Datos originales')
plt.plot(x_plot_spline, y_plot_spline, '-', label='Spline lineal')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interpolación con Splines Lineales')
plt.legend()
plt.grid(True)
plt.show()

# Interpolación Cúbica
a, b, c, d = cubic_spline_coefficients(x_data, y_data)

# Evaluar y graficar splines cúbicos
xx = np.linspace(min(x_data), max(x_data), 100)
yy = [cubic_spline_eval(x_data, a, b, c, d, x) for x in xx]

plt.figure(figsize=(10, 6))
plt.plot(x_data, y_data, 'o', label='Datos originales')
plt.plot(xx, yy, '-', label='Spline cúbico')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interpolación con Splines Cúbicos')
plt.legend()
plt.grid(True)
plt.show()
