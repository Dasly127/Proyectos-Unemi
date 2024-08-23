

# main.py

from clases import MatrizEstudiantes

def mostrar_menu():
    print("\nMenú de opciones:")
    print("1. Agregar estudiante")
    print("2. Modificar datos de un estudiante")
    print("3. Cambiar estado de un estudiante")
    print("4. Mostrar todos los estudiantes")
    print("5. Salir")

    opcion = input("Ingrese el número de la opción que desea realizar: ")
    return opcion

def main():
    matriz_estudiantes = MatrizEstudiantes()

    while True:
        opcion = mostrar_menu()

        if opcion == "1":
            matriz_estudiantes.agregar_estudiante()
        elif opcion == "2":
            matriz_estudiantes.modificar_estudiante()
        elif opcion == "3":
            matriz_estudiantes.cambiar_estado_estudiante()
        elif opcion == "4":
            matriz_estudiantes.mostrar_estudiantes()
        elif opcion == "5":
            print("¡Gracias por usar el programa del grupo 5!")
            break
        else:
            print("Opción inválida. Por favor, ingrese un número del 1 al 5.")

if __name__ == "__main__":
    main()
