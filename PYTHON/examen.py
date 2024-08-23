class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre 
        self.edad = edad

    def es_mayor_de_edad(self):
        if self.edad >= 18:
            return True
        else:
            return False