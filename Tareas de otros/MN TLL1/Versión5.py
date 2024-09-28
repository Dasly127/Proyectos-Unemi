

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Datos del problema (Características del edificio)
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
    [0.86, 588.00, 294.00, 147.00, 7.00, 3, 0.00, 0]
])

# Asegurando que Y1 y Y2 tengan el mismo tamaño que X
Y1 = np.array([15.55, 15.55, 15.55, 15.55, 20.84, 21.46, 20.71, 19.68, 19.50, 19.95])
Y2 = np.array([21.33, 21.33, 21.33, 21.33, 28.28, 25.38, 25.16, 29.60, 27.30, 21.97])

# División de datos en entrenamiento y prueba (80% entrenamiento, 20% prueba)
X_train, X_test, Y1_train, Y1_test = train_test_split(X, Y1, test_size=0.2, random_state=42)
X_train, X_test, Y2_train, Y2_test = train_test_split(X, Y2, test_size=0.2, random_state=42)

# Modelo de regresión lineal para Carga de Calefacción (Y1)
model_Y1 = LinearRegression()
model_Y1.fit(X_train, Y1_train)
Y1_pred = model_Y1.predict(X_test)

# Modelo de regresión lineal para Carga de Enfriamiento (Y2)
model_Y2 = LinearRegression()
model_Y2.fit(X_train, Y2_train)
Y2_pred = model_Y2.predict(X_test)

# Gráfico para la Carga de Calefacción (Y1)
plt.figure(figsize=(10, 5))
plt.scatter(Y1_test, Y1_pred, color='blue', label='Predicciones Y1')
plt.plot([Y1_test.min(), Y1_test.max()], [Y1_test.min(), Y1_test.max()], color='red', lw=2, label='Referencia')
plt.title('Predicciones vs Reales para Carga de Calefacción (Y1)')
plt.xlabel('Carga de Calefacción Real (Y1)')
plt.ylabel('Carga de Calefacción Predicha (Y1)')
plt.legend()
plt.show()

# Gráfico para la Carga de Enfriamiento (Y2)
plt.figure(figsize=(10, 5))
plt.scatter(Y2_test, Y2_pred, color='green', label='Predicciones Y2')
plt.plot([Y2_test.min(), Y2_test.max()], [Y2_test.min(), Y2_test.max()], color='orange', lw=2, label='Referencia')
plt.title('Predicciones vs Reales para Carga de Enfriamiento (Y2)')
plt.xlabel('Carga de Enfriamiento Real (Y2)')
plt.ylabel('Carga de Enfriamiento Predicha (Y2)')
plt.legend()
plt.show()

