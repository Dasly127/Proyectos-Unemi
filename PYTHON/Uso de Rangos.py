# Ejercicio 1. Iterar un rango de 0 a 10 e imprimir números divisibles entre 3

for numero in range(11):  # Rango de 0 a 10 (inclusivo)
    if numero % 3 == 0:
        print(numero)



# Ejercicio 2. Crear un rango de numeros de 2 a 6, e imprimelos

numeros = range(2, 7)  # Rango de 2 a 6 (exclusivo)

for numero in numeros:
    print(numero)


# Ejercicio 3. Crear un rango de 3 a 10, pero con incremento de 2 en 2, en lugar de 1 en 1


for numero in range(3, 11, 2):  # Rango de 3 a 10 con incremento de 2
    print(numero)
