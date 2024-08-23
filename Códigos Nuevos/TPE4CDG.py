import sys
import math
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import messagebox
from tkinter.simpledialog import askfloat

def validar_entrada(valor, nombre, min_val=0, max_val=float('inf')):
    if valor is None:
        messagebox.showerror("Error", f"{nombre} no puede estar vacío.")
        return False
    if valor <= min_val or valor > max_val:
        messagebox.showerror("Error", f"{nombre} debe ser un número positivo y menor que {max_val}.")
        return False
    return True

def datos_digitales_senales_digitales():
    try:
        R = askfloat("Entrada", "Ingrese la velocidad de transmisión (R): ")
        if not validar_entrada(R, "Velocidad de transmisión (R)"):
            return

        L = askfloat("Entrada", "Ingrese el número de niveles de la señal (L): ")
        if not validar_entrada(L, "Número de niveles de la señal (L)"):
            return

        M = askfloat("Entrada", "Ingrese el número de posibles símbolos (M): ")
        if not validar_entrada(M, "Número de posibles símbolos (M)"):
            return

        Vm1 = R / L
        Vm2 = R / math.log2(M)
        
        messagebox.showinfo("Resultados", f"Velocidad de modulación usando Vm = R / L: {Vm1}\nVelocidad de modulación usando Vm = R / log2(M): {Vm2}")

    except Exception as e:
        messagebox.showerror("Error", f"Se produjo un error: {e}")

def ask(fc, t):
    try:
        A = 1
        s_t_1 = A * np.cos(2 * np.pi * fc * t)
        s_t_0 = np.zeros_like(t)
        return s_t_1, s_t_0
    except Exception as e:
        messagebox.showerror("Error", f"Se produjo un error en ASK: {e}")

def psk(fc, t):
    try:
        A = 1
        s_t_1 = A * np.cos(2 * np.pi * fc * t + np.pi)
        s_t_0 = A * np.cos(2 * np.pi * fc * t)
        return s_t_1, s_t_0
    except Exception as e:
        messagebox.showerror("Error", f"Se produjo un error en PSK: {e}")

def datos_digitales_senales_analogicas():
    try:
        fc = askfloat("Entrada", "Ingrese la frecuencia de la portadora (fc): ")
        if not validar_entrada(fc, "Frecuencia de la portadora (fc)", 0, 1e9):
            return

        t = np.linspace(0, 1, 1000)
        
        s_t_1_ask, s_t_0_ask = ask(fc, t)
        plt.figure()
        plt.plot(t, s_t_1_ask, label='ASK 1')
        plt.plot(t, s_t_0_ask, label='ASK 0')
        plt.legend()
        plt.title('ASK')
        plt.show()
        
        s_t_1_psk, s_t_0_psk = psk(fc, t)
        plt.figure()
        plt.plot(t, s_t_1_psk, label='PSK 1')
        plt.plot(t, s_t_0_psk, label='PSK 0')
        plt.legend()
        plt.title('PSK')
        plt.show()

    except Exception as e:
        messagebox.showerror("Error", f"Se produjo un error: {e}")

def am_modulation(fc, fm, t, m):
    try:
        A = 1
        s_t = (1 + m * np.cos(2 * np.pi * fm * t)) * np.cos(2 * np.pi * fc * t)
        return s_t
    except Exception as e:
        messagebox.showerror("Error", f"Se produjo un error en AM: {e}")

def fm_modulation(fc, fm, t, beta):
    try:
        A = 1
        s_t = A * np.cos(2 * np.pi * fc * t + beta * np.sin(2 * np.pi * fm * t))
        return s_t
    except Exception as e:
        messagebox.showerror("Error", f"Se produjo un error en FM: {e}")

def datos_analogicos_senales_analogicas():
    try:
        fc = askfloat("Entrada", "Ingrese la frecuencia de la portadora (fc): ")
        if not validar_entrada(fc, "Frecuencia de la portadora (fc)", 0, 1e9):
            return

        fm = askfloat("Entrada", "Ingrese la frecuencia del mensaje (fm): ")
        if not validar_entrada(fm, "Frecuencia del mensaje (fm)", 0, 1e9):
            return

        m = askfloat("Entrada", "Ingrese el índice de modulación para AM (m): ")
        if not validar_entrada(m, "Índice de modulación para AM (m)", 0, 1):
            return

        beta = askfloat("Entrada", "Ingrese el índice de modulación para FM (beta): ")
        if not validar_entrada(beta, "Índice de modulación para FM (beta)", 0, 10):
            return

        t = np.linspace(0, 1, 1000)
        
        s_t_am = am_modulation(fc, fm, t, m)
        plt.figure()
        plt.plot(t, s_t_am, label='AM')
        plt.legend()
        plt.title('Modulación de Amplitud (AM)')
        plt.show()
        
        s_t_fm = fm_modulation(fc, fm, t, beta)
        plt.figure()
        plt.plot(t, s_t_fm, label='FM')
        plt.legend()
        plt.title('Modulación Angular (FM)')
        plt.show()

    except Exception as e:
        messagebox.showerror("Error", f"Se produjo un error: {e}")

def mostrar_menu():
    try:
        root = tk.Tk()
        root.title("Trabajo práctico de Comunicación de Datos")

        frame = tk.Frame(root, padx=10, pady=10)
        frame.pack()

        label_title = tk.Label(frame, text="Trabajo práctico de Comunicación de Datos", font=("Arial", 14, "bold"))
        label_title.grid(row=0, column=0, columnspan=2, pady=5)

        autores = tk.Label(frame, text="Realizado por:\nSantana, Guadamud, Flores, Cruz & Delgado (2024)", font=("Arial", 12))
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
    except Exception as e:
        messagebox.showerror("Error", f"Se produjo un error en la interfaz: {e}")

if __name__ == "__main__":
    mostrar_menu()
