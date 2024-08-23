'''
Ejercicio: Convertidor de temperaturas
Realizar dos funciones para convertir de grados a celsius o fahrenheit y viceversa
'''

temperatura_C = float(input("Ingrese la temperatura en F°: "))
temperatura_F = float(input("Ingrese la temperatura en C°: "))


def fahrenheit_a_celsius(temperatura_F):
    Temperatura_C = (temperatura_F - 32) * 5/9
    return Temperatura_C

Temperatura_cel = fahrenheit_a_celsius(temperatura_F)


def celsius_a_fahrenheit(temperatura_C):
    Temperatura_F = (temperatura_C * 9/5) + 32
    return Temperatura_F

Temperatura_far = celsius_a_fahrenheit(temperatura_C)


print(f"Tu temperatura de F° A C° es: {Temperatura_cel}")
print(f"Tu temperatura de C° A F° es: {Temperatura_far}")