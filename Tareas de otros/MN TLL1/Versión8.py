

import numpy as np
import matplotlib.pyplot as plt

def ajustar_datos(edades, horas_uso):
    """Ajusta los datos utilizando el método de mínimos cuadrados."""
    coeficientes = np.polyfit(edades, horas_uso, 1)
    polinomio = np.poly1d(coeficientes)
    return coeficientes, polinomio

def calcular_r_cuadrado(edades, horas_uso, polinomio):
    """Calcula el coeficiente de determinación R²."""
    residuos = horas_uso - polinomio(edades)
    SS_residuos = np.sum(residuos**2)
    SS_total = np.sum((horas_uso - np.mean(horas_uso))**2)
    return 1 - (SS_residuos / SS_total)

def graficar_datos(edades, horas_uso, polinomio, r_cuadrado):
    """Grafica los datos y el ajuste lineal."""
    x_linea = np.linspace(min(edades), max(edades), 100)
    y_linea = polinomio(x_linea)
    
    plt.scatter(edades, horas_uso, color='blue', label='Datos')
    plt.plot(x_linea, y_linea, color='red', label='Ajuste lineal')
    plt.title(f'Ajuste lineal de Horas de Uso vs Edad\nR² = {r_cuadrado:.2f}')
    plt.xlabel('Edad (años)')
    plt.ylabel('Horas de uso diarias')
    plt.legend()
    plt.grid()
    plt.show()

def main():
    # Datos obtenidos
    edades = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
    horas_uso = np.array([1, 0.5, 2, 3, 2.5, 1.5, 2, 1, 3, 2, 2, 4, 5])
    
    # Ajuste de datos
    coeficientes, polinomio = ajustar_datos(edades, horas_uso)
    
    # Calcular R2
    r_cuadrado = calcular_r_cuadrado(edades, horas_uso, polinomio)
    
    # Graficar resultados
    graficar_datos(edades, horas_uso, polinomio, r_cuadrado)
    
    # Imprimir resultados
    print(f'Coeficientes de la recta: {coeficientes}')
    print(f'Coeficiente de determinación (R²): {r_cuadrado:.4f}')

if __name__ == "__main__":
    main()
