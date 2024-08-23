class Estudiante:
    def __init__(self, cedula, nombre, apellido, n1, n2, ex1, n3, n4, ex2):
        # Usamos un Constructor para inicializar las propiedades del estudiante
        self.cedula = cedula
        self.nombre = nombre
        self.apellido = apellido
        # Almacenamos las notas y exámenes en una lista para facilitar el cálculo del promedio
        self.notas = {'n1': n1, 'n2': n2, 'ex1': ex1, 'n3': n3, 'n4': n4, 'ex2': ex2}

    def calcular_total_notas(self):
        # Método para calcular el total de las notas del estudiante
        total = sum(self.notas.values())
        return total

    def estado_aprobacion(self):
        # Método para determinar el estado de aprobación del estudiante
        if self.calcular_total_notas() >= 70:
            return "Aprobado"
        else:
            return "Reprobado"


estudiantes = []  # Lista para almacenar objetos de la clase Estudiante

def mostrar_menu():
    # Función para mostrar las opciones del menú
    print("\nMenú:")
    print("1. Ingresar estudiante")
    print("2. Mostrar listado de estudiantes")
    print("3. Modificar nombre y apellido del estudiante")
    print("4. Eliminar estudiante")
    print("5. Buscar estudiante por cédula")
    print("6. Mostrar estudiante con mejor promedio")
    print("7. Salir")

def ingresar_estudiante():
    # Función para ingresar un nuevo estudiante
    cedula = input("Cédula del estudiante: ")
    nombre = input("Nombre del estudiante: ")
    apellido = input("Apellido del estudiante: ")

    # Validar y ajustar las notas dentro del rango correcto
    while True:
        try:
            n1 = float(input("Nota 1 (sobre 15): "))
            if 0 <= n1 <= 15:
                break
            else:
                print("La nota debe estar entre 0 y 15. Intenta nuevamente.")
        except ValueError:
            print("Ingresa un número válido.")

    while True:
        try:
            n2 = float(input("Nota 2 (sobre 15): "))
            if 0 <= n2 <= 15:
                break
            else:
                print("La nota debe estar entre 0 y 15. Intenta nuevamente.")
        except ValueError:
            print("Ingresa un número válido.")

    while True:
        try:
            ex1 = float(input("Examen 1 (sobre 20): "))
            if 0 <= ex1 <= 20:
                break
            else:
                print("La nota debe estar entre 0 y 20. Intenta nuevamente.")
        except ValueError:
            print("Ingresa un número válido.")

    while True:
        try:
            n3 = float(input("Nota 3 (sobre 15): "))
            if 0 <= n3 <= 15:
                break
            else:
                print("La nota debe estar entre 0 y 15. Intenta nuevamente.")
        except ValueError:
            print("Ingresa un número válido.")

    while True:
        try:
            n4 = float(input("Nota 4 (sobre 15): "))
            if 0 <= n4 <= 15:
                break
            else:
                print("La nota debe estar entre 0 y 15. Intenta nuevamente.")
        except ValueError:
            print("Ingresa un número válido.")

    while True:
        try:
            ex2 = float(input("Examen 2 (sobre 20): "))
            if 0 <= ex2 <= 20:
                break
            else:
                print("La nota debe estar entre 0 y 20. Intenta nuevamente.")
        except ValueError:
            print("Ingresa un número válido.")

    # Crear un objeto Estudiante y agregarlo a la lista de estudiantes
    estudiante = Estudiante(cedula, nombre, apellido, n1, n2, ex1, n3, n4, ex2)
    estudiantes.append(estudiante)
    
    # Mostrar el total de notas del estudiante recién ingresado y su estado de aprobación
    print(f"Total de notas del estudiante {nombre} {apellido}: {estudiante.calcular_total_notas()}")
    print(f"Estado de aprobación: {estudiante.estado_aprobacion()}")
    print("Estudiante ingresado correctamente.")

