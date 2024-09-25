

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Generar datos de ejemplo (puedes cambiarlos por tus propios datos)
x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y = np.array([2, 3, 5, 7, 11, 13, 17, 19, 23, 25])

# Ajustar la recta mediante regresión lineal
slope, intercept, r_value, p_value, std_err = linregress(x, y)

# Calcular el coeficiente de determinación (R²)
r_squared = r_value ** 2

# Imprimir resultados
print("Pendiente de la recta:", slope)
print("Intersección con el eje y:", intercept)
print("Coeficiente de determinación (R²):", r_squared)

# Graficar los datos y la recta de ajuste
plt.scatter(x, y)
plt.plot(x, slope * x + intercept, color='red')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Ajuste de curvas mediante regresión lineal')
plt.show()

