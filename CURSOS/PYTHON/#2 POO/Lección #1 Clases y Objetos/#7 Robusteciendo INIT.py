'''
Para Agregar una tupla y diccionario a una clase
'''

class Persona:
    # Definimos parámetros
    def __init__(self, nombre, apellido, edad, *valores, **terminos):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.valores = valores 
        self.terminos = terminos 

    def mostrarDetalle(self):
        print(f"Persona: {self.nombre} {self.apellido} {self.edad} {self.valores} {self.terminos}")

# Para llamar el objeto 
persona1 = Persona("Juan", "Perez", 28, 12343242, 2, 5, m= "manzana", p = "pera")
persona1.mostrarDetalle()

# Este intento de acceder a persona1.telefono causará un error porque no existe el atributo telefono
# print(persona1.telefono)

persona2 = Persona("Karla", "Gomez", 30)
persona2.mostrarDetalle()