def mostrar_listado_estudiantes():
    # Función para mostrar el listado de estudiantes
    if not estudiantes:
        print("No hay estudiantes ingresados.")
        return

    print("\nListado de estudiantes:")
    for estudiante in estudiantes:
        print(f"Cédula: {estudiante.cedula}\nNombre: {estudiante.nombre}\nApellido: {estudiante.apellido}\nTotal de notas: {estudiante.calcular_total_notas()}\nEstado de aprobación: {estudiante.estado_aprobacion()}\n")

def modificar_nombre_apellido():
    # Función para modificar el nombre y apellido de un estudiante
    cedula = input("Cédula del estudiante que desea modificar: ")
    encontrado = False

    # Buscar al estudiante por cédula y modificar su nombre y apellido si se encuentra
    for estudiante in estudiantes:
        if estudiante.cedula == cedula:
            estudiante.nombre = input("Nuevo nombre: ")
            estudiante.apellido = input("Nuevo apellido: ")
            encontrado = True
            print("Nombre y apellido modificados correctamente.")
            break

    if not encontrado:
        print("Estudiante no encontrado.")

def eliminar_estudiante():
    # Función para eliminar un estudiante de la lista
    cedula = input("Cédula del estudiante que desea eliminar: ")
    encontrado = False

    # Buscar al estudiante por cédula y eliminarlo de la lista si se encuentra
    for estudiante in estudiantes:
        if estudiante.cedula == cedula:
            estudiantes.remove(estudiante)
            encontrado = True
            print("Estudiante eliminado correctamente.")
            break

    if not encontrado:
        print("Estudiante no encontrado.")

def buscar_estudiante_por_cedula():
    # Función para buscar un estudiante por su cédula
    cedula = input("Ingrese la cédula del estudiante que desea buscar (o ingrese '0' para salir): ")

    # Verificar si el usuario desea salir
    if cedula == '0':
        print("Saliendo de la búsqueda. ¡Hasta luego!")
        return

    encontrado = False

    # Validar que la cédula ingresada sea numérica
    while not cedula.isdigit():
        print("Por favor, ingrese un número de cédula válido.")
        cedula = input("Ingrese la cédula del estudiante que desea buscar (o ingrese '0' para salir): ")

        # Verificar si el usuario desea salir
        if cedula == '0':
            print("Saliendo de la búsqueda. ¡Hasta luego!")
            return

    # Buscar al estudiante por cédula y mostrar su información si se encuentra
    for estudiante in estudiantes:
        if estudiante.cedula == cedula:
            print(f"Estudiante encontrado:\nCédula: {estudiante.cedula}\nNombre: {estudiante.nombre}\nApellido: {estudiante.apellido}")
            encontrado = True
            break

    if not encontrado:
        print("Estudiante no encontrado.")


def mostrar_mejor_promedio():
    # Usamos la Función para mostrar el estudiante con el mejor promedio
    if not estudiantes:
        print("No hay estudiantes ingresados.")
        return

    # Encontramos al estudiante con el mejor promedio utilizando la función max y la función calcular_total_notas()
    mejor_promedio = max(estudiantes, key=lambda estudiante: estudiante.calcular_total_notas())
    print(f"Estudiante con mejor total de notas:\nCédula: {mejor_promedio.cedula}\nNombre: {mejor_promedio.nombre}\nApellido: {mejor_promedio.apellido}\nTotal de notas: {mejor_promedio.calcular_total_notas()}\nEstado de aprobación: {mejor_promedio.estado_aprobacion()}")


# Bucle principal que muestra el menú y ejecuta las funciones según la opción seleccionada
while True:
    mostrar_menu()
    opcion = input("Seleccione una opción (1-7): ")

    if opcion == "1":
        ingresar_estudiante()
    elif opcion == "2":
        mostrar_listado_estudiantes()
    elif opcion == "3":
        modificar_nombre_apellido()
    elif opcion == "4":
        eliminar_estudiante()
    elif opcion == "5":
        buscar_estudiante_por_cedula()
    elif opcion == "6":
        mostrar_mejor_promedio()
    elif opcion == "7":
        print("Saliendo del programa. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")


