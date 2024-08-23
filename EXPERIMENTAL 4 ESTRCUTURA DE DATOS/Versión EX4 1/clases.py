


class Estudiante:
    def __init__(self, id, cedula, nombres, apellido, estado):
        self.id = id
        self.cedula = cedula
        self.nombres = nombres
        self.apellido = apellido
        self.estado = estado

class PilaEstudiantes:
    def __init__(self): 
        self.id_pila = [1, 2, 3, 4, 5]
        self.cedula_pila = ["1725442493", "1104395767", "0501975957", "0931481741", "0503236408"]
        self.nombres_pila = ["LALO", "MARLY", "FÉLIX", "LISSETE", "LUIS"]
        self.apellidos_pila = ["SALAZAR", "ASTUDILLO", "COQUE", "MITE", "PERALTA"]
        self.estado_pila = ["A", "A", "A", "A", "A"]
        self.next_id = 6  # ID inicial para nuevos estudiantes

    def agregar_estudiante(self):  
        cedula = input("Ingrese la cédula del estudiante (10 dígitos): ")
        if len(cedula) == 10 and cedula.isdigit():
            nombres = input("Ingrese el nombre del estudiante: ").upper()
            apellido = input("Ingrese el apellido del estudiante: ").upper()
            estado = self.validar_estado("Ingrese el estado del estudiante (A/I): ")

            self.id_pila.append(self.next_id)
            self.cedula_pila.append(cedula)
            self.nombres_pila.append(nombres)
            self.apellidos_pila.append(apellido)
            self.estado_pila.append(estado)

            self.next_id += 1
            print("Estudiante agregado con éxito.")
        else:
            print("La cédula debe tener 10 dígitos y contener solo números.")
            print("Inténtelo de nuevo, por favor.")

    def modificar_estudiante(self):
        if not self.id_pila:
            print("No hay estudiantes registrados.")
            return

        id_modificar = self.obtener_id_estudiante()
        if id_modificar in self.id_pila:
            index = self.id_pila.index(id_modificar)
            self.nombres_pila[index] = input("Ingrese el nuevo nombre del estudiante: ").upper()
            self.apellidos_pila[index] = input("Ingrese el nuevo apellido del estudiante: ").upper()
            print("Datos modificados con éxito.")
        else:
            print(f"No se encontró un estudiante con el ID {id_modificar}")

    def cambiar_estado_estudiante(self):
        if not self.id_pila:
            print("No hay estudiantes registrados.")
            return

        id_cambiar = self.obtener_id_estudiante()
        if id_cambiar in self.id_pila:
            index = self.id_pila.index(id_cambiar)
            self.estado_pila[index] = "I" if self.estado_pila[index] == "A" else "A"
            print(f"Nuevo estado del estudiante {id_cambiar}: {self.estado_pila[index]}")
        else:
            print(f"No se encontró un estudiante con el ID {id_cambiar}")

    def mostrar_estudiantes(self):
        if not self.id_pila:
            print("No hay estudiantes registrados.")
            return

        print("\n  ID    |       Nombre        |       Apellido       |    Cédula   |  Estado")
        print("----------------------------------------------------------------------------")
        
        for i in range(len(self.id_pila)-1, -1, -1):  # Mostrar en orden LIFO
            print(f"  {self.id_pila[i]:<6}| {self.nombres_pila[i]:<20}| {self.apellidos_pila[i]:<20} | {self.cedula_pila[i]:^10}  |   {self.estado_pila[i]:^7}")

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
