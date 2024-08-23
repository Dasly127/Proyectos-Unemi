'''
Crear una función para sumar los valores recibidos de tipo numérico,
utilizando argumentos variables *args como parámetro de la función
y regresar como resultado la suma de todos los valores pasados como argumentos.
'''

def sumar_valores(*args):
    resultado = 0

    for valor in args:
        resultado += valor
    
    return resultado

print(sumar_valores(3, 5, 9))
    