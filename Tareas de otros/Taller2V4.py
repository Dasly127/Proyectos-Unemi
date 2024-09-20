

# Clase Nodo que representa cada materia
class Nodo:
    def __init__(self, codigo, nombre, estado):
        # Almacenar los datos de la materia en una sola cadena utilizando el separador "/"
        self.datos = f"{codigo}/{nombre}/{estado}"
        self.siguiente = None  # Apuntador al siguiente nodo

# Clase ListaEnlazada que administra los nodos
class ListaEnlazada:
    def __init__(self):
        self.cabeza = None  # Inicializa la lista vacía

    # Método para insertar un nuevo nodo al final de la lista
    def insertar(self, codigo, nombre, estado):
        nuevo_nodo = Nodo(codigo, nombre, estado)  # Crear nuevo nodo con los datos
        if self.cabeza is None:  # Si la lista está vacía
            self.cabeza = nuevo_nodo  # El nuevo nodo será la cabeza
        else:
            actual = self.cabeza
            while actual.siguiente:  # Recorre hasta el último nodo
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo  # Inserta el nuevo nodo al final

    # Método para modificar los datos de una materia (nombre y estado) en un nodo específico
    def modificar(self, codigo, nuevo_nombre, nuevo_estado):
        actual = self.cabeza
        while actual:  # Recorre la lista
            # Descompone los datos almacenados para acceder al código de la materia
            codigo_actual, _, _ = actual.datos.split('/')
            if codigo_actual == codigo:  # Si el código coincide con el solicitado
                actual.datos = f"{codigo}/{nuevo_nombre}/{nuevo_estado}"  # Modifica el nombre y el estado
                print(f"Materia con código {codigo} modificada.")
                return
            actual = actual.siguiente  # Avanza al siguiente nodo
        print(f"Materia con código {codigo} no encontrada.")  # Si no se encuentra el código

    # Método para consultar toda la información almacenada en la lista enlazada
    def consultar(self):
        actual = self.cabeza
        if actual is None:  # Si la lista está vacía
            print("La lista está vacía.")
        else:
            while actual:  # Recorre la lista
                print(actual.datos)  # Imprime los datos del nodo actual
                actual = actual.siguiente  # Avanza al siguiente nodo

# Función principal para manejar el menú
def menu():
    lista = ListaEnlazada()

    # Inicializar las 5 materias
    lista.insertar("MAT101", "Matemáticas", "Activa")
    lista.insertar("HIS102", "Historia", "Inactiva")
    lista.insertar("BIO103", "Biología", "Activa")
    lista.insertar("QUI104", "Química", "Inactiva")
    lista.insertar("FIS105", "Física", "Activa")

    while True:
        print("\nMenú de opciones:")
        print("1. Mostrar materias")
        print("2. Insertar materia")
        print("3. Modificar materia")
        print("4. Consultar materias")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("Materias inicializadas:")
            lista.consultar()  # Muestra las materias inicializadas
        
        elif opcion == "2":
            codigo = input("Ingrese el código de la materia: ")
            nombre = input("Ingrese el nombre de la materia: ")
            estado = input("Ingrese el estado de la materia: ")
            lista.insertar(codigo, nombre, estado)
            print("Materia insertada correctamente.")
        
        elif opcion == "3":
            codigo = input("Ingrese el código de la materia a modificar: ")
            nuevo_nombre = input("Ingrese el nuevo nombre de la materia: ")
            nuevo_estado = input("Ingrese el nuevo estado de la materia: ")
            lista.modificar(codigo, nuevo_nombre, nuevo_estado)
        
        elif opcion == "4":
            print("Lista de materias:")
            lista.consultar()
        
        elif opcion == "5":
            print("Saliendo del programa.")
            break
        
        else:
            print("Opción no válida. Intente nuevamente.")

# Ejecución del menú
menu()


