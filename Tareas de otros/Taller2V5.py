

# Clase Nodo que representa cada materia
class Nodo:
    def __init__(self, codigo, nombre, estado):
        self.datos = f"{codigo}/{nombre}/{estado}"
        self.siguiente = None

# Clase ListaEnlazada que administra los nodos
class ListaEnlazada:
    def __init__(self):
        self.cabeza = None
        self.contador = 0  # Contador de materias

    def insertar(self, codigo, nombre, estado):
        if self.contador >= 5:  # Limitar a 5 materias
            print("No se pueden agregar más materias. Límite alcanzado.")
            return
        
        nuevo_nodo = Nodo(codigo, nombre, estado)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
        self.contador += 1  # Incrementar contador

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

    def consultar(self):
        actual = self.cabeza
        if actual is None:
            print("La lista está vacía.")
        else:
            while actual:
                print(actual.datos)
                actual = actual.siguiente

def validar_codigo(codigo):
    return len(codigo) > 0  # Ajusta la validación según sea necesario

def validar_nombre(nombre):
    return len(nombre) > 0  # Nombre no puede estar vacío

def validar_estado(estado):
    return estado in ["Activa", "Inactiva"]

def menu():
    lista = ListaEnlazada()
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
            lista.consultar()
        
        elif opcion == "2":
            codigo = input("Ingrese el código de la materia: ")
            if not validar_codigo(codigo):
                print("Código no válido.")
                continue
            
            nombre = input("Ingrese el nombre de la materia: ")
            if not validar_nombre(nombre):
                print("Nombre no válido.")
                continue
            
            estado = input("Ingrese el estado de la materia (Activa/Inactiva): ")
            if not validar_estado(estado):
                print("Estado no válido. Debe ser 'Activa' o 'Inactiva'.")
                continue
            
            lista.insertar(codigo, nombre, estado)
            print("Materia insertada correctamente.")
        
        elif opcion == "3":
            codigo = input("Ingrese el código de la materia a modificar: ")
            nuevo_nombre = input("Ingrese el nuevo nombre de la materia: ")
            nuevo_estado = input("Ingrese el nuevo estado de la materia (Activa/Inactiva): ")
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


