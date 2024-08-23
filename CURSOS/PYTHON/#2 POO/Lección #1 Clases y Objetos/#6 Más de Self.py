

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
persona1.telefono = 0998204107
print(persona1.telefono)

persona2 = Persona("Karla", "Gomez", 30)
persona2.mostrarDetalle()
print(persona2.telefono)