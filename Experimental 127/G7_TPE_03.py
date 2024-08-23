

class PILAS_NUM:
    """
    Clase que representa una estructura de datos compuesta por dos pilas.
    Permite llenar las pilas con 5 y 7 elementos numéricos cada una, intercalarlas o sumar sus valores.
    """
    def __init__(self):
        # Creamos las pilas
        self.pila_num1 = []
        self.pila_num2 = []

    def llenar_pilas_num(self):
        """
        Llena las pilas con números ingresados por el usuario.
        """
        self.pila_num1 = self._llenar_pila_num(5, "pila 1")
        self.pila_num2 = self._llenar_pila_num(7, "pila 2")

    def _llenar_pila_num(self, cantidad_elementos, nombre_pila_num):
        """
        Llena una pila específica con la cantidad de elementos especificada.
        """
        pila = []
        for i in range(cantidad_elementos):
            while True:
                try:
                    elemento_num = int(input(f"Ingrese un número para {nombre_pila_num} (elemento {i + 1}): "))
                    pila.append(elemento_num)
                    break
                except ValueError:
                    print("Debe ingresar un número válido.")
        return pila

    def intercalar_pilas_num(self):
        """
        Intercala las dos pilas y muestra el resultado.
        """
        try:
            # Crear copias de las pilas originales
            pila1_copia = self.pila_num1.copy()
            pila2_copia = self.pila_num2.copy()
            pila_resultado = self._intercalar_pilas(pila1_copia, pila2_copia)
            self._mostrar_pilas()
            print(f"Intercalación de pilas: {pila_resultado}")
        except Exception as error:
            print(f"Error al intercalar pilas: {error}")

    def _intercalar_pilas(self, pila1, pila2):
        """
        Realiza la intercalación de dos pilas y retorna la pila resultante.
        """
        pila_resultado = []
        pila_mayor, pila_menor = (pila1, pila2) if len(pila1) > len(pila2) else (pila2, pila1)

        while pila_mayor or pila_menor:
            if pila_mayor:
                pila_resultado.append(pila_mayor.pop())
            if pila_menor:
                pila_resultado.append(pila_menor.pop())

        return pila_resultado

    def sumar_pilas_num(self):
        """
        Suma los elementos de las dos pilas y muestra el resultado.
        """
        try:
            # Crear copias de las pilas originales
            pila1_copia = self.pila_num1.copy()
            pila2_copia = self.pila_num2.copy()
            pila_resultado = self._sumar_pilas(pila1_copia, pila2_copia)
            self._mostrar_pilas()
            print(f"Suma de pilas: {pila_resultado}")
        except Exception as error:
            print(f"Error al sumar pilas: {error}")

    def _sumar_pilas(self, pila1, pila2):
        """
        Realiza la suma de los elementos de dos pilas y retorna la pila resultante.
        """
        pila_resultado = []
        pila_mayor, pila_menor = (pila1, pila2) if len(pila1) > len(pila2) else (pila2, pila1)

        while pila_menor:
            pila_resultado.append(pila_mayor.pop() + pila_menor.pop())

        while pila_mayor:
            pila_resultado.append(pila_mayor.pop())

        return pila_resultado

    def _mostrar_pilas(self):
        """
        Muestra el contenido de las pilas.
        """
        print(f"Datos de la pila 1: {self.pila_num1}")
        print(f"Datos de la pila 2: {self.pila_num2}")

# Programa principal
def main():
    pilas_num = PILAS_NUM()
    pilas_num.llenar_pilas_num()

    while True:
        try:
            opcion_menu = int(input("""Seleccione la operación que desea realizar:
1. Intercalar las pilas
2. Sumar las pilas
3. Finalizar el programa

Ingrese su opción: """))

            if opcion_menu == 1:
                pilas_num.intercalar_pilas_num()
            elif opcion_menu == 2:
                pilas_num.sumar_pilas_num()
            elif opcion_menu == 3:
                print("Saliendo del programa.")
                break
            else:
                print("Seleccione una de las opciones disponibles por favor.")
        except ValueError:
            print("Debe ingresar una de las opciones proporcionadas.")
        except Exception as error:
            print(f"Error en la ejecución del programa: {error}")

if __name__ == "__main__":
    main()
