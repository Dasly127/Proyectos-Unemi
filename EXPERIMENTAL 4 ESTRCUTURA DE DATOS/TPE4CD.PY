import sys
import math
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import messagebox
from tkinter.simpledialog import askfloat

def datos_digitales_senales_digitales():
    R = askfloat("Entrada", "Ingrese la velocidad de transmisión (R): ")
    L = askfloat("Entrada", "Ingrese el número de niveles de la señal (L): ")
    M = askfloat("Entrada", "Ingrese el número de posibles símbolos (M): ")
    
    Vm1 = R / L
    Vm2 = R / math.log2(M)
    
    messagebox.showinfo("Resultados", f"Velocidad de modulación usando Vm = R / L: {Vm1}\nVelocidad de modulación usando Vm = R / log2(M): {Vm2}")

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
    fc = askfloat("Entrada", "Ingrese la frecuencia de la portadora (fc): ")
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
    fc = askfloat("Entrada", "Ingrese la frecuencia de la portadora (fc): ")
    fm = askfloat("Entrada", "Ingrese la frecuencia del mensaje (fm): ")
    m = askfloat("Entrada", "Ingrese el índice de modulación para AM (m): ")
    beta = askfloat("Entrada", "Ingrese el índice de modulación para FM (beta): ")
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

def mostrar_menu():
    root = tk.Tk()
    root.title("Trabajo práctico de Comunicación de Datos")

    frame = tk.Frame(root, padx=10, pady=10)
    frame.pack()

    label_title = tk.Label(frame, text="Trabajo práctico de Comunicación de Datos", font=("Arial", 14, "bold"))
    label_title.grid(row=0, column=0, columnspan=2, pady=5)

    autores = tk.Label(frame, text="Realizado por:\nDíaz, Echeverría, Flores, Méndez, Rodríguez & Vera (2024)", font=("Arial", 12))
    autores.grid(row=1, column=0, columnspan=2, pady=5)

    label_subtitle = tk.Label(frame, text="Modulación y codificación de datos", font=("Arial", 12, "bold"))
    label_subtitle.grid(row=2, column=0, columnspan=2, pady=10)

    btn1 = tk.Button(frame, text="1. Datos digitales, señales digitales", command=datos_digitales_senales_digitales)
    btn1.grid(row=3, column=0, columnspan=2, pady=5, sticky="w")

    btn2 = tk.Button(frame, text="2. Datos digitales, señales analógicas", command=datos_digitales_senales_analogicas)
    btn2.grid(row=4, column=0, columnspan=2, pady=5, sticky="w")

    btn3 = tk.Button(frame, text="3. Datos analógicos, señales analógicas", command=datos_analogicos_senales_analogicas)
    btn3.grid(row=5, column=0, columnspan=2, pady=5, sticky="w")

    btn4 = tk.Button(frame, text="4. Salir", command=root.quit)
    btn4.grid(row=6, column=0, columnspan=2, pady=5, sticky="w")

    label_footer = tk.Label(frame, text="Elija una opción [1 – 4]:", font=("Arial", 10))
    label_footer.grid(row=7, column=0, columnspan=2, pady=10)

    version = tk.Label(frame, text="Versión 1.0", font=("Arial", 8))
    version.grid(row=8, column=1, sticky="e")

    root.mainloop()

if __name__ == "__main__":
    mostrar_menu()
