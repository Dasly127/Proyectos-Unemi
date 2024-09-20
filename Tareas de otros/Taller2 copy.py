

# Clase Materia que representa cada nodo en la lista
class Materia:
    def __init__(self, codigo, nombre, estado):
        self.codigo = codigo
        self.nombre = nombre
        self.estado = estado
        self.siguiente_materia = None

    def obtener_datos(self):
        return f"{self.codigo}/{self.nombre}/{self.estado}"

# Clase RegistroMaterias que maneja la lista de materias
class RegistroMaterias:
    def __init__(self):
        self.primera_materia = None

    # Añade una nueva materia al final de la lista
    def agregar_materia(self, codigo, nombre, estado):
        nueva_materia = Materia(codigo, nombre, estado)
        if not self.primera_materia:
            self.primera_materia = nueva_materia
        else:
            actual = self.primera_materia
            while actual.siguiente_materia:
                actual = actual.siguiente_materia
            actual.siguiente_materia = nueva_materia

    # Modifica los datos de una materia existente
    def actualizar_materia(self, codigo, nuevo_nombre, nuevo_estado):
        actual = self.primera_materia
        while actual:
            if actual.codigo == codigo:
                actual.nombre = nuevo_nombre
                actual.estado = nuevo_estado
                print(f"Materia con código {codigo} actualizada.")
                return
            actual = actual.siguiente_materia
        print(f"Materia con código {codigo} no encontrada.")

    # Consulta todas las materias almacenadas en la lista
    def mostrar_materias(self):
        if not self.primera_materia:
            print("No hay materias registradas.")
        else:
            actual = self.primera_materia
            while actual:
                print(actual.obtener_datos())
                actual = actual.siguiente_materia

# Inicialización del registro de materias
registro = RegistroMaterias()
registro.agregar_materia("MAT101", "Matemáticas", "Activa")
registro.agregar_materia("HIS102", "Historia", "Inactiva")
registro.agregar_materia("BIO103", "Biología", "Activa")
registro.agregar_materia("QUI104", "Química", "Inactiva")
registro.agregar_materia("FIS105", "Física", "Activa")

# Consultar la lista de materias
print("Lista de materias:")
registro.mostrar_materias()

# Actualizar los datos de una materia (BIO103)
registro.actualizar_materia("BIO103", "Biología Avanzada", "Inactiva")

# Consultar la lista de materias tras la actualización
print("\nLista después de la actualización:")
registro.mostrar_materias()
