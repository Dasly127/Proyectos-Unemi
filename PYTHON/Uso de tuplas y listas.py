# Dada la siguiente tupla,
# crear una lista que sólo incluya los números menores a 5

# Definimos la tupla
tupla = (13, 1, 8, 3, 2, 5, 8)

# Inicializamos una lista vacía para almacenar los números menores a 5
lista = []

# Iteramos sobre cada elemento en la tupla
for elemento in tupla:
    # Verificamos si el elemento es menor que 5
    if elemento < 5:
        # Si es así, lo agregamos a la lista
        lista.append(elemento)

# Imprimimos la tupla original
print("Tupla original:", tupla)

# Imprimimos la lista con los números menores a 5

print("Lista con números menores a 5:", lista)







