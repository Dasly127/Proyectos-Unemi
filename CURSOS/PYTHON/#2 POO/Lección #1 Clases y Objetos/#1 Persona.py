
#Clase creada
class Persona:
	#Para crear un método usamos __init__
	def __init__(self):
		self.nombre = "Juan"
		self.apellido = "Pérez"
		self.edad = 29

#Para llamar el objeto 
persona1 = Persona()
print(persona1.nombre) #Para llamar atributos de una clase
print(persona1.apellido)
print(persona1.edad)

