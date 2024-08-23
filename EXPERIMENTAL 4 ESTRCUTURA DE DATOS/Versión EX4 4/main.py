"""

TPE # 4: El trabajo práctico experimental # 1 debe actualizarlo utilizando listas, respetando el 
programa principal y la clase solicitada. 
___________________________________________________________________________________________________

Consideraciones generales
-. Si el programa no se implementa con POO la nota es de CERO. 
-. Si el programa no funciona, se cae o presenta un error la nota es de CERO 
-. Copia o similitud de código, la nota es de CERO para todos los involucrados. 
-. Si por alguna razón, al revisar por ejemplo el 2do requerimiento el programa se cae, el 
equipo recibe la nota que hasta ese momento obtuvo, y finaliza la revisión. 

___________________________________________________________________________________________________

Criterios que considera la rúbrica:
    Procesos: cumplimiento y funcionamiento 
    Validación del programa 
    Estructuras y formato solicitado 

"""

#Para ejecutar el programa, simplemente corre main.py. 
#El menú de opciones se mostrará, y se podrá interactuar con él 
# ingresando el número de la opción que desees realizar.


#Importamos el Módulo con las clases
from clases import PilaEstudiantes

#Menú Principal
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

"""
FUNCIONES DEL MENÚ:

    ¬ mostrar_menu()
    Muestra el menú de opciones y solicita al usuario que elija una opción. Devuelve la opción elegida como una cadena.

    
    ¬ main()
    Función principal que inicializa una instancia de PilaEstudiantes y gestiona el ciclo de vida del programa, 
    llamando a los métodos correspondientes de PilaEstudiantes según la opción elegida por el usuario.


MENÚ DE OPCIONES: 

¬ Agregar estudiante
Llama al método agregar_estudiante() de PilaEstudiantes.

¬ Modificar datos de un estudiante
Llama al método modificar_estudiante() de PilaEstudiantes.

¬ Cambiar estado de un estudiante
Llama al método cambiar_estado_estudiante() de PilaEstudiantes.

¬ Mostrar todos los estudiantes
Llama al método mostrar_estudiantes() de PilaEstudiantes.

¬ Salir
Finaliza el programa.

"""