

import sys
from digital_signals import datos_digitales_senales_digitales
from analog_signals import datos_digitales_senales_analogicas, datos_analogicos_senales_analogicas

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
