
#Clase creada
class Persona:
	#Definimos parámetros
	def __init__(self, nombre, apellido, edad):
		self.nombre = "Juan"
		self.apellido = "Pérez"
		self.edad = 29

#Para llamar el objeto 
persona1 = Persona("Juan", "Perez", "28")
print(persona1.nombre) #Para llamar atributos de una clase
print(persona1.apellido)
print(persona1.edad)
