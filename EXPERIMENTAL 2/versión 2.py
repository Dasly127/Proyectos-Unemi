"""
UƟlizando POO cree una clase llamada ventas en donde se deberá almacenar los montos
de ventas por cada vendedor. Inicialice el archivo Ɵpo texto con al menos 5 registros. El
programa principal que invoca a la clase presentará un menú para el ingreso del vendedor y su
monto de venta, modificar sus datos, eliminarlo o para mostrar quienes cumplieron con la meta
de ventas establecida, la última opción del menú es salir.
Si deseo mostrar quienes cumplieron las ventas debo ingresar el monto mínimo de cumplimiento
para que con ese criterio se filtren los datos del archivo y se presenten en pantalla

-. Si el programa no funciona, se cae o presenta un error la nota es de CERO
-. Copia o similitud de código, la nota es de CERO para todos los involucrados.
-. Si el programa corre y funciona, se revisa:
   --Cada opción del CRUD que funcione y haga lo solicitado equivale a 3 puntos 
-. Usa las funciones para implementar el programa 3 puntos
-. Si por alguna razón, al revisar por ejemplo el 2do requerimiento el programa se cae, el
equipo recibe la nota que hasta ese momento obtuvo, y finaliza la revisión.

"""


class Vendedor:
    #Atributos clase Vendedor
    id_vendedor = 0

    def __init__(self, nombre, monto_venta):
        self.id = Vendedor.id_vendedor
        Vendedor.id_vendedor += 1
        self.nombre = nombre
        self.monto_venta = monto_venta
        self.cumplimiento = self.validar_cumplimiento(monto_venta)

    def validar_cumplimiento(self, monto_venta):
        #Compara y valida la venta segun el valor minimo ingresado
        return "C" if monto_venta >= matriz_vendedores.valor_venta_minimo else "N"

class MatrizVendedores:
    #Atributos clase Matriz que gestiona los vendedores
    def __init__(self):
        # Designa espacio para los matrices de gestion
        self.vendedores = {}
        self.valor_venta_minimo = 0

    def leer_vendedores(self):
        #Lectrua de datos desde el TXT
        try:
            with open("Ventas.txt", "r") as archivo:
                for linea in archivo:
                    datos = linea.strip().split(",")
                    if len(datos) == 4:
                        id_vendedor, nombre, monto_venta, _ = datos
                        self.vendedores[int(id_vendedor)] = Vendedor(nombre, float(monto_venta))
        except FileNotFoundError:
            print("No se encontro el archivo Ventas.txt")
        except ValueError:
            print("Formato de datos incorrecto en el archivo")

    def agregar_vendedor(self):
        #Metodo que agrega vendedor y su venta
        nombre = input("Ingrese el nombre : ")
        monto_venta = float(input("Ingrese el monto de venta : "))
        vendedor = Vendedor(nombre, monto_venta)
        self.vendedores[vendedor.id] = vendedor

        with open("Ventas.txt", "a") as archivo:
            archivo.write(f"{vendedor.id},{vendedor.nombre},{vendedor.monto_venta},{vendedor.cumplimiento}\n")
        print("Vendedor agregado con exito")

    def modificar_vendedor(self):
        #Modifica  datos del vendedor tanto Nombre como la Venta
        self.mostrar_vendedores()
        id_modificar = int(input("Ingrese el ID del vendedor que quiere modificar: "))
        if id_modificar in self.vendedores:
            vendedor = self.vendedores[id_modificar]
            vendedor.nombre = input("Ingrese el nuevo nombre: ")
            vendedor.monto_venta = float(input("Ingrese el nuevo monto de venta : "))
            vendedor.cumplimiento = vendedor.validar_cumplimiento(vendedor.monto_venta)

            # Actualizar el archivo de texto
            self.actualizar_archivo_vendedores()
            print("Datos modificdos con exito")
        else:
            print(f"No se encontro un vendedor con el ID {id_modificar}")

    def eliminar_vendedor(self):
        #Elimina el vendedor
        self.mostrar_vendedores()
        id_eliminar = int(input("Ingrese el ID del vendedor a eliminar: "))
        if id_eliminar in self.vendedores:
            del self.vendedores[id_eliminar]
            self.actualizar_archivo_vendedores()
            print(f"Vendedor con ID {id_eliminar} eliminado exitosamente.")
        else:
            print(f"No se encontro un vendedor con el ID {id_eliminar}")

    def mostrar_vendedores(self):
        #Muestra los vendores ingresados en el TXT y en el diccionario vendedores
        print(f"\nValor de venta minimo: {self.valor_venta_minimo}")
        print("\n{0:^10}|{1:^20}|{2:^20}|{3:^20}".format("ID", "Nombre", "Monto de venta", "Cumplimiento C/N"))
        print("-" * 70)
        for id_vendedor, vendedor in self.vendedores.items():
            print("{0:^10}|{1:^20}|{2:^20}|{3:^20}".format(id_vendedor, vendedor.nombre, vendedor.monto_venta, vendedor.cumplimiento))

    def establecer_valor_venta_minimo(self):
     while True:
        try:
            self.valor_venta_minimo = float(input("Ingrese el valor de venta mínimo: "))
            print(f"Valor de venta mínimo establecido en: {self.valor_venta_minimo}")
            self.actualizar_cumplimiento_vendedores()
            break
        except ValueError:
            print("Por favor, ingrese un valor numérico para el valor de venta mínimo.")


    def actualizar_cumplimiento_vendedores(self):
        #luego de ingresar un valor de venta minimo se actualiza el Cumplimiento o No Cumplimiento
        for vendedor in self.vendedores.values():
            vendedor.cumplimiento = "C" if vendedor.monto_venta >= self.valor_venta_minimo else "N"

        # Actualizar el archivo de texto
        self.actualizar_archivo_vendedores()

    def actualizar_archivo_vendedores(self):
        #Actualiza el Archivo TXT
        with open("Ventas.txt", "w") as archivo:
            for vendedor in self.vendedores.values():
                archivo.write(f"{vendedor.id},{vendedor.nombre},{vendedor.monto_venta},{vendedor.cumplimiento}\n")

def mostrar_menu():
    print("\nMenú de opciones:")
    print("1. Establecer valor de venta minimo")
    print("2. Agregar vendedor")
    print("3. Modificar datos de un vendedor")
    print("4. Eliminar vendedor")
    print("5. Mostrar todos los vendedores")
    print("6. Salir")

    opcion = input("Ingrese una opcion: ")
    return opcion

# Programa principal
matriz_vendedores = MatrizVendedores()
matriz_vendedores.leer_vendedores()

while True:
    opcion = mostrar_menu()

    if opcion == "1":
        matriz_vendedores.establecer_valor_venta_minimo()
    elif opcion == "2":
        matriz_vendedores.agregar_vendedor()
    elif opcion == "3":
        matriz_vendedores.modificar_vendedor()
    elif opcion == "4":
        matriz_vendedores.eliminar_vendedor()
    elif opcion == "5":
        matriz_vendedores.mostrar_vendedores()
    elif opcion == "6":
        print("¡Finalizando Programa!")
        break
    else:
        print("Ingrese una opcion [1-6]")