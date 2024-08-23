

class Estudiante:
    def __init__(self, id, cedula, nombres, apellido, estado):
        self.id = id
        self.cedula = cedula
        self.nombres = nombres
        self.apellido = apellido
        self.estado = estado

class MatrizEstudiantes:
    def __init__(self): 
        self.estudiantes = [[None, None, None, None, None] for _ in range(5)]
        self.next_id = 1

    def agregar_estudiante(self):  
        if self.next_id > len(self.estudiantes):
            print("La matriz de estudiantes está llena.")
            return

        cedula = input("Ingrese la cédula del estudiante (10 dígitos): ")
        if len(cedula) == 10:
            nombres = input("Ingrese el nombre del estudiante: ").upper()
            apellido = input("Ingrese el apellido del estudiante: ").upper()
            estado = self.validar_estado("Ingrese el estado del estudiante (A/I): ")
            estudiante = Estudiante(self.next_id, cedula, nombres, apellido, estado)
            self.estudiantes[self.next_id - 1] = [self.next_id, cedula, nombres, apellido, estado]
            self.next_id += 1
            print("Estudiante agregado con éxito.")
        else:
            print("La cédula debe tener 10 dígitos")
            print("Inténtelo de nuevo, por favor.")

    def modificar_estudiante(self):
        if not any(self.estudiantes):
            print("No hay estudiantes registrados.")
            return

        id_modificar = self.obtener_id_estudiante()
        if 0 < id_modificar <= len(self.estudiantes) and self.estudiantes[id_modificar - 1][0] is not None:
            estudiante = self.estudiantes[id_modificar - 1]
            estudiante[2] = input("Ingrese el nuevo nombre del estudiante: ").upper()
            estudiante[3] = input("Ingrese el nuevo apellido del estudiante: ").upper()
            print("Datos modificados con éxito.")
        else:
            print(f"No se encontró un estudiante con el ID {id_modificar}")

    def cambiar_estado_estudiante(self):
        if not any(self.estudiantes):
            print("No hay estudiantes registrados.")
            return

        id_cambiar = self.obtener_id_estudiante()
        if 0 < id_cambiar <= len(self.estudiantes) and self.estudiantes[id_cambiar - 1][0] is not None:
            estudiante = self.estudiantes[id_cambiar - 1]
            estudiante[4] = "I" if estudiante[4] == "A" else "A"
            print(f"Nuevo estado del estudiante {estudiante[0]}: {estudiante[4]}")
        else:
            print(f"No se encontró un estudiante con el ID {id_cambiar}")

    def mostrar_estudiantes(self):
        if not any(self.estudiantes):
            print("No hay estudiantes registrados.")
            return

        print("\n  ID    |       Nombre        |       Apellido       |    Cédula   |  Estado")
        print("----------------------------------------------------------------------------")

        for estudiante in self.estudiantes:
            if estudiante[0] is not None:
                print(f"  {estudiante[0]:<6}| {estudiante[2]:<20}| {estudiante[3]:<20} | {estudiante[1]:^10}  |   {estudiante[4]:^7}")
    
    def validar_estado(self, mensaje):
        while True:
            estado = input(mensaje).upper()
            if estado in ["A", "I"]:
                return estado
            else:
                print("Error: El estado debe ser 'A' o 'I'")

    def obtener_id_estudiante(self):
        while True:
            id_estudiante = input("Ingrese el ID del estudiante: ")
            if id_estudiante.isdigit():
                return int(id_estudiante)
            else:
                print("Error: El ID debe ser un número entero.")

def mostrar_menu():
    print("\nMenú de opciones:")
    print("1. Agregar estudiante")
    print("2. Modificar datos de un estudiante")
    print("3. Cambiar estado de un estudiante")
    print("4. Mostrar todos los estudiantes")
    print("5. Salir")

    opcion = input("Ingrese el número de la opción que desea realizar: ")
    return opcion

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
