
try: 
    archivo = open('prueba.txt', 'w', encoding='utf-8')
    archivo.write('Agregamos información al archivo')
except Exception as e:
    print(e)
finally:
    archivo.close()
    print('Archivo cerrado')
    
