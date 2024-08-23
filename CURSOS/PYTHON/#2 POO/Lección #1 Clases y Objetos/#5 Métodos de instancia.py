'''
Este código define una clase Persona que permite crear objetos que representan a personas 
con un nombre, apellido y edad. Además, proporciona un método para mostrar los detalles de cada persona. 
Es una estructura básica en programación orientada a objetos (POO) 
que ilustra cómo encapsular datos y comportamientos relacionados en una sola entidad (clase), facilitando 
la creación y gestión de múltiples objetos similares.
'''

class Persona:
    # Definimos parámetros
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def mostrarDetalle(self):
        print(f"Persona: {self.nombre} {self.apellido} {self.edad}")

# Para llamar el objeto 
persona1 = Persona("Juan", "Perez", 28)
persona1.mostrarDetalle()

persona2 = Persona("Karla", "Gomez", 30)
persona2.mostrarDetalle()
