#Definir una tupla
frutas = ('Naranja', 'Plátano', 'Guayaba')
print(frutas)
#saber el largo
print(len(frutas))
#acceder a un elemento
print(frutas[0])
# navegación inversa
print(frutas[-1])
# acceder a un rango
print(frutas[0:1])# sin incluir el último índice
#recorrer elementos

#Para imprimir elementos de forma Horizontal
for fruta in frutas:
    print(fruta, end=' ')
#cambiar valor tupla
# frutas[0] = 'Pera'


#Para convertir una tupla a Lista
frutasLista = list(frutas)
frutasLista[0] = 'Pera'

#Para regresar una lista a tupla
frutas = tuple(frutasLista)
print('\n',frutas) #Para imprimir elementos de forma Horizontal
#eliminar la tupla
del frutas
print(frutas)