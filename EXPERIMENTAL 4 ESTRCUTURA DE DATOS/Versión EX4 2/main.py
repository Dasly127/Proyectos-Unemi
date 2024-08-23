


from clases import PilaEstudiantes

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
    pila_estudiantes = PilaEstudiantes()

    while True:
        opcion = mostrar_menu()

        if opcion == "1":
            pila_estudiantes.agregar_estudiante()
        elif opcion == "2":
            pila_estudiantes.modificar_estudiante()
        elif opcion == "3":
            pila_estudiantes.cambiar_estado_estudiante()
        elif opcion == "4":
            pila_estudiantes.mostrar_estudiantes()
        elif opcion == "5":
            print("¡Gracias por usar el programa del grupo 5!")
            break
        else:
            print("Opción inválida. Por favor, ingrese un número del 1 al 5.")

if __name__ == "__main__":
    main()
