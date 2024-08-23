
import sys
import math
import numpy as np
import matplotlib.pyplot as plt

def datos_digitales_senales_digitales():
    R = float(input("Ingrese la velocidad de transmisión (R): "))
    L = float(input("Ingrese el número de niveles de la señal (L): "))
    M = float(input("Ingrese el número de posibles símbolos (M): "))
    
    Vm1 = R / L
    Vm2 = R / math.log2(M)
    
    print(f"Velocidad de modulación usando Vm = R / L: {Vm1}")
    print(f"Velocidad de modulación usando Vm = R / log2(M): {Vm2}")

def ask(fc, t):
    A = 1  # Amplitud arbitraria
    s_t_1 = A * np.cos(2 * np.pi * fc * t)
    s_t_0 = np.zeros_like(t)
    return s_t_1, s_t_0

def psk(fc, t):
    A = 1  # Amplitud arbitraria
    s_t_1 = A * np.cos(2 * np.pi * fc * t + np.pi)
    s_t_0 = A * np.cos(2 * np.pi * fc * t)
    return s_t_1, s_t_0

def datos_digitales_senales_analogicas():
    fc = float(input("Ingrese la frecuencia de la portadora (fc): "))
    t = np.linspace(0, 1, 1000)  # Vector de tiempo arbitrario
    
    # ASK
    s_t_1_ask, s_t_0_ask = ask(fc, t)
    plt.figure()
    plt.plot(t, s_t_1_ask, label='ASK 1')
    plt.plot(t, s_t_0_ask, label='ASK 0')
    plt.legend()
    plt.title('ASK')
    plt.show()
    
    # PSK
    s_t_1_psk, s_t_0_psk = psk(fc, t)
    plt.figure()
    plt.plot(t, s_t_1_psk, label='PSK 1')
    plt.plot(t, s_t_0_psk, label='PSK 0')
    plt.legend()
    plt.title('PSK')
    plt.show()

def am_modulation(fc, fm, t, m):
    A = 1  # Amplitud arbitraria
    s_t = (1 + m * np.cos(2 * np.pi * fm * t)) * np.cos(2 * np.pi * fc * t)
    return s_t

def fm_modulation(fc, fm, t, beta):
    A = 1  # Amplitud arbitraria
    s_t = A * np.cos(2 * np.pi * fc * t + beta * np.sin(2 * np.pi * fm * t))
    return s_t

def datos_analogicos_senales_analogicas():
    fc = float(input("Ingrese la frecuencia de la portadora (fc): "))
    fm = float(input("Ingrese la frecuencia del mensaje (fm): "))
    m = float(input("Ingrese el índice de modulación para AM (m): "))
    beta = float(input("Ingrese el índice de modulación para FM (beta): "))
    t = np.linspace(0, 1, 1000)  # Vector de tiempo arbitrario
    
    # AM
    s_t_am = am_modulation(fc, fm, t, m)
    plt.figure()
    plt.plot(t, s_t_am, label='AM')
    plt.legend()
    plt.title('Modulación de Amplitud (AM)')
    plt.show()
    
    # FM
    s_t_fm = fm_modulation(fc, fm, t, beta)
    plt.figure()
    plt.plot(t, s_t_fm, label='FM')
    plt.legend()
    plt.title('Modulación Angular (FM)')
    plt.show()

def menu_principal():
    while True:
        print("Trabajo práctico de Comunicación de Datos")
        print("Realizado por:")
        print("Díaz, Echeverría, Flores, Méndez, Rodríguez & Vera (2024)")
        print("\nModulación y codificación de datos\n")
        print("1. Datos digitales, señales digitales")
        print("2. Datos digitales, señales analógicas")
        print("3. Datos analógicos, señales analógicas")
        print("4. Salir")
        print("\nElija una opción [1 - 4]: ", end='')
        
        opcion = input()
        
        if opcion == '1':
            datos_digitales_senales_digitales()
        elif opcion == '2':
            datos_digitales_senales_analogicas()
        elif opcion == '3':
            datos_analogicos_senales_analogicas()
        elif opcion == '4':
            sys.exit()
        else:
            print("Opción no válida. Inténtelo de nuevo.")

if __name__ == "__main__":
    menu_principal()
