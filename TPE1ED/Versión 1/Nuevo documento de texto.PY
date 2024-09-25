

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
        print(f"Proveedor: {nombre_proveedor}")
        print(f"Estado: {estado_proveedor}")
        productos_asociados = [pp for pp in prod_proveedor if pp[0] == cod_proveedor]
        for pp in productos_asociados:
            producto = next((p for p in productos if p[0] == pp[1]), None)
            if producto:
                print(f"ID: {producto[0]} PRODUCTO: {producto[1]} ESTADO: {producto[2]}")
        print(f"Total de productos: {len(productos_asociados)}")
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
            print(f"Producto modificado: {producto}")
        else:
            print("Producto no encontrado.")
    else:
        print("Proveedor no encontrado.")

# Ejemplo de uso
print("Consulta antes de la modificación:")
consultar_productos_por_proveedor("KARLA MARIDUEÑA")

# Modificar el producto
modificar_producto("KARLA MARIDUEÑA", "2", "CREMA DE LECHE", "A")

print("\nConsulta después de la modificación:")
consultar_productos_por_proveedor("KARLA MARIDUEÑA")
