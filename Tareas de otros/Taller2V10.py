#Clase inicial
class Nodo:
    def __init__(self, codigo, nombre, estado):
        # Inicializa un nodo con el código, nombre y estado de la materia
        self._datos = f"{codigo}/{nombre}/{estado}"
        self._siguiente = None  # Inicializa el siguiente nodo como None


    # Encapsulamiento
    @property
    def datos(self):
        # Propiedad para obtener los datos del nodo
        return self._datos

    @property
    def siguiente(self):
        # Propiedad para obtener el siguiente nodo
        return self._siguiente

    @siguiente.setter
    def siguiente(self, nodo):
        # Setter para establecer el siguiente nodo
        self._siguiente = nodo

class ListaEnlazada:
    def __init__(self):
        # Inicializa la lista enlazada con la cabeza como None
        self._cabeza = None

    def validar_estado(self, estado):
        # Valida el estado de la materia y lo normaliza
        estado_normalizado = estado.strip().lower()
        if estado_normalizado == "activa":
            return "ACTIVA"
        elif estado_normalizado == "inactiva":
            return "INACTIVA"
        else:
            print("Estado no válido. Debe ser 'Activa' o 'Inactiva'.")
            return None

    def codigo_existente(self, codigo):
        # Verifica si el código de la materia ya existe en la lista
        actual = self._cabeza
        while actual:
            codigo_actual, _, _ = actual.datos.split('/')
            if codigo_actual == codigo:
                return True
            actual = actual.siguiente
        return False

    def insertar(self, codigo, nombre, estado, mostrar_mensaje=True):
        # Inserta una nueva materia en la lista enlazada
        if self.codigo_existente(codigo):
            print(f"El código {codigo} ya está registrado.")
            return

        estado_validado = self.validar_estado(estado)
        if not estado_validado:
            return

        nuevo_nodo = Nodo(codigo, nombre.upper(), estado_validado)  # Crea un nuevo nodo
        if self._cabeza is None:
            self._cabeza = nuevo_nodo  # Si la lista está vacía, establece la cabeza
        else:
            actual = self._cabeza
            while actual.siguiente:  # Busca el último nodo
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo  # Enlaza el nuevo nodo al final de la lista
        if mostrar_mensaje:
            print("Materia insertada correctamente.")

    def modificar(self, codigo, nuevo_nombre, nuevo_estado):
        # Método que modifica los datos de una materia existente
        actual = self._cabeza
        while actual:
            codigo_actual, _, _ = actual.datos.split('/')
            if codigo_actual == codigo:
                estado_validado = self.validar_estado(nuevo_estado)
                if not estado_validado:
                    return

                actual._datos = f"{codigo}/{nuevo_nombre.upper()}/{estado_validado}"
                print(f"Materia con código {codigo} modificada.")
                return
            actual = actual.siguiente
        print(f"Materia con código {codigo} no encontrada.")

    def consultar(self):
        # Consulta y muestra todas las materias en la lista
        actual = self._cabeza
        if actual is None:
            print("La lista está vacía.")
        else:
            while actual:
                print(actual.datos)  # Imprime los datos de cada nodo
                actual = actual.siguiente

def menu():
    # Función para manejar el menú de opciones del sistema
    lista = ListaEnlazada()

    # Inicializa las 5 materias sin mostrar un mensaje adicional
    lista.insertar("ECO127", "ECONOMÍA", "Activa", mostrar_mensaje=False)
    lista.insertar("ALG214", "ALGEBRA", "Inactiva", mostrar_mensaje=False)
    lista.insertar("EST235", "ESTRUCTURAS", "Activa", mostrar_mensaje=False)
    lista.insertar("CAL201", "CALCULO", "Inactiva", mostrar_mensaje=False)
    lista.insertar("LEN134", "LENGUAJE", "Activa", mostrar_mensaje=False)

    while True:
        # Bucle que muestra el menú y gestiona las opciones
        print("\nSistema de Materias Unemi:")
        print("Elija una de las opciones proporcionadas")
        print("1. Insertar materia")
        print("2. Modificar materia")
        print("3. Consultar materias")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            # Opción para insertar una nueva materia
            codigo = input("Ingrese el código de la materia: ")
            nombre = input("Ingrese el nombre de la materia: ")
            estado = input("Ingrese el estado de la materia (Activa/Inactiva): ")
            lista.insertar(codigo, nombre, estado)
        
        elif opcion == "2":
            # Opción para modificar una materia existente
            codigo = input("Ingrese el código de la materia a modificar: ")
            nuevo_nombre = input("Ingrese el nuevo nombre de la materia: ")
            nuevo_estado = input("Ingrese el nuevo estado de la materia: ")
            lista.modificar(codigo, nuevo_nombre, nuevo_estado)
        
        elif opcion == "3":
            # Opción para consultar todas las materias
            print("Lista de materias:")
            lista.consultar()
        
        elif opcion == "4":
            # Opción para salir del programa
            print("Saliendo del programa.")
            break
        
        else:
            # Manejamos la opción no válida
            print("Opción no válida. Intente nuevamente.")

# Ejecución del menú
menu()






