class Producto:
    #constructor
    def __init__(self):
        self.codigo=''
        self.nombre=''
        self.stock=0
        self.precio=0
class Inventario:
    def __init__(self):
        self.listaProductos=[]
    def crearProducto(self):
        print("*** CREAR PRODUCTO ***")
        objeto = Producto()
        objeto.codigo=input("Ingresar código: ")
        objeto.nombre=input("Ingresar nombre:")
        objeto.stock = int(input("Ingresar stock:"))
        objeto.precio = float(input("Ingresar precio:"))
        self.listaProductos.append(objeto)
        print("Registro guardado satisfactoriamente!\n")
    def consultarListadoProductos(self):
        print("*** LISTADO DE PRODUCTOS ***")
        for datos in self.listaProductos:
            print(f'Código: {datos.codigo} - Nombre: {datos.nombre} - Stock: {datos.stock} - Precio: {datos.precio}')
def menu():
    prod = Inventario()
    while True:
        print("***** MENÚ DEL INVENTARIO *****")
        print("1.- Crear Producto")
        print("2.- Consultar Listado de Productos")
        print("3.- Salir\n")
        try:
            opcion= int(input("Ingresar la opción del menú: "))
            if (opcion>0 and opcion<4):
                print("Opción válida!\n")
            else:
                print("Opción no válida!\n")
            if (opcion == 1):
                prod.crearProducto()
            elif (opcion == 2):
                prod.consultarListadoProductos()
        except:
            print("Valor ingresado no es el correcto!\n")
menu()