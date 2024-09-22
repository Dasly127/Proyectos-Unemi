

# Clase Nodo que representa cada materia
class Nodo:
    def __init__(self, codigo, nombre, estado):
        self.datos = f"{codigo}/{nombre}/{estado}"
        self.siguiente = None  # Apuntador al siguiente nodo

# Clase ListaEnlazada que administra los nodos
class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    # Método para validar el estado (acepta en cualquier formato, pero almacena en mayúsculas)
    def validar_estado(self, estado):
        estado_normalizado = estado.strip().lower()  # Normaliza el estado eliminando espacios y convirtiendo a minúsculas
        if estado_normalizado == "activa":
            return "ACTIVA"
        elif estado_normalizado == "inactiva":
            return "INACTIVA"
        else:
            print("Estado no válido. Debe ser 'Activa' o 'Inactiva'.")
            return None

    # Método para insertar una nueva materia con opción para suprimir el mensaje de inserción
    def insertar(self, codigo, nombre, estado, mostrar_mensaje=True):
        estado_validado = self.validar_estado(estado)  # Validar el estado
        if not estado_validado:
            return  # Si el estado no es válido, no continuar

        nuevo_nodo = Nodo(codigo, nombre.upper(), estado_validado)  # Almacena el nombre en mayúsculas y el estado validado
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
                
                actual.datos = f"{codigo}/{nuevo_nombre.upper()}/{estado_validado}"  # Modifica y almacena el nombre en mayúsculas y estado validado
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
    lista.insertar("ECO127", "ECONOMÍA", "Activa", mostrar_mensaje=False)
    lista.insertar("ALG214", "ALGEBRA", "Inactiva", mostrar_mensaje=False)
    lista.insertar("EST235", "ESTRUCTURAS", "Activa", mostrar_mensaje=False)
    lista.insertar("CAL201", "CALCULO", "Inactiva", mostrar_mensaje=False)
    lista.insertar("LEN134", "LENGUAJE", "Activa", mostrar_mensaje=False)

    while True:
        print("\nSistema de Materias Unemi:")
        print("Elija una de las opciones proporcionadas")
        print("1. Insertar materia")
        print("2. Modificar materia")
        print("3. Consultar materias")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            codigo = input("Ingrese el código de la materia: ")
            nombre = input("Ingrese el nombre de la materia: ")
            estado = input("Ingrese el estado de la materia (Activa/Inactiva): ")
            lista.insertar(codigo, nombre, estado)
        
        elif opcion == "2":
            codigo = input("Ingrese el código de la materia a modificar: ")
            nuevo_nombre = input("Ingrese el nuevo nombre de la materia: ")
            nuevo_estado = input("Ingrese el nuevo estado de la materia: ")
            lista.modificar(codigo, nuevo_nombre, nuevo_estado)
        
        elif opcion == "3":
            print("Lista de materias:")
            lista.consultar()
        
        elif opcion == "4":
            print("Saliendo del programa.")
            break
        
        else:
            print("Opción no válida. Intente nuevamente.")

# Ejecución del menú
menu()




