"""
Aplicando POO crear una matriz que permita:
-.Crear la clase estudiante, es decir:1
- Ingresar los datos de los estudiantes (id, nombres, apellido, estado).
- El ID es un dato secuencial numérico, que solo idenƟfica a un estudiante,
por lo tanto, no puede repetirse.

-.Nombre y apellido, cada uno es una cadena Ɵpo texto y finalmente el
estado solo almacena una letra A para AcƟvo o I para InacƟvo.

-.Su matriz debe tener al menos 5 registros.
o Modificar los datos del estudiante: es decir corregir algún detalle solo de su
nombre o apellido.

-.Activar o Eliminar un estudiante específico: enƟéndase que sería una
eliminación lógica que consiste en solo cambiar la letra que se almacena como
su estado, si Ɵene estado I lo cambio por A, y viceversa.

-.Cree su programa principal y desde allí invoque a su clase estudiante.

-.Herramienta de desarrollo es Python, usted puede elegir el IDE de trabajo de su
preferencia.
"""

class Estudiante:
    """
    Clase para representar a un estudiante.
    """
    def __init__(self, id, cedula, nombres, apellido, estado):
        """
        Inicializa un objeto Estudiante con los atributos dados.
        """
        self.id = id
        self.cedula = cedula
        self.nombres = nombres
        self.apellido = apellido
        self.estado = estado

class MatrizEstudiantes:
    """
    Clase para gestionar una lista de estudiantes.
    """
    def __init__(self):
        """
        Inicializa una matriz de estudiantes vacía.
        """
        self.estudiantes = {}
        self.next_id = 1


    def agregar_estudiante(self):  
        """
        Agrega un nuevo estudiante a la lista.
        """
        cedula = input("Ingrese la cédula del estudiante (10 dígitos): ")
        if len(cedula) == 10:

# Utilizamos la función upper() para convertir texto de minúsculas a mayúsculas
           nombres = input("Ingrese el nombre del estudiante: ").upper()
           apellido = input("Ingrese el apellido del estudiante: ").upper()
           estado = self.validar_estado("Ingrese el estado del estudiante (A/I): ")
           estudiante = Estudiante(self.next_id, cedula, nombres, apellido, estado)
           self.estudiantes[self.next_id] = estudiante
           self.next_id += 1
           print("Estudiante agregado con éxito.")

        else:

           print("La cedula debe tener 10 digitos")
           print("Intentelo de nuevo porfavor.")

    def modificar_estudiante(self):
        """
        Modifica los datos de un estudiante existente.
        """
        if not self.estudiantes:
            print("No hay estudiantes registrados.")
            return

        id_modificar = self.obtener_id_estudiante()
        if id_modificar in self.estudiantes:
            estudiante = self.estudiantes[id_modificar]
            estudiante.nombres = input("Ingrese el nuevo nombre del estudiante: ").upper()
            estudiante.apellido = input("Ingrese el nuevo apellido del estudiante: ").upper()
            print("Datos modificados con éxito.")
        else:
            print(f"No se encontró un estudiante con el ID {id_modificar}")

    def cambiar_estado_estudiante(self):
        """
        Cambia el estado de un estudiante de activo a inactivo o viceversa.
        """
        if not self.estudiantes:
            print("No hay estudiantes registrados.")
            return

        id_cambiar = self.obtener_id_estudiante()
        if id_cambiar in self.estudiantes:
            estudiante = self.estudiantes[id_cambiar]
            estudiante.estado = "I" if estudiante.estado == "A" else "A"
            print(f"Nuevo estado del estudiante {estudiante.id}: {estudiante.estado}")
        else:
            print(f"No se encontró un estudiante con el ID {id_cambiar}")

    def mostrar_estudiantes(self):
        """
        Muestra los datos de todos los estudiantes en la lista.
        """
        if not self.estudiantes:
            print("No hay estudiantes registrados.")
            return

        print("\nDatos de todos los estudiantes:")
        for id_estudiante, estudiante in self.estudiantes.items():
            print(f"ID: {id_estudiante}, Cédula: {estudiante.cedula}, Nombre: {estudiante.nombres}, Apellido: {estudiante.apellido}, Estado: {estudiante.estado}")

    def validar_estado(self, mensaje):
        """
        Valida el estado ingresado por el usuario (A/I).
        """
        while True:
            estado = input(mensaje).upper()
            if estado in ["A", "I"]:
                return estado
            else:
                print("Error: El estado debe ser 'A' o 'I'")

    def obtener_id_estudiante(self):
        """
        Obtiene el ID del estudiante ingresado por el usuario.
        """
        while True:
            id_estudiante = input("Ingrese el ID del estudiante: ")
            if id_estudiante.isdigit():
                return int(id_estudiante)
            else:
                print("Error: El ID debe ser un número entero.")

# Función para mostrar el menú y manejar las opciones impreso por pantalla
def mostrar_menu():
    print("\nMenú de opciones:")
    print("1. Agregar estudiante")
    print("2. Modificar datos de un estudiante")
    print("3. Cambiar estado de un estudiante")
    print("4. Mostrar todos los estudiantes")
    print("5. Salir")

    opcion = input("Ingrese el número de la opción que desea realizar: ")
    return opcion

# Ejecución del menú 
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
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor, ingrese un número del 1 al 10")
