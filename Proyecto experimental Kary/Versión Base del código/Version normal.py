



# Definición de la clase Estudiante con sus atributos solicitados en la tarea
class Estudiante:
    def __init__(self, id, nombres, apellido, estado):
        self.id = id
        self.nombres = nombres
        self.apellido = apellido
        self.estado = estado

    def __str__(self):
        return f"ID: {self.id}, Nombres: {self.nombres}, Apellido: {self.apellido}, Estado: {self.estado}"


# Definición de la clase MatrizEstudiantes solicitado
class MatrizEstudiantes:
    def __init__(self):
        # Inicialización de la matriz con los integrantes del grupo
        self.estudiantes = [
            Estudiante(1, "JOHNNY JAVIER", "SANTOS CEDENO", "A"),
            Estudiante(2, "MARIA ELIZABETH", "CARRERA CUENCA", "A"),
            Estudiante(3, "LISSETH DE LOURDES", "JIMENEZ CONTRERAS", "I"),
            Estudiante(4, "MARIA CAROLINA", "ROMAN ROSARIO", "A"),
            Estudiante(5, "KATHERINE PAOLA", "YUGCHA FARINANGO", "I")
        ]

    # agregar un estudiante a la MatrizEstudiantes
    def agregar_estudiante(self, estudiante):
        if self.validar_id(estudiante.id):
            self.estudiantes.append(estudiante)
        else:
            print(f"El ID {estudiante.id} ya existe.")

    # modificar nombres y apellidos de un estudiante
    def modificar_nombre_apellido(self, id, nombres=None, apellido=None):
        estudiante = self.buscar_estudiante(id)
        if estudiante:
            if nombres.isalpha() and apellido.isalpha():
                estudiante.nombres = nombres
                estudiante.apellido = apellido
                print(f"Datos modificados correctamente para el ID {id}.")
            else:
                print("Los nombres y apellidos deben contener solo letras.")
        else:
            print(f"No se encontró el estudiante con ID {id}.")

    # cambiar el estado de un estudiante
    def cambiar_estado(self, id):
        estudiante = self.buscar_estudiante(id)
        if estudiante:
            if estudiante.estado.upper() in ['A', 'I']:
                if estudiante.estado == 'A':
                    estudiante.estado = 'I'
                else:
                    estudiante.estado = 'A'
                print(f"Estado cambiado correctamente para el ID {id}.")
            else:
                print("Ingreso incorrecto para el estado.")
        else:
            #mensaje de error
            print(f"No se encontró el estudiante con ID {id}.")

    # buscar un estudiante por su ID mediante la funcion for vista en clase
    def buscar_estudiante(self, id):
        for estudiante in self.estudiantes:
            if estudiante.id == id:
                return estudiante
        return None

    #  validar si un ID ya existe en la matriz
    def validar_id(self, id):
        return not any(estudiante.id == id for estudiante in self.estudiantes)


# Programa principal
if __name__ == "__main__":
    matriz_estudiantes = MatrizEstudiantes()
# Imprime el menú principal con las opciones
    while True:
        print("\n--- Menú Sistema de Ingreso de Estudiantes ---")
        print("1. Ingresar Estudiante Nuevo.")
        print("2. Modificar Datos de Estudiante.")
        print("3. Activar o eliminar Estudiante.")
        print("4. Mostrar Lista de Estudiantes.")
        print("5. Salir.")

        opcion = input("Seleccione una opción: ")

        # Opción para ingresar un nuevo estudiante
        if opcion == "1":
            while True:
                print("\n--- Ingresar Estudiante Nuevo ---")
                nombres = input("Ingrese nombres del estudiante (o 'z' para volver al menú principal): ")

                # Opción para volver al menú principal
                if nombres.lower() == 'z':
                    break

                apellido = input("Ingrese apellidos del estudiante: ")
                estado = input("Ingrese estado (A para Activo, I para Inactivo): ")

                # Validación de datos ingresados
                if nombres.isalpha() and apellido.isalpha() and estado.upper() in ['A', 'I']:
                    nuevo_estudiante = Estudiante(6, nombres, apellido, estado.upper())
                    matriz_estudiantes.agregar_estudiante(nuevo_estudiante)
                    break
                else:
                    print("Ingreso incorrecto. Por favor, intente nuevamente.")

        # Opción para modificar datos de un estudiante
        elif opcion == "2":
            while True:
                print("\n--- Modificar Datos de Estudiante ---")
                id_estudiante = input(
                    "Ingrese el ID del estudiante a modificar (o 'z' para volver al menú principal): ")

                # Opción para volver al menú principal
                if id_estudiante.lower() == 'z':
                    break

                try:
                    id_estudiante = int(id_estudiante)
                    if id_estudiante > 0:
                        break
                    else:
                        print("El ID debe ser un número positivo.")
                except ValueError:
                    print("Por favor, ingrese un ID válido (solo números enteros).")

            if str(id_estudiante).isdigit():
                nombres = input("Ingrese nuevos nombres del estudiante: ")
                apellido = input("Ingrese nuevos apellidos del estudiante: ")

                # Validación de datos ingresados
                if nombres.isalpha() and apellido.isalpha():
                    matriz_estudiantes.modificar_nombre_apellido(id_estudiante, nombres, apellido)
                else:
                    print("Los nombres y apellidos deben contener solo letras.")
            else:
                print("Ingreso incorrecto. Por favor, ingrese un ID válido.")

        # Opción para activar o eliminar un estudiante
        elif opcion == "3":
            while True:
                print("\n--- Activar o Eliminar Estudiante ---")
                id_estudiante = input(
                    "Ingrese el ID del estudiante a activar o eliminar (o 'z' para volver al menú principal): ")

                # Opción para volver al menú principal
                if id_estudiante.lower() == 'z':
                    break

                try:
                    id_estudiante = int(id_estudiante)
                    if id_estudiante > 0:
                        break
                    else:
                        print("El ID debe ser un número positivo.")
                except ValueError:
                    print("Por favor, ingrese un ID válido (solo números enteros).")

            if str(id_estudiante).isdigit():
                matriz_estudiantes.cambiar_estado(id_estudiante)
            else:
                print("Ingreso incorrecto. Por favor, ingrese un ID válido.")

        # Opción para mostrar la lista de estudiantes
        elif opcion == "4":
            print("\nLista de Estudiantes:")
            for estudiante in matriz_estudiantes.estudiantes:
                print(estudiante)

        # Opción para salir del programa
        elif opcion == "5":
            print("Saliendo del programa...Muchas gracias")
            break

        # Opción para manejar ingresos incorrectos
        else:
            print("Opción no válida. Por favor, ingrese una opción correcta.")
