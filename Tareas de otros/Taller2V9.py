class Nodo:
    def __init__(self, codigo, nombre, estado):
        self._datos = f"{codigo}/{nombre}/{estado}"
        self._siguiente = None

    @property
    def datos(self):
        return self._datos

    @property
    def siguiente(self):
        return self._siguiente

    @siguiente.setter
    def siguiente(self, nodo):
        self._siguiente = nodo

class ListaEnlazada:
    def __init__(self):
        self._cabeza = None

    def validar_estado(self, estado):
        estado_normalizado = estado.strip().lower()
        if estado_normalizado == "activa":
            return "ACTIVA"
        elif estado_normalizado == "inactiva":
            return "INACTIVA"
        else:
            print("Estado no válido. Debe ser 'Activa' o 'Inactiva'.")
            return None

    def codigo_existente(self, codigo):
        actual = self._cabeza
        while actual:
            codigo_actual, _, _ = actual.datos.split('/')
            if codigo_actual == codigo:
                return True
            actual = actual.siguiente
        return False

    def insertar(self, codigo, nombre, estado, mostrar_mensaje=True):
        if self.codigo_existente(codigo):
            print(f"El código {codigo} ya está registrado.")
            return

        estado_validado = self.validar_estado(estado)
        if not estado_validado:
            return

        nuevo_nodo = Nodo(codigo, nombre.upper(), estado_validado)
        if self._cabeza is None:
            self._cabeza = nuevo_nodo
        else:
            actual = self._cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
        if mostrar_mensaje:
            print("Materia insertada correctamente.")

    def modificar(self, codigo, nuevo_nombre, nuevo_estado):
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
        actual = self._cabeza
        if actual is None:
            print("La lista está vacía.")
        else:
            while actual:
                print(actual.datos)
                actual = actual.siguiente

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





