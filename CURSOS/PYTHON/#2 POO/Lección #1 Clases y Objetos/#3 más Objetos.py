

#Clase creada
class Persona:
	#Definimos parámetros
	def __init__(self, nombre, apellido, edad):
		self.nombre = "Juan"
		self.apellido = "Pérez"
		self.edad = 29

#Para llamar el objeto 
persona1 = Persona("Juan", "Perez", "28")

print(f"objeto persona2: {persona1.nombre} {persona1.apellido} {persona1.edad}")


persona2 = Persona("Karla", "Gomez", "30")

print(f"objeto persona2: {persona2.nombre} {persona2.apellido} {persona2.edad}")