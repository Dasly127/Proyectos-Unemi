


##Prototipo de la clase 
"""
class AreaRectangulo:

    def __init__(self, Base, Altura):
        self.base = 
        self.altura = Altura
    def CalcularArea(self):
        return self.base * self.altura

AreaRectangulo = AreaRectangulo(Base, Altura)

print(input("Ingrese la altura del rectangulo: "))
print(input("Ingrese la base del rectangulo: "))
"""


'''
VERSIÓN CORREGIDA
'''
class AreaRectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

altura1 = float(input("Ingrese la altura del rectángulo: "))
base1 = float(input("Ingrese la base del rectángulo: "))

altura2 = float(input("Ingrese la altura del rectángulo: "))
base2 = float(input("Ingrese la base del rectángulo: "))

rectangulo1 = AreaRectangulo(base1, altura1)

print("El área del rectángulo es:", rectangulo1.calcular_area())


rectangulo2 = AreaRectangulo(base2, altura2)

print("El área del rectángulo es:", rectangulo2.calcular_area())