


import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Datos completos del problema
X = np.array([
    [0.98, 514.50, 294.00, 110.25, 7.00, 2, 0.00, 0],
    [0.98, 514.50, 294.00, 110.25, 7.00, 3, 0.00, 0],
    [0.98, 514.50, 294.00, 110.25, 7.00, 4, 0.00, 0],
    [0.98, 514.50, 294.00, 110.25, 7.00, 5, 0.00, 0],
    [0.90, 563.50, 318.50, 122.50, 7.00, 2, 0.00, 0],
    [0.90, 563.50, 318.50, 122.50, 7.00, 3, 0.00, 0],
    [0.90, 563.50, 318.50, 122.50, 7.00, 4, 0.00, 0],
    [0.90, 563.50, 318.50, 122.50, 7.00, 5, 0.00, 0],
    [0.86, 588.00, 294.00, 147.00, 7.00, 2, 0.00, 0],
    [0.86, 588.00, 294.00, 147.00, 7.00, 3, 0.00, 0],
    [0.86, 588.00, 294.00, 147.00, 7.00, 4, 0.00, 0],
    [0.86, 588.00, 294.00, 147.00, 7.00, 5, 0.00, 0],
    [0.82, 612.50, 318.50, 147.00, 7.00, 2, 0.00, 0],
    [0.82, 612.50, 318.50, 147.00, 7.00, 3, 0.00, 0],
    [0.82, 612.50, 318.50, 147.00, 7.00, 4, 0.00, 0],
    [0.82, 612.50, 318.50, 147.00, 7.00, 5, 0.00, 0],
    [0.79, 637.00, 343.00, 147.00, 7.00, 2, 0.00, 0],
    [0.79, 637.00, 343.00, 147.00, 7.00, 3, 0.00, 0],
    [0.79, 637.00, 343.00, 147.00, 7.00, 4, 0.00, 0],
    [0.79, 637.00, 343.00, 147.00, 7.00, 5, 0.00, 0]
])

Y1 = np.array([15.55, 15.55, 15.55, 15.55, 20.84, 21.46, 20.71, 19.68, 19.50, 19.95, 19.34, 18.31, 17.05, 17.41, 16.95, 15.98, 28.52, 29.90, 29.63, 28.75])  # Carga de Calefacción
Y2 = np.array([21.33, 21.33, 21.33, 21.33, 28.28, 25.38, 25.16, 29.60, 27.30, 21.97, 23.49, 27.87, 23.77, 21.46, 21.16, 24.93, 37.73, 31.27, 30.93, 39.44])  # Carga de Enfriamiento

# Ajuste de regresión lineal para Y1 (Carga de Calefacción)
model_Y1 = LinearRegression()
model_Y1.fit(X, Y1)
Y1_pred = model_Y1.predict(X)

# Ajuste de regresión lineal para Y2 (Carga de Enfriamiento)
model_Y2 = LinearRegression()
model_Y2.fit(X, Y2)
Y2_pred = model_Y2.predict(X)

# Gráfico para Y1 (Carga de Calefacción)
plt.figure(figsize=(10, 5))
plt.scatter(np.arange(len(Y1)), Y1, color='blue', label='Datos originales (Y1)')
plt.plot(np.arange(len(Y1)), Y1_pred, color='red', label='Recta de ajuste (Y1)')
plt.title('Ajuste de mínimos cuadrados para Carga de Calefacción (Y1)')
plt.xlabel('Índice de muestra')
plt.ylabel('Carga de Calefacción (Y1)')
plt.legend()
plt.show()

# Gráfico para Y2 (Carga de Enfriamiento)
plt.figure(figsize=(10, 5))
plt.scatter(np.arange(len(Y2)), Y2, color='green', label='Datos originales (Y2)')
plt.plot(np.arange(len(Y2)), Y2_pred, color='orange', label='Recta de ajuste (Y2)')
plt.title('Ajuste de mínimos cuadrados para Carga de Enfriamiento (Y2)')
plt.xlabel('Índice de muestra')
plt.ylabel('Carga de Enfriamiento (Y2)')
plt.legend()
plt.show()

# Cálculo del Coeficiente de Determinación (R²) para Y1
R2_Y1 = model_Y1.score(X, Y1)
print("Coeficiente de Determinación (R²) para Y1:", R2_Y1)

# Cálculo del Coeficiente de Determinación (R²) para Y2
R2_Y2 = model_Y2.score(X, Y2)
print("Coeficiente de Determinación (R²) para Y2:", R2_Y2)


