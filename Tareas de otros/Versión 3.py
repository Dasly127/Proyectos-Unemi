

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

# Ejemplo de uso
lista = ListaEnlazada()

# Insertar materias en la lista
lista.insertar("MAT101", "Matemáticas", "Activa")
lista.insertar("HIS102", "Historia", "Inactiva")
lista.insertar("BIO103", "Biología", "Activa")
lista.insertar("QUI104", "Química", "Inactiva")
lista.insertar("FIS105", "Física", "Activa")

# Consultar la lista inicial
print("Lista de materias:")
lista.consultar()

# Modificar una materia (cambiar nombre y estado de 'BIO103')
lista.modificar("BIO103", "Biología Avanzada", "Inactiva")

# Consultar la lista después de la modificación
print("\nLista después de la modificación:")
lista.consultar()
