


class PILAS_NUM:
    """
    Clase que representa una estructura de datos compuesta por dos pilas. 
    Permite llenar las pilas con 5 y 7 elementos numéricos cada una, intercalarlas o sumar sus valores.
    """
    def __init__(self):
        # Creamos las pilas
        self.pila1 = []
        self.pila2 = []

    def llenar_pilas(self):
        # Llenamos la pila1 con 5 elementos
        self.pila1 = self._llenar_pila(5, "pila 1")

        # Llenamos la pila2 con 7 elementos
        self.pila2 = self._llenar_pila(7, "pila 2")

    def _llenar_pila(self, cantidad, nombre_pila):
        pila = []
        for i in range(cantidad):
            while True:
                try:
                    elemento = int(input(f"Ingrese un número para {nombre_pila} (elemento {i + 1}): "))
                    pila.append(elemento)
                    break
                except ValueError:
                    print("Entrada no válida. Por favor, ingrese un número entero.")
        return pila

    def intercalar_pilas(self):
        try:
            # Definimos la pila final
            pila_final = self._intercalar(self.pila1, self.pila2)
            
            # Imprimimos los datos de las pilas originales
            print(f"Datos de la pila 1: {self.pila1}")
            print(f"Datos de la pila 2: {self.pila2}")

            # Mostramos la pila final
            print(f"Intercalación de pilas: {pila_final}")
        except Exception as e:
            print(f"Error al intercalar pilas: {e}")

    def _intercalar(self, pila1, pila2):
        pila_final = []
        if len(pila1) >= len(pila2):
            pila_mayor = pila1[:]
            pila_menor = pila2[:]
        else:
            pila_mayor = pila2[:]
            pila_menor = pila1[:]

        # Intercalamos los elementos
        while len(pila_mayor) > 0 or len(pila_menor) > 0:
            if len(pila_mayor) > 0:
                pila_final.append(pila_mayor.pop(0))
            if len(pila_menor) > 0:
                pila_final.append(pila_menor.pop(0))

        return pila_final

    def sumar_pilas(self):
        try:
            # Verificar si las pilas tienen el mismo tamaño
            if len(self.pila1) != len(self.pila2):
                raise ValueError("Las pilas no tienen el mismo tamaño y no se pueden sumar elemento a elemento.")

            # Definimos la pila final
            pila_final = self._sumar(self.pila1, self.pila2)
            
            # Imprimimos los datos de las pilas originales
            print(f"Datos de la pila 1: {self.pila1}")
            print(f"Datos de la pila 2: {self.pila2}")

            # Mostramos la pila final
            print(f"Suma de pilas: {pila_final}")
        except Exception as e:
            print(f"Error al sumar pilas: {e}")

    def _sumar(self, pila1, pila2):
        pila_final = []
        for i in range(len(pila1)):
            pila_final.append(pila1[i] + pila2[i])
        return pila_final

    def mostrar_pilas(self):
        try:
            print("Pila 1:", self.pila1)
            print("Pila 2:", self.pila2)
        except Exception as e:
            print(f"Error al mostrar pilas: {e}")


# Programa principal
def main():
    pilas_num = PILAS_NUM()

    # Llenamos las pilas
    pilas_num.llenar_pilas()

    while True:
        try:
            # Elegimos la operación a realizar
            opcion = int(input("""Seleccione la operación que desea realizar:
1. Intercalar pilas
2. Sumar pilas
3. Mostrar pilas
4. Salir

Ingrese su opción: """))

            if opcion == 1:
                pilas_num.intercalar_pilas()
            elif opcion == 2:
                pilas_num.sumar_pilas()
            elif opcion == 3:
                pilas_num.mostrar_pilas()
            elif opcion == 4:
                print("Saliendo del programa.")
                break
            else:
                print("Opción inválida. Por favor, seleccione una opción válida.")
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número entero.")
        except Exception as e:
            print(f"Error en la ejecución del programa: {e}")

if __name__ == "__main__":
    main()
