

archivo = open('prueba.txt', 'r', encoding='utf-8')


#iterar el archivo
#for linea in archivo:
#    print(linea)

#print(archivo.readline())


archivo2 = open('copia.txt', 'a', encoding='utf-8')
archivo2.write(archivo.read())

archivo.close()
archivo2.close()

print('Archivo cerrado')
