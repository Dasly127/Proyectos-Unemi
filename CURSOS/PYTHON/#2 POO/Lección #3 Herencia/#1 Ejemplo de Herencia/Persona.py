
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)  # Se pasan los parámetros a la clase base
        self.sueldo = sueldo 

empleado1 = Empleado("Juan", 30, 5000)
print(empleado1.nombre)
print(empleado1.edad)
print(empleado1.sueldo)
