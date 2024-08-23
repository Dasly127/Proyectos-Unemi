
#Función para llamar un diccionario

def ListarTerminos(**terminos):
    for llave, valor in terminos.items():
        print(f"{llave}: {valor}")

ListarTerminos(IDE = "INTEGRATED DEVELOPER ENVIROMENT", PK = "Peka" )
