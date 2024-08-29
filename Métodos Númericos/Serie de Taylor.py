

import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# Definir la variable y la función
x = sp.symbols('x')
f_exp = sp.exp(x)

# Serie de Taylor hasta el orden 4 en el punto a = 0
serie_taylor_exp = sp.series(f_exp, x, 0, 5)  # 5 para incluir términos hasta x^4
print("Serie de Taylor de e^x hasta el orden 4:")
print(serie_taylor_exp)

# Definir la función original y las aproximaciones
f_original = np.exp
f_approx_1 = lambda x: 1 + x
f_approx_2 = lambda x: 1 + x + x**2 / 2
f_approx_3 = lambda x: 1 + x + x**2 / 2 + x**3 / 6
f_approx_4 = lambda x: 1 + x + x**2 / 2 + x**3 / 6 + x**4 / 24

# Rango de valores para x
x_vals = np.linspace(-2, 2, 400)
y_original = f_original(x_vals)
y_approx_1 = f_approx_1(x_vals)
y_approx_2 = f_approx_2(x_vals)
y_approx_3 = f_approx_3(x_vals)
y_approx_4 = f_approx_4(x_vals)

# Graficar las aproximaciones
plt.figure(figsize=(10, 6))
plt.plot(x_vals, y_original, label='f(x) = e^x', color='black')
plt.plot(x_vals, y_approx_1, label='Aprox. 1er orden', linestyle='dashed')
plt.plot(x_vals, y_approx_2, label='Aprox. 2do orden', linestyle='dotted')
plt.plot(x_vals, y_approx_3, label='Aprox. 3er orden', linestyle='dashdot')
plt.plot(x_vals, y_approx_4, label='Aprox. 4to orden', linestyle='solid')

plt.legend()
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Expansión en Serie de Taylor de f(x) = e^x')
plt.grid(True)
plt.show()

# Cálculo del error de truncamiento
error_1 = np.abs(y_original - y_approx_1)
error_2 = np.abs(y_original - y_approx_2)
error_3 = np.abs(y_original - y_approx_3)
error_4 = np.abs(y_original - y_approx_4)

# Graficar los errores
plt.figure(figsize=(10, 6))
plt.plot(x_vals, error_1, label='Error 1er orden')
plt.plot(x_vals, error_2, label='Error 2do orden')
plt.plot(x_vals, error_3, label='Error 3er orden')
plt.plot(x_vals, error_4, label='Error 4to orden')

plt.legend()
plt.xlabel('x')
plt.ylabel('Error de truncamiento')
plt.title('Error de truncamiento en la Serie de Taylor de f(x) = e^x')
plt.grid(True)
plt.show()
