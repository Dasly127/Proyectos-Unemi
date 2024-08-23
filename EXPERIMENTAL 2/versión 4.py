class Vendedor:
    # Atributos clase Vendedor
    id_vendedor = 0

    def __init__(self, nombre, monto_venta):
        self.id = Vendedor.id_vendedor
        Vendedor.id_vendedor += 1
        self.nombre = nombre.upper()  # Convertir nombre a mayúsculas
        self.monto_venta = monto_venta
        self.cumplimiento = self.validar_cumplimiento(monto_venta)

    def validar_cumplimiento(self, monto_venta):
        # Compara y valida la venta según el valor mínimo ingresado
        return "C" if monto_venta >= matriz_vendedores.valor_venta_minimo else "N"


class MatrizVendedores:
    # Atributos clase Matriz que gestiona los vendedores
    def __init__(self):
        # Designa espacio para los matrices de gestión
        self.vendedores = {}
        self.valor_venta_minimo = 0

    def leer_vendedores(self):
        # Lectura de datos desde el TXT
        try:
            with open("Ventas.txt", "r") as archivo:
                for linea in archivo:
                    datos = linea.strip().split(",")
                    if len(datos) == 4:
                        id_vendedor, nombre, monto_venta, _ = datos
                        self.vendedores[int(id_vendedor)] = Vendedor(nombre, float(monto_venta))
        except FileNotFoundError:
            print("No se encontró el archivo Ventas.txt")
        except ValueError:
            print("Formato de datos incorrecto en el archivo")

    def agregar_vendedor(self):
        # Método que agrega vendedor y su venta
        while True:
            nombre = input("Ingrese el nombre: ").upper()  # Convertir nombre a mayúsculas
            if nombre.replace(" ", "").isalpha():  # Verifica si el nombre contiene solo letras
                break
            else:
                print("El nombre no puede contener números ni caracteres especiales.")

        while True:
            try:
                monto_venta = float(input("Ingrese el monto de venta: "))
                break
            except ValueError:
                print("Por favor, ingrese un valor numérico para el monto de venta.")

        vendedor = Vendedor(nombre, monto_venta)
        self.vendedores[vendedor.id] = vendedor

        with open("Ventas.txt", "a") as archivo:
            archivo.write(f"{vendedor.id},{vendedor.nombre},{vendedor.monto_venta},{vendedor.cumplimiento}\n")
        print("Vendedor agregado con éxito")

    def modificar_vendedor(self):
        # Modifica datos del vendedor tanto Nombre como la Venta
        self.mostrar_vendedores()
        while True:
            try:
                id_modificar = int(input("Ingrese el ID del vendedor que quiere modificar: "))
                if id_modificar in self.vendedores:
                    break
                else:
                    print(f"No se encontró un vendedor con el ID {id_modificar}")
            except ValueError:
                print("Por favor, ingrese un valor numérico para el ID del vendedor.")

        vendedor = self.vendedores[id_modificar]
        vendedor.nombre = input("Ingrese el nuevo nombre: ").upper()  # Convertir nombre a mayúsculas
        while True:
            try:
                vendedor.monto_venta = float(input("Ingrese el nuevo monto de venta : "))
                break
            except ValueError:
                print("Por favor, ingrese un valor numérico para el monto de venta.")

        vendedor.cumplimiento = vendedor.validar_cumplimiento(vendedor.monto_venta)

        # Actualizar el archivo de texto
        self.actualizar_archivo_vendedores()
        print("Datos modificados con éxito")

    def eliminar_vendedor(self):
        # Elimina el vendedor
        self.mostrar_vendedores()
        while True:
            try:
                id_eliminar = int(input("Ingrese el ID del vendedor a eliminar: "))
                if id_eliminar in self.vendedores:
                    break
                else:
                    print(f"No se encontró un vendedor con el ID {id_eliminar}")
            except ValueError:
                print("Por favor, ingrese un valor numérico para el ID del vendedor.")

        del self.vendedores[id_eliminar]
        self.actualizar_archivo_vendedores()
        print(f"Vendedor con ID {id_eliminar} eliminado exitosamente.")

    def mostrar_vendedores(self):
        # Muestra los vendores ingresados en el TXT y en el diccionario vendedores
        print(f"\nValor de venta mínimo: {self.valor_venta_minimo}")
        print("\n{0:^10}|{1:^20}|{2:^20}|{3:^20}".format("ID", "Nombre", "Monto de venta", "Cumplimiento C/N"))
        print("-" * 70)
        for id_vendedor, vendedor in self.vendedores.items():
            print("{0:^10}|{1:^20}|{2:^20}|{3:^20}".format(id_vendedor, vendedor.nombre, vendedor.monto_venta,
                                                             vendedor.cumplimiento))

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
        # Luego de ingresar un valor de venta mínimo se actualiza el Cumplimiento o No Cumplimiento
        for vendedor in self.vendedores.values():
            vendedor.cumplimiento = "C" if vendedor.monto_venta >= self.valor_venta_minimo else "N"

        # Actualizar el archivo de texto
        self.actualizar_archivo_vendedores()

    def actualizar_archivo_vendedores(self):
        # Actualiza el Archivo TXT
        with open("Ventas.txt", "w") as archivo:
            for vendedor in self.vendedores.values():
                archivo.write(
                    f"{vendedor.id},{vendedor.nombre},{vendedor.monto_venta},{vendedor.cumplimiento}\n")


def mostrar_menu():
    print("\nMenú de opciones:")
    print("1. Establecer valor de venta mínimo")
    print("2. Agregar vendedor")
    print("3. Modificar datos de un vendedor")
    print("4. Eliminar vendedor")
    print("5. Mostrar todos los vendedores")
    print("6. Salir")

    opcion = input("Ingrese una opción: ")
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
        print("Ingrese una opción [1-6]")

#Fin del programa 