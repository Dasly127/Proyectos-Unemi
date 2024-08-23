class Producto:
    """
    Clase que representa un producto con atributos como código, nombre, stock y precio.
    """
    def __init__(self):
        """
        Constructor de la clase Producto.
        Inicializa los atributos con valores predeterminados.
        """
        self.codigo = ''
        self.nombre = ''
        self.stock = 0
        self.precio = 0


class Inventario:
    """
    Clase que gestiona un inventario de productos.
    """
    def __init__(self):
        """
        Constructor de la clase Inventario.
        Inicializa un atributo listaProductos como una lista vacía.
        """
        self.listaProductos = []

    def crearProducto(self):
        """
        Método para crear un nuevo producto y agregarlo al inventario.
        El usuario ingresa información como código, nombre, stock y precio.
        """
        print("*** CREAR PRODUCTO ***")
        objeto = Producto()
        objeto.codigo = input("Ingresar código: ")
        objeto.nombre = input("Ingresar nombre: ")
        objeto.stock = int(input("Ingresar stock: "))
        objeto.precio = float(input("Ingresar precio: "))
        self.listaProductos.append(objeto)
        print("Registro guardado satisfactoriamente!\n")

    def consultarListadoProductos(self):
        """
        Método para imprimir en consola el listado de productos en el inventario.
        Muestra información como código, nombre, stock y precio de cada producto.
        """
        print("*** LISTADO DE PRODUCTOS ***")
        for datos in self.listaProductos:
            print(f'Código: {datos.codigo} - Nombre: {datos.nombre} - Stock: {datos.stock} - Precio: {datos.precio}')


def menu():
    """
    Función que implementa un menú interactivo para gestionar el inventario de productos.
    Permite al usuario realizar acciones como crear productos, consultar listado de productos y salir.
    """
    prod = Inventario()
    while True:
        print("***** MENÚ DEL INVENTARIO *****")
        print("1.- Crear Producto")
        print("2.- Consultar Listado de Productos")
        print("3.- Salir\n")
        try:
            opcion = int(input("Ingresar la opción del menú: "))
            if 1 <= opcion <= 3:
                print("Opción válida!\n")
            else:
                print("Opción no válida!\n")
            
            if opcion == 1:
                prod.crearProducto()
            elif opcion == 2:
                prod.consultarListadoProductos()
            elif opcion == 3:
                break  # Salir del bucle si la opción es 3

        except ValueError:
            print("Valor ingresado no es el correcto!\n")


# Llamada a la función menu para iniciar la aplicación
menu()
