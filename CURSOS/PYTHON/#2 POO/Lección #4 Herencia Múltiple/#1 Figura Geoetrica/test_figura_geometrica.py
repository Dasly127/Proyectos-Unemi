
from Rectangulo import Rectangulo
from Cuadrado import Cuadrado

print("Creación Objeto Cuadrado".center(50,"-"))
cuadrado1 = Cuadrado(5, "rojo")
print(f"Cálculo del área cuadrado: {cuadrado1.calcular_area()}")
print(cuadrado1)

print("Creación Objeto Recatngulo".center(50,"-"))
rectangulo1 = Rectangulo(3, 8, "Verde")
print(f"Cálculo del área del rectángulo: {rectangulo1.calcular_area()}")
print(rectangulo1)
