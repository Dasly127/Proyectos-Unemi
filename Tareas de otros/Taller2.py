

# Clase Nodo que representa cada materia
class Nodo:
    def __init__(self, codigo, nombre, estado):
        self.datos = f"{codigo}/{nombre}/{estado}"
        self.siguiente = None

# Clase ListaEnlazada que administra los nodos
class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    # Método para insertar un nuevo nodo (materia) al final de la lista
    def insertar(self, codigo, nombre, estado):
        nuevo_nodo = Nodo(codigo, nombre, estado)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    # Método para modificar los datos de una materia
    def modificar(self, codigo, nuevo_nombre, nuevo_estado):
        actual = self.cabeza
        while actual:
            codigo_actual, _, _ = actual.datos.split('/')
            if codigo_actual == codigo:
                actual.datos = f"{codigo}/{nuevo_nombre}/{nuevo_estado}"
                print(f"Materia con código {codigo} modificada.")
                return
            actual = actual.siguiente
        print(f"Materia con código {codigo} no encontrada.")

    # Método para consultar la información almacenada en la lista enlazada
    def consultar(self):
        actual = self.cabeza
        if actual is None:
            print("La lista está vacía.")
        else:
            while actual:
                print(actual.datos)
                actual = actual.siguiente

# Inicialización de la lista con 5 materias
lista = ListaEnlazada()
lista.insertar("MAT101", "Matemáticas", "Activa")
lista.insertar("HIS102", "Historia", "Inactiva")
lista.insertar("BIO103", "Biología", "Activa")
lista.insertar("QUI104", "Química", "Inactiva")
lista.insertar("FIS105", "Física", "Activa")

# Consultar la lista inicializada
print("Lista de materias:")
lista.consultar()

# Modificar una materia (ejemplo: cambiar el nombre y estado de 'BIO103')
lista.modificar("BIO103", "Biología Avanzada", "Inactiva")

# Consultar la lista después de la modificación
print("\nLista después de la modificación:")
lista.consultar()
