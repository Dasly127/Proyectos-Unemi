"""
Un "set" en Python es una colección desordenada y mutable de elementos únicos. En otras palabras, un set es una estructura de datos que no permite elementos duplicados y no mantiene un orden específico de los elementos.

Puedes crear un set en Python utilizando llaves {} o la función set(). Por ejemplo:


# Crear un set usando llaves
mi_set = {1, 2, 3, 4, 5}

# Crear un set usando la función set()
mi_otro_set = set([1, 2, 3, 4, 5])
"""

# set
planetas = {'Marte', 'Júpiter', 'Venus'}
print(planetas)
#largo
print(len(planetas))
# revisar si un elemento está presente
print('Marte' in planetas)
# agregar un elemento
planetas.add('Tierra')
print( planetas)
#no se pueden duplicar elementos
planetas.add('Tierra')
print(planetas)
# eliminar elemento posiblemente arrojando un error
planetas.remove('Tierra')
print(planetas)
# eliminar elemento sin arrojar error
planetas.discard('Júpiters')
print(planetas)
# limpiar set
planetas.clear()
print(planetas)
# eliminar el set
del planetas
print(planetas)