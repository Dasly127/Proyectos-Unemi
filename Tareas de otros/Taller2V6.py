

# Clase Nodo que representa cada materia
class Nodo:
    def __init__(self, codigo, nombre, estado):
        self.datos = f"{codigo}/{nombre}/{estado}"
        self.siguiente = None  # Apuntador al siguiente nodo

# Clase ListaEnlazada que administra los nodos
class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    # Método para validar el estado
    def validar_estado(self, estado):
        estado_normalizado = estado.capitalize()  # Normaliza el estado (Primera letra mayúscula)
        if estado_normalizado not in ["Activa", "Inactiva"]:
            print("Estado no válido. Debe ser 'Activa' o 'Inactiva'.")
            return None
        return estado_normalizado

    # Método para insertar una nueva materia con opción para suprimir el mensaje de inserción
    def insertar(self, codigo, nombre, estado, mostrar_mensaje=True):
        estado_validado = self.validar_estado(estado)  # Validar el estado
        if not estado_validado:
            return  # Si el estado no es válido, no continuar

        nuevo_nodo = Nodo(codigo, nombre, estado_validado)  # Almacena el estado validado
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
        if mostrar_mensaje:
            print("Materia insertada correctamente.")  # Mostrar mensaje solo si mostrar_mensaje=True

    # Método para modificar los datos de una materia
    def modificar(self, codigo, nuevo_nombre, nuevo_estado):
        actual = self.cabeza
        while actual:
            codigo_actual, _, _ = actual.datos.split('/')
            if codigo_actual == codigo:
                estado_validado = self.validar_estado(nuevo_estado)  # Validar el estado
                if not estado_validado:
                    return  # Si el estado no es válido, no continuar
                
                actual.datos = f"{codigo}/{nuevo_nombre}/{estado_validado}"  # Modifica los datos
                print(f"Materia con código {codigo} modificada.")
                return
            actual = actual.siguiente
        print(f"Materia con código {codigo} no encontrada.")

    # Método para consultar toda la información almacenada en la lista
    def consultar(self):
        actual = self.cabeza
        if actual is None:
            print("La lista está vacía.")
        else:
            while actual:
                print(actual.datos)
                actual = actual.siguiente

# Función principal para manejar el menú
def menu():
    lista = ListaEnlazada()

    # Inicializar las 5 materias sin mostrar el mensaje de inserción
    lista.insertar("MAT101", "Matemáticas", "Activa", mostrar_mensaje=False)
    lista.insertar("HIS102", "Historia", "Inactiva", mostrar_mensaje=False)
    lista.insertar("BIO103", "Biología", "Activa", mostrar_mensaje=False)
    lista.insertar("QUI104", "Química", "Inactiva", mostrar_mensaje=False)
    lista.insertar("FIS105", "Física", "Activa", mostrar_mensaje=False)

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
            nombre = input("Ingrese el nombre de la materia: ")
            estado = input("Ingrese el estado de la materia (Activa/Inactiva): ")
            lista.insertar(codigo, nombre, estado)
        
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




