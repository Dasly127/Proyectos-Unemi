


# clases.py

class Estudiante:
    def __init__(self, id, cedula, nombres, apellido, estado):
        self.id = id
        self.cedula = cedula
        self.nombres = nombres
        self.apellido = apellido
        self.estado = estado

class MatrizEstudiantes:
    def __init__(self): 
        self.estudiantes = [
            [1, "0102030405", "JUAN", "PEREZ", "A"],
            [2, "0203040506", "MARIA", "LOPEZ", "A"],
            [3, "0304050607", "CARLOS", "GARCIA", "A"],
            [4, "0405060708", "ANA", "MARTINEZ", "A"],
            [5, "0506070809", "LUIS", "RODRIGUEZ", "A"]
        ]
        self.next_id = 6  # El próximo ID disponible

    def agregar_estudiante(self):  
        cedula = input("Ingrese la cédula del estudiante (10 dígitos): ")
        if len(cedula) == 10:
            nombres = input("Ingrese el nombre del estudiante: ").upper()
            apellido = input("Ingrese el apellido del estudiante: ").upper()
            estado = self.validar_estado("Ingrese el estado del estudiante (A/I): ")
            estudiante = Estudiante(self.next_id, cedula, nombres, apellido, estado)
            self.estudiantes.append([self.next_id, cedula, nombres, apellido, estado])
            self.next_id += 1
            print("Estudiante agregado con éxito.")
        else:
            print("La cédula debe tener 10 dígitos")
            print("Inténtelo de nuevo, por favor.")

    def modificar_estudiante(self):
        if not self.estudiantes:
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
        if not self.estudiantes:
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
        if not self.estudiantes:
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
