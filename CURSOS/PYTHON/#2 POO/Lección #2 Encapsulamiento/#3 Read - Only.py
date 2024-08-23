



class Persona:
    # Definimos parámetros
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre
        self.apellido = apellido
        self.edad = edad

    @property
    def nombre(self):
        print("Llamando método get")
        return self._nombre
    
'''
    @nombre.setter
    def nombre(self, nombre):
        print("llamando método set")
        self._nombre = nombre

    def mostrarDetalle(self):
        print(f"Persona: {self._nombre} {self.apellido} {self.edad}")
'''


# Para llamar el objeto 
persona1 = Persona("Juan","Perez","28")
persona1.nombre = "Juan Carlos"
print(persona1.nombre)