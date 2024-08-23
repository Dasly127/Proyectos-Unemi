

import math

def datos_digitales_senales_digitales():
    R = float(input("Ingrese la velocidad de transmisión (R): "))
    L = float(input("Ingrese el número de niveles de la señal (L): "))
    M = float(input("Ingrese el número de posibles símbolos (M): "))
    
    Vm1 = R / L
    Vm2 = R / math.log2(M)
    
    print(f"Velocidad de modulación usando Vm = R / L: {Vm1}")
    print(f"Velocidad de modulación usando Vm = R / log2(M): {Vm2}")


