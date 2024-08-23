import sys
import math
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import messagebox
from tkinter.simpledialog import askfloat

def validar_entrada(valor, nombre, min_val=0, max_val=float('inf')):
    """
    Valida que un valor de entrada esté dentro de un rango específico.
    Entradas:
        - valor: Valor a validar.
        - nombre: Nombre del valor para mostrar en mensajes de error.
        - min_val: Valor mínimo permitido.
        - max_val: Valor máximo permitido.
    Salida:
        - True si la validación es exitosa.
        - False si la validación falla.
    """
    if valor is None:
        messagebox.showerror("Error", f"{nombre} no puede estar vacío.")
        return False
    if valor <= min_val or valor > max_val:
        messagebox.showerror("Error", f"{nombre} debe ser un número positivo y menor que {max_val}.")
        return False
    return True

def datos_digitales_senales_digitales():
    """
    Calcula y muestra la velocidad de modulación para señales digitales.
    Entradas:
        - R: Velocidad de transmisión.
        - L: Número de niveles de la señal.
        - M: Número de posibles símbolos.
    Proceso:
        - Solicita al usuario las entradas necesarias.
        - Calcula la velocidad de modulación usando dos fórmulas.
        - Muestra los resultados en un cuadro de diálogo.
    Salida:
        - Velocidades de modulación Vm1 y Vm2.
    """
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
    """
    Genera señales para la Modulación por Desplazamiento de Amplitud (ASK).
    Entradas:
        - fc: Frecuencia de la portadora.
        - t: Vector de tiempo.
    Proceso:
        - Calcula la señal modulada para un bit 1 (s_t_1) y un bit 0 (s_t_0).
    Salida:
        - Señales s_t_1 y s_t_0.
    """
    try:
        A = 1
        pi = 3.1416
        s_t_1 = A * np.cos(2 * pi * fc * t)
        s_t_0 = np.zeros_like(t)
        return s_t_1, s_t_0
    except Exception as e:
        messagebox.showerror("Error", f"Se produjo un error en ASK: {e}")

def psk(fc, t):
    """
    Genera señales para la Modulación por Desplazamiento de Fase (PSK).
    Entradas:
        - fc: Frecuencia de la portadora.
        - t: Vector de tiempo.
    Proceso:
        - Calcula la señal modulada para un bit 1 (s_t_1) y un bit 0 (s_t_0).
    Salida:
        - Señales s_t_1 y s_t_0.
    """
    try:
        A = 1
        pi = 3.1416
        s_t_1 = A * np.cos(2 * pi * fc * t + pi)
        s_t_0 = A * np.cos(2 * pi * fc * t)
        return s_t_1, s_t_0
    except Exception as e:
        messagebox.showerror("Error", f"Se produjo un error en PSK: {e}")

def psk_multinivel(fc, t):
    """
    Genera señales para la Modulación por Desplazamiento de Fase de múltiples niveles (PSK multinivel).
    Entradas:
        - fc: Frecuencia de la portadora.
        - t: Vector de tiempo.
    Proceso:
        - Calcula señales moduladas para diferentes niveles de fase (s_t_1, s_t_2, s_t_3, s_t_4).
    Salida:
        - Señales s_t_1, s_t_2, s_t_3 y s_t_4.
    """
    try:
        A = 1
        pi = 3.1416
        s_t_1 = A * np.cos(2 * pi * fc * t + pi / 4)  # π/4
        s_t_2 = A * np.cos(2 * pi * fc * t + 3 * pi / 4)  # 3π/4
        s_t_3 = A * np.cos(2 * pi * fc * t - 3 * pi / 4)  # -3π/4
        s_t_4 = A * np.cos(2 * pi * fc * t - pi / 4)  # -π/4
        return s_t_1, s_t_2, s_t_3, s_t_4
    except Exception as e:
        messagebox.showerror("Error", f"Se produjo un error en PSK multinivel: {e}")

