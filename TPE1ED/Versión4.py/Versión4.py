

import os

# Función para escribir en un archivo si no existe previamente
def escribir_si_no_existe(nombre_archivo, contenido):
    if not os.path.isfile(nombre_archivo):
        with open(nombre_archivo, 'w') as archivo:
            archivo.write(contenido)

# Definición de contenido de archivos
contenido_proveedor = "COD|NOMBRE|ESTADO\n1|MARCELO JARRÍN|A\n2|KARLA MARIDUEÑA|I\n3|PATRICIO CASTRO|A\n"
contenido_productos = "ID|PRODUCTO|ESTADO\n1|AZÚCAR|A\n2|CREMA LECHE|I\n3|CAFÉ EN GRANO LOJA|A\n4|ACEITE DE COCO|A\n"
contenido_asociacion = "PRV_COD|PRO_COD|ESTADO\n1|3|A\n1|2|A\n3|1|A\n2|2|I\n2|4|A\n"

# Crear los archivos necesarios si no existen
escribir_si_no_existe('Proveedores.txt', contenido_proveedor)
escribir_si_no_existe('Productos.txt', contenido_productos)
escribir_si_no_existe('Asociacion.txt', contenido_asociacion)

# Función para leer el contenido de un archivo y devolver una lista de listas
def leer_datos(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        return [linea.strip().split('|') for linea in archivo.readlines()[1:]]

# Cargar datos de los archivos
datos_proveedores = leer_datos('Proveedores.txt')
datos_productos = leer_datos('Productos.txt')
datos_asociacion = leer_datos('Asociacion.txt')

# Función para mostrar los productos de un proveedor específico
def listar_productos_por_proveedor(nombre):
    nombre = nombre.upper()  # Convertir a mayúsculas
    proveedor = next((prov for prov in datos_proveedores if prov[1] == nombre), None)
    
    if proveedor:
        cod_proveedor, estado_proveedor = proveedor[0], proveedor[2]
        print(f"Proveedor: {nombre} (Estado: {estado_proveedor})")
        productos_relacionados = [rel for rel in datos_asociacion if rel[0] == cod_proveedor]
        
        for relacion in productos_relacionados:
            producto = next((prod for prod in datos_productos if prod[0] == relacion[1]), None)
            if producto:
                print(f"ID: {producto[0]} | Producto: {producto[1]} | Estado: {producto[2]}")
        print(f"Total de productos: {len(productos_relacionados)}")
    else:
        print("Proveedor no encontrado.")

# Función para modificar los datos de un producto
def actualizar_producto(nombre_proveedor, id_producto, nuevo_nombre, nuevo_estado):
    nombre_proveedor = nombre_proveedor.upper()  # Convertir a mayúsculas
    nuevo_nombre = nuevo_nombre.upper()  # Convertir a mayúsculas
    nuevo_estado = nuevo_estado.upper()  # Convertir a mayúsculas

    proveedor = next((prov for prov in datos_proveedores if prov[1] == nombre_proveedor), None)
    
    if proveedor:
        producto = next((prod for prod in datos_productos if prod[0] == id_producto), None)
        if producto:
            producto[1], producto[2] = nuevo_nombre, nuevo_estado
            guardar_cambios('Productos.txt', datos_productos)
            print(f"Producto actualizado: {producto}")
        else:
            print("Producto no encontrado.")
    else:
        print("Proveedor no encontrado.")

# Función para escribir los cambios en un archivo
def guardar_cambios(nombre_archivo, lista_datos):
    with open(nombre_archivo, 'w') as archivo:
        encabezado = "ID|PRODUCTO|ESTADO\n" if 'Productos' in nombre_archivo else "COD|NOMBRE|ESTADO\n"
        archivo.write(encabezado)
        for linea in lista_datos:
            archivo.write('|'.join(linea) + '\n')

# Función para mostrar toda la información
def mostrar_todo():
    print("\n--- PROVEEDORES ---")
    for proveedor in datos_proveedores:
        print(f"COD: {proveedor[0]} | NOMBRE: {proveedor[1]} | ESTADO: {proveedor[2]}")
    
    print("\n--- PRODUCTOS ---")
    for producto in datos_productos:
        print(f"ID: {producto[0]} | PRODUCTO: {producto[1]} | ESTADO: {producto[2]}")
    print()

# Función para mostrar el menú principal
def menu_principal():
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Consultar productos por proveedor")
    print("2. Modificar un producto")
    print("3. Ver todos los proveedores y productos")
    print("4. Salir")
    return input("Seleccione una opción: ")

# Función principal que ejecuta el programa
def iniciar_programa():
    while True:
        opcion = menu_principal()
        if opcion == '1':
            nombre_proveedor = input("Ingrese el nombre del proveedor: ").upper()  # Convertir a mayúsculas
            listar_productos_por_proveedor(nombre_proveedor)
        elif opcion == '2':
            nombre_proveedor = input("Ingrese el nombre del proveedor: ").upper()  # Convertir a mayúsculas
            id_producto = input("ID del producto a modificar: ").upper()  # Convertir a mayúsculas
            nuevo_nombre = input("Nuevo nombre del producto: ").upper()  # Convertir a mayúsculas
            nuevo_estado = input("Nuevo estado (A/I): ").upper()  # Convertir a mayúsculas
            actualizar_producto(nombre_proveedor, id_producto, nuevo_nombre, nuevo_estado)
        elif opcion == '3':
            mostrar_todo()
        elif opcion == '4':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

# Ejecutar el programa si es el archivo principal
if __name__ == "__main__":
    iniciar_programa()

