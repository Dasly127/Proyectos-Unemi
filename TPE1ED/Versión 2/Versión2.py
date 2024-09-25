


import os

# Función para crear un archivo si no existe
def crear_archivo(archivo, contenido):
    if not os.path.exists(archivo):
        with open(archivo, 'w') as f:
            f.write(contenido)

# Crear archivos .txt si no existen
contenido_proveedor = """COD|NOMBRE|ESTADO
1|MARCELO JARRÍN|A
2|KARLA MARIDUEÑA|I
3|PATRICIO CASTRO|A
"""
contenido_productos = """ID|PRODUCTO|ESTADO
1|AZÚCAR|A
2|CREMA LECHE|I
3|CAFÉ EN GRANO LOJA|A
4|ACEITE DE COCO|A
"""
contenido_prod_proveedor = """PRV_COD|PRO_COD|ESTADO
1|3|A
1|2|A
3|1|A
2|2|I
2|4|A
"""

# Crear los archivos si no existen
crear_archivo('Proveedor.txt', contenido_proveedor)
crear_archivo('Productos.txt', contenido_productos)
crear_archivo('Prod_Proveedor.txt', contenido_prod_proveedor)

# Función para cargar archivos de texto
def cargar_datos(archivo):
    datos = []
    with open(archivo, 'r') as f:
        for linea in f.readlines()[1:]:  # Saltar el encabezado
            datos.append(linea.strip().split('|'))
    return datos

# Cargar archivos de texto
proveedores = cargar_datos('Proveedor.txt')
productos = cargar_datos('Productos.txt')
prod_proveedor = cargar_datos('Prod_Proveedor.txt')

# Función para consultar productos por proveedor
def consultar_productos_por_proveedor(nombre_proveedor):
    proveedor = [p for p in proveedores if p[1] == nombre_proveedor]
    if proveedor:
        cod_proveedor = proveedor[0][0]
        estado_proveedor = proveedor[0][2]
        print(f"\nProveedor: {nombre_proveedor}")
        print(f"Estado: {estado_proveedor}")
        productos_asociados = [pp for pp in prod_proveedor if pp[0] == cod_proveedor]
        for pp in productos_asociados:
            producto = next((p for p in productos if p[0] == pp[1]), None)
            if producto:
                print(f"ID: {producto[0]} PRODUCTO: {producto[1]} ESTADO: {producto[2]}")
        print(f"Total de productos: {len(productos_asociados)}\n")
    else:
        print("Proveedor no encontrado.")

# Función para modificar producto por proveedor
def modificar_producto(nombre_proveedor, id_producto, nuevo_nombre, nuevo_estado):
    # Buscar proveedor
    proveedor = next((p for p in proveedores if p[1] == nombre_proveedor), None)
    if proveedor:
        # Buscar producto
        producto = next((p for p in productos if p[0] == id_producto), None)
        if producto:
            # Modificar nombre y estado
            producto[1] = nuevo_nombre
            producto[2] = nuevo_estado
            print(f"\nProducto modificado: {producto}")
            # Actualizar archivo de productos
            actualizar_archivo('Productos.txt', productos)
        else:
            print("Producto no encontrado.")
    else:
        print("Proveedor no encontrado.")

# Función para actualizar el archivo de productos
def actualizar_archivo(archivo, datos):
    with open(archivo, 'w') as f:
        f.write('ID|PRODUCTO|ESTADO\n')  # Encabezado
        for d in datos:
            f.write('|'.join(d) + '\n')

# Función para mostrar el menú
def mostrar_menu():
    print("\n--- MENÚ ---")
    print("1. Consultar productos por proveedor")
    print("2. Modificar producto")
    print("3. Salir")
    opcion = input("Seleccione una opción (1-3): ")
    return opcion

# Función principal del programa con menú interactivo
def main():
    while True:
        opcion = mostrar_menu()
        if opcion == '1':
            nombre_proveedor = input("Ingrese el nombre del proveedor: ")
            consultar_productos_por_proveedor(nombre_proveedor)
        elif opcion == '2':
            nombre_proveedor = input("Ingrese el nombre del proveedor: ")
            id_producto = input("Ingrese el ID del producto a modificar: ")
            nuevo_nombre = input("Ingrese el nuevo nombre del producto: ")
            nuevo_estado = input("Ingrese el nuevo estado (A/I): ")
            modificar_producto(nombre_proveedor, id_producto, nuevo_nombre, nuevo_estado)
        elif opcion == '3':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

# Ejecución del programa
if __name__ == "__main__":
    main()