def datos_digitales_senales_analogicas():
    """
    Genera y muestra señales para ASK y PSK basadas en datos digitales.
    Entradas:
        - fc: Frecuencia de la portadora.
    Proceso:
        - Solicita la frecuencia de la portadora al usuario.
        - Genera señales para ASK y PSK.
        - Muestra las señales generadas en gráficos.
    Salida:
        - Gráficos de las señales moduladas.
    """
    try:
        fc = askfloat("Entrada", "Ingrese la frecuencia de la portadora (fc): ")
        if not validar_entrada(fc, "Frecuencia de la portadora (fc)", 0, 1e9):
            return

        t = np.linspace(0, 1, 1000)
        
        # Mostrar ASK
        s_t_1_ask, s_t_0_ask = ask(fc, t)
        plt.figure()
        plt.plot(t, s_t_1_ask, label='ASK 1')
        plt.plot(t, s_t_0_ask, label='ASK 0')
        plt.legend()
        plt.title('ASK')
        plt.show()
        
        # Mostrar PSK
        s_t_1_psk, s_t_0_psk = psk(fc, t)
        plt.figure()
        plt.plot(t, s_t_1_psk, label='PSK 1')
        plt.plot(t, s_t_0_psk, label='PSK 0')
        plt.legend()
        plt.title('PSK')
        plt.show()

        # Mostrar PSK multinivel
        s_t_1_psk, s_t_2_psk, s_t_3_psk, s_t_4_psk = psk_multinivel(fc, t)
        plt.figure()
        plt.plot(t, s_t_1_psk, label='PSK π/4')
        plt.plot(t, s_t_2_psk, label='PSK 3π/4')
        plt.plot(t, s_t_3_psk, label='PSK -3π/4')
        plt.plot(t, s_t_4_psk, label='PSK -π/4')
        plt.legend()
        plt.title('PSK multinivel')
        plt.show()

    except Exception as e:
        messagebox.showerror("Error", f"Se produjo un error: {e}")

def am_modulation(fc, fm, t, m):
    """
    Genera señales para la Modulación de Amplitud (AM).
    Entradas:
        - fc: Frecuencia de la portadora.
        - fm: Frecuencia del mensaje.
        - t: Vector de tiempo.
        - m: Índice de modulación.
    Proceso:
        - Calcula la señal modulada en amplitud.
    Salida:
        - Señal modulada s_t.
    """
    try:
        A = 1
        pi = 3.1416
        s_t = (1 + m * np.cos(2 * pi * fm * t)) * np.cos(2 * pi * fc * t)
        return s_t
    except Exception as e:
        messagebox.showerror("Error", f"Se produjo un error en AM: {e}")

def fm_modulation(fc, fm, t, beta):
    """
    Genera señales para la Modulación de Frecuencia (FM).
    Entradas:
        - fc: Frecuencia de la portadora.
        - fm: Frecuencia del mensaje.
        - t: Vector de tiempo.
        - beta: Índice de modulación.
    Proceso:
        - Calcula la señal modulada en frecuencia.
    Salida:
        - Señal modulada s_t.
    """
    try:
        A = 1
        pi = 3.1416
        s_t = A * np.cos(2 * pi * fc * t + beta * np.sin(2 * pi * fm * t))
        return s_t
    except Exception as e:
        messagebox.showerror("Error", f"Se produjo un error en FM: {e}")

def datos_analogicos_senales_analogicas():
    """
    Genera y muestra señales para AM y FM basadas en datos analógicos.
    Entradas:
        - fc: Frecuencia de la portadora.
        - fm: Frecuencia del mensaje.
        - m: Índice de modulación para AM.
        - beta: Índice de modulación para FM.
    Proceso:
        - Solicita las frecuencias e índices de modulación al usuario.
        - Genera señales para AM y FM.
        - Muestra las señales generadas en gráficos.
    Salida:
        - Gráficos de las señales moduladas.
    """
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
 
    """
    Genera y muestra señales para AM y FM basadas en datos analógicos.
    Entradas:
        - fc: Frecuencia de la portadora.
        - fm: Frecuencia del mensaje.
        - m: Índice de modulación para AM.
        - beta: Índice de modulación para FM.
    Proceso:
        - Solicita las frecuencias e índices de modulación al usuario.
        - Genera señales para AM y FM.
        - Muestra las señales generadas en gráficos.
    Salida:
        - Gráficos de las señales moduladas.
    """
    
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
