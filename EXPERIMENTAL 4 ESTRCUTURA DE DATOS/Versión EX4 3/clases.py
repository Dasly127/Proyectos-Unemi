

class PilaEstudiantes:
    def __init__(self): 
        self.id_pila = [1, 2, 3, 4, 5]
        self.cedula_pila = ["1725442493", "1104395767", "0501975957", "0931481741", "0503236408"]
        self.nombres_pila = ["LALO", "MARLY", "FÉLIX", "LISSETE", "LUIS"]
        self.apellidos_pila = ["SALAZAR", "ASTUDILLO", "COQUE", "MITE", "PERALTA"]
        self.estado_pila = ["A", "A", "A", "A", "A"]
        self.next_id = 6  # ID inicial para nuevos estudiantes

    def agregar_estudiante(self):  
        while True:
            cedula = input("Ingrese la cédula del estudiante (10 dígitos): ")
            if len(cedula) == 10 and cedula.isdigit():
                break
            else:
                print("La cédula debe tener 10 dígitos y contener solo números.")
                print("Inténtelo de nuevo, por favor.")
        
        while True:
            nombres = input("Ingrese el nombre del estudiante: ").upper()
            if nombres.strip() and nombres.replace(" ", "").isalpha():
                break
            else:
                print("El nombre debe contener solo letras y no puede estar en blanco. Inténtelo de nuevo.")
        
        while True:
            apellido = input("Ingrese el apellido del estudiante: ").upper()
            if apellido.strip() and apellido.replace(" ", "").isalpha():
                break
            else:
                print("El apellido debe contener solo letras y no puede estar en blanco. Inténtelo de nuevo.")

        estado = self.validar_estado("Ingrese el estado del estudiante (A/I): ")

        self.id_pila.append(self.next_id)
        self.cedula_pila.append(cedula)
        self.nombres_pila.append(nombres)
        self.apellidos_pila.append(apellido)
        self.estado_pila.append(estado)

        self.next_id += 1
        print("Estudiante agregado con éxito.")

    def modificar_estudiante(self):
        if not self.id_pila:
            print("No hay estudiantes registrados.")
            return

        id_modificar = self.obtener_id_estudiante()
        if id_modificar in self.id_pila:
            index = self.id_pila.index(id_modificar)
            while True:
                nombre = input("Ingrese el nuevo nombre del estudiante: ").upper()
                if nombre.strip() and nombre.replace(" ", "").isalpha():
                    self.nombres_pila[index] = nombre
                    break
                else:
                    print("El nombre debe contener solo letras y no puede estar en blanco. Inténtelo de nuevo.")

            while True:
                apellido = input("Ingrese el nuevo apellido del estudiante: ").upper()
                if apellido.strip() and apellido.replace(" ", "").isalpha():
                    self.apellidos_pila[index] = apellido
                    break
                else:
                    print("El apellido debe contener solo letras y no puede estar en blanco. Inténtelo de nuevo.")
                    
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
        
        for i in range(len(self.id_pila)):  # Mostrar en orden FIFO
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
