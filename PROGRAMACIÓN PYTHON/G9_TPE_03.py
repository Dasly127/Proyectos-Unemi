

class PILASNUM:

    '''
    Clase que representa dos pilas de números y permite realizar operaciones de llenado, intercalado y suma.
    '''
   
    def __init__(self):
        '''
        Inicializa las pilas y el resultado como listas vacías.
        '''
        self.pila_a = []
        self.pila_b = []
        self.resultado = []

    def llenar_pilas(self):
        '''
        Método para llenar las pilas con número ingresados por el usuario
        '''
        self.pila_a = self.obtener_numeros(5, "Pila A")
        self.pila_b = self.obtener_numeros(7, "Pila B")

    def obtener_numeros(self, cantidad, nombre_pila):
        '''
         Método que solicita al usuario una cantidad específica de números para llenar una pila.
        '''
        numeros = []
        for i in range(cantidad):
            while True:
                try:
                    num = int(input(f"Ingrese el número {i + 1} para {nombre_pila}: "))
                    numeros.append(num)
                    break
                except ValueError:
                    print("Por favor, ingrese un número válido.")
        return numeros #Lista de números ingresados por el usuario.

    def intercalar_pilas(self):
        """
        Intercala los elementos de las dos pilas y guarda el resultado en la pila de resultado.
        Muestra las pilas originales y el resultado.
        """
        self.resultado = []
        len_a = len(self.pila_a)
        len_b = len(self.pila_b)
        i, j = 0, 0

        while i < len_a and j < len_b:
            '''
            Este bucle se encarga de intercalar los elementos de pila_a y pila_b 
            mientras ambos índices i y j sean menores que las longitudes respectivas de las pilas.
            Este bucle garantiza que los elementos se intercalen uno a uno desde ambas pilas hasta 
            que una de ellas se quede sin elementos.
            '''
            self.resultado.append(self.pila_b[j])
            self.resultado.append(self.pila_a[i])
            i += 1
            j += 1

        while i < len_a:
            '''
            Este bucle se ejecuta si todavía hay elementos restantes en pila_a 
            después de que pila_b se haya agotado.
            Este bucle añade los elementos restantes de pila_a a self.resultado.
            '''
            self.resultado.append(self.pila_a[i])
            i += 1

        while j < len_b:
            '''
            Este bucle se ejecuta si todavía hay elementos restantes en pila_b 
            después de que pila_a se haya agotado.
            Este bucle añade los elementos restantes de pila_b a self.resultado.
            '''
            self.resultado.append(self.pila_b[j])
            j += 1

        print("Pilas Intercaladas:")
        print(f"Pila A: {self.pila_a}")
        print(f"Pila B: {self.pila_b}")
        print(f"Resultado: {self.resultado}")

    def sumar_pilas(self):
        """
        Suma los elementos de las dos pilas y guarda el resultado en la pila de resultado.
        Muestra las pilas originales y el resultado.
        """
        self.resultado = []
        len_a = len(self.pila_a)
        len_b = len(self.pila_b)
        min_len = min(len_a, len_b)

        for i in range(min_len):
            self.resultado.append(self.pila_a[i] + self.pila_b[i])

        if len_a > len_b:
            self.resultado.extend(self.pila_a[min_len:])
        else:
            self.resultado.extend(self.pila_b[min_len:])

        print("Suma de Pilas:")
        print(f"Pila A: {self.pila_a}")
        print(f"Pila B: {self.pila_b}")
        print(f"Resultado: {self.resultado}")

def mostrar_menu():
    """
    Función para mostrar el menú de opciones al usuario.
    """
    print("\nSeleccione una opción:")
    print("1. Llenar las pilas")
    print("2. Intercalar las pilas")
    print("3. Sumar las pilas")
    print("4. Salir")

def main():
    """
    Función principal que maneja la interacción con el usuario y ejecuta las operaciones correspondientes.
    """
    gestor = PILASNUM()

    while True:
        mostrar_menu()
        try:
            opcion = int(input("Ingrese su opción: "))
            if opcion == 1:
                gestor.llenar_pilas()
            elif opcion == 2:
                gestor.intercalar_pilas()
            elif opcion == 3:
                gestor.sumar_pilas()
            elif opcion == 4:
                print("Saliendo del programa.")
                break
            else:
                print("Opción no válida, por favor seleccione una opción del menú.")
        except ValueError:
            print("Por favor, ingrese un número válido.")
        except KeyboardInterrupt:
            print("\nInterrupción del teclado detectada. Saliendo del programa.")
            break

if __name__ == "__main__":
    main()
