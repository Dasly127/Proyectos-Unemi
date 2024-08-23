


class Persona:
    # Definimos parámetros
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    @property
    def nombre(self):
        print("Llamando método get")
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        print("Llamando método set")
        self._nombre = nombre
    
    @property
    def apellido(self):
        return self._apellido
    
    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido
    
    @property
    def edad(self):
        return self._edad
    
    @edad.setter
    def edad(self, edad):
        self._edad = edad

    def mostrarDetalle(self):
        print(f"Persona: {self._nombre} {self._apellido} {self._edad}")

# Para llamar el objeto 
persona1 = Persona("Juan", "Perez", 28)
persona1.nombre = "Juan Carlos"
print(persona1.nombre)