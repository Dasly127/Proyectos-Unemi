class Estudiante:
    def __init__(self, cedula, nombre, apellido, nota1, nota2, examen1, nota3, nota4, examen2):
        self.cedula = cedula
        self.nombre = nombre
        self.apellido = apellido
        self.notas = {'nota1': nota1, 'nota2': nota2, 'examen1': examen1, 'nota3': nota3, 'nota4': nota4, 'examen2': examen2}

    def calcular_total_notas(self):
        total = sum(self.notas.values())
        return total

    def estado_aprobacion(self):
        return "Aprobado" if self.calcular_total_notas() >= 70 else "Reprobado"


estudiantes = []

def mostrar_menu():
    print("\nMenú:")
    print("1. Ingresar alumno")
    print("2. Mostrar listado de alumnos")
    print("3. Modificar nombre y apellido del alumno")
    print("4. Eliminar alumno")
    print("5. Encontrar Alumno por cédula")
    print("6. Indicar el mejor alumno con mejor promedio")
    print("7. Salir del programa")

def ingresar_estudiante():
    cedula = input("Cédula del alumno: ")
    nombre = input("Nombre del alumno: ")
    apellido = input("Apellido del alumno: ")

    def ingresar_nota(mensaje, rango):
        while True:
            try:
                nota = float(input(f"{mensaje} (sobre {rango}): "))
                if 0 <= nota <= rango:
                    return nota
                else:
                    print(f"La nota debe estar entre 0 y {rango}. Intenta nuevamente.")
            except ValueError:
                print("Ingresa un número válido.")

    nota1 = ingresar_nota("Nota 1", 15)
    nota2 = ingresar_nota("Nota 2", 15)
    examen1 = ingresar_nota("Examen 1", 20)
    nota3 = ingresar_nota("Nota 3", 15)
    nota4 = ingresar_nota("Nota 4", 15)
    examen2 = ingresar_nota("Examen 2", 20)

    estudiante = Estudiante(cedula, nombre, apellido, nota1, nota2, examen1, nota3, nota4, examen2)
    estudiantes.append(estudiante)

    print(f"Total de notas del alumno {nombre} {apellido}: {estudiante.calcular_total_notas()}")
    print(f"Estado de aprobación: {estudiante.estado_aprobacion()}")
    print("Alumno ingresado correctamente.")

def mostrar_listado_estudiantes():
    if not estudiantes:
        print("No hay Alumnos ingresados.")
        return

    print("\nListado de estudiantes:")
    for estudiante in estudiantes:
        print(f"Cédula: {estudiante.cedula}\nNombre: {estudiante.nombre}\nApellido: {estudiante.apellido}\nTotal de notas: {estudiante.calcular_total_notas()}\nEstado de aprobación: {estudiante.estado_aprobacion()}\n")

def modificar_nombre_apellido():
    cedula = input("Cédula del alumno que desea modificar: ")
    encontrado = False

    for estudiante in estudiantes:
        if estudiante.cedula == cedula:
            estudiante.nombre = input("Nuevo nombre: ")
            estudiante.apellido = input("Nuevo apellido: ")
            encontrado = True
            print("Nombre y apellido del alumno modificados correctamente.")
            break

    if not encontrado:
        print("Alumno no encontrado.")

def eliminar_estudiante():
    cedula = input("Cédula del alumno que desea eliminar: ")
    encontrado = False

    for estudiante in estudiantes:
        if estudiante.cedula == cedula:
            estudiantes.remove(estudiante)
            encontrado = True
            print("El Alumno mecionado a sido eliminado correctamente.")
            break

    if not encontrado:
        print("alumno no encontrado.")

def buscar_estudiante_por_cedula():
    cedula = input("Ingrese la cédula del alumno que desea encontrar (o presione '0' para salir de la opción): ")

    if cedula == '0':
        print("Busqueda cancelada.")
        return

    encontrado = False

    while not cedula.isdigit():
        print("Por favor, ingresa un número de cédula que sea válido.")
        cedula = input("Ingrese la cédula del alumno que desea encontrar (o presione '0' para salir de la opción): ")

        if cedula == '0':
            print("Busqueda cancelada")
            return

    for estudiante in estudiantes:
        if estudiante.cedula == cedula:
            print(f"Alumno encontrado:\nCédula: {estudiante.cedula}\nNombre: {estudiante.nombre}\nApellido: {estudiante.apellido}")
            encontrado = True
            break

    if not encontrado:
        print("Alumno no encontrado.")

def mostrar_mejor_promedio():
    if not estudiantes:
        print("No hay Alumnos ingresados.")
        return

    mejor_promedio = max(estudiantes, key=lambda estudiante: estudiante.calcular_total_notas())
    print(f"El Alumno con mejor total de notas:\nCédula: {mejor_promedio.cedula}\nNombre: {mejor_promedio.nombre}\nApellido: {mejor_promedio.apellido}\nTotal de notas: {mejor_promedio.calcular_total_notas()}\nEstado de aprobación: {mejor_promedio.estado_aprobacion()}")


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
        print("Gracias por usar mi prorgrama :3")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
