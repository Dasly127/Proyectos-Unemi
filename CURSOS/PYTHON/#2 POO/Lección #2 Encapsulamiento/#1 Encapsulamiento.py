'''
El encapsulamiento es un principio fundamental en la programación orientada a objetos (POO) 
que se refiere a la restricción del acceso a ciertos componentes de un objeto, lo que hace que algunos 
de sus datos y métodos solo sean accesibles dentro de la clase en la que fueron definidos. 
Este concepto ayuda a proteger los datos y a asegurar que el objeto se use de la manera prevista.
'''

class Persona:
    # Definimos parámetros
    def __init__(self, nombre, apellido, edad):
        self.__nombre = nombre
        self.apellido = apellido
        self.edad = edad


    def mostrarDetalle(self):
        print(f"Persona: {self.__nombre} {self.apellido} {self.edad}")

# Para llamar el objeto 
persona1 = Persona("Juan","Perez","28")

#A esto se le conoce como atributo encapsulado 
persona1.__nombre = "Juan Carlos"

persona1.mostrarDetalle()