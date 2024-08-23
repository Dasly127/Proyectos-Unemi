'''
Crear un programa con POO que permita calcular el volumen de un cubo:

- El cubo tiene 3m de ancho
- de profundo tiene 5m
- de alto tiene 6m
- 2x5x6 = 90m cúbicos

Esos deben ser 3 atributos de la clase 

La clase se va llamar Cubo
'''


class Cubo:
    def __init__(self, anchura, profundidad, altura) -> None:
        self.anchura = anchura
        self.profundidad = profundidad
        self.altura = altura
    
    def CalcularVolumen(self):
        return self.anchura * self.profundidad * self.altura

#Pedimos datos al Usuario
anchura = float(input("Ingrese la aanchura del cubo: "))
profundidad = float(input("Ingrese la profundidad del cubo: "))
altura = float(input("Ingrese la altura del cubo: "))

#Creamos la variable cubo con las instancias proporcionadas
cubo = Cubo(anchura, profundidad, altura)   

#Calculamos el Volumen
volumen = cubo.CalcularVolumen()

#Mostramos el resultado
print("El volumen del cubo es:", volumen)





