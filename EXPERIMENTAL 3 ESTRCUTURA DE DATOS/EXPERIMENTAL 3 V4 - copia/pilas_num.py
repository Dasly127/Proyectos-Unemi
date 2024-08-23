
class PILAS_NUM:
    def __init__(self):
        self.pila1 = []
        self.pila2 = []
        self.pila_intercalada = []
        self.pila_suma = []

    def llenar_pilas(self):
        self.pila1 = self._llenar_pila(1, 5)
        self.pila2 = self._llenar_pila(2, 7)

    def _llenar_pila(self, numero_pila, cantidad_elementos):
        pila = []
        for i in range(cantidad_elementos):
            while True:
                try:
                    elemento = int(input(f"Ingresa el elemento {i + 1} para la pila {numero_pila}: "))
                    pila.append(elemento)
                    break
                except ValueError:
                    print("Entrada no válida. Por favor, ingresa un número entero.")
        return pila

    def intercalar_pilas(self):
        try:
            # Hacer una copia de las pilas originales para no modificarlas
            pila1_copia = self.pila1.copy()
            pila2_copia = self.pila2.copy()
            self.pila_intercalada = self._intercalar(pila1_copia, pila2_copia)
            self._mostrar_info("Pila 1 inicial", self.pila1)
            self._mostrar_info("Pila 2 inicial", self.pila2)
            self._mostrar_info("Pila intercalada", self.pila_intercalada)
        except Exception as e:
            print(f"Error al intercalar pilas: {e}")

    def _intercalar(self, pila1, pila2):
        intercalada = []
        pila_mayor, pila_menor = (pila1, pila2) if len(pila1) > len(pila2) else (pila2, pila1)
        
        # Intercalar elementos hasta que la pila menor esté vacía
        while pila_menor:
            intercalada.append(pila_mayor.pop())
            intercalada.append(pila_menor.pop())
        
        # Agregar los elementos sobrantes de la pila mayor
        while pila_mayor:
            intercalada.append(pila_mayor.pop())
        
        return intercalada

    def sumar_pilas(self):
        try:
            # Hacer una copia de las pilas originales para no modificarlas
            pila1_copia = self.pila1.copy()
            pila2_copia = self.pila2.copy()
            self.pila_suma = self._sumar(pila1_copia, pila2_copia)
            self._mostrar_info("Pila 1 inicial", self.pila1)
            self._mostrar_info("Pila 2 inicial", self.pila2)
            self._mostrar_info("Suma ajustada de las pilas", self.pila_suma)
        except Exception as e:
            print(f"Error al sumar pilas: {e}")

    def _sumar(self, pila1, pila2):
        suma = []
        pila_mayor, pila_menor = (pila1, pila2) if len(pila1) > len(pila2) else (pila2, pila1)
        
        # Sumar elementos hasta que la pila menor esté vacía
        while pila_menor:
            suma.append(pila_mayor.pop() + pila_menor.pop())
        
        # Agregar los elementos sobrantes de la pila mayor
        while pila_mayor:
            suma.append(pila_mayor.pop())
        
        return suma

    def mostrar_pilas(self):
        try:
            self._mostrar_info("Pila 1", self.pila1)
            self._mostrar_info("Pila 2", self.pila2)
            if self.pila_intercalada:
                self._mostrar_info("Pila intercalada", self.pila_intercalada)
            if self.pila_suma:
                self._mostrar_info("Pila suma", self.pila_suma)
        except Exception as e:
            print(f"Error al mostrar pilas: {e}")

    def _mostrar_info(self, titulo, pila):
        print(f"{titulo}: {' '.join(map(str, pila))}")



'''
    ###EXPLICACIÓN DEL CÓDIGO###

    => Constructor de la clase PILAS_NUM.
            Inicializa las pilas como listas vacías:
            - self.pila1: contendrá los primeros 5 elementos ingresados.
            - self.pila2: contendrá los siguientes 7 elementos ingresados.
            - self.pila_intercalada: contendrá los elementos de pila1 y pila2 intercalados.
            - self.pila_suma: contendrá los elementos resultantes de sumar pila1 y pila2.


    => def llenar_pilas(self):
            
            Método para llenar las pilas con elementos ingresados por el usuario.
            Llama al método auxiliar _llenar_pila para llenar cada pila con la cantidad específica de elementos.
            
            self.pila1 = self._llenar_pila(1, 5)
            self.pila2 = self._llenar_pila(2, 7)

            
    => def _llenar_pila(self, numero_pila, cantidad_elementos):
        
            Método auxiliar para llenar una pila con una cantidad específica de elementos ingresados por el usuario.
            
            Parámetros:
            - numero_pila: Identificador de la pila (1 o 2) para mostrar en los mensajes.
            - cantidad_elementos: Número de elementos que debe contener la pila.
            
            Retorna:
            - Una lista con los elementos ingresados por el usuario.
            

    => def intercalar_pilas(self):
            
            Método para intercalar los elementos de las dos pilas (pila1 y pila2).
            Imprime las pilas originales y la pila intercalada resultante.
            Maneja excepciones que puedan ocurrir durante el proceso.
            

    => def _intercalar(self, pila1, pila2):
            
            Método auxiliar para intercalar los elementos de dos pilas.
            Comienza con la pila que tiene más elementos y alterna elementos de ambas pilas.
            Los elementos sobrantes de la pila más larga se añaden al final de la pila intercalada.
            
            Parámetros:
            - pila1: Lista con los elementos de la primera pila.
            - pila2: Lista con los elementos de la segunda pila.
            
            Retorna:
            - Una lista con los elementos intercalados.
            
    => def sumar_pilas(self):
            
            Método para sumar los elementos de las dos pilas (pila1 y pila2).
            Imprime las pilas originales y la suma ajustada de las pilas.
            Maneja excepciones que puedan ocurrir durante el proceso.


    => def _sumar(self, pila1, pila2):
            
            Método auxiliar para sumar los elementos de dos pilas.
            Suma los elementos hasta la longitud de la pila más corta y añade los elementos sobrantes de la pila más larga.
            
            Parámetros:
            - pila1: Lista con los elementos de la primera pila.
            - pila2: Lista con los elementos de la segunda pila.
            
            Retorna:
            - Una lista con la suma ajustada de las pilas.


    => def mostrar_pilas(self):
            
            Método para mostrar el contenido de las pilas.
            Imprime el contenido de pila1, pila2 y, si existen, pila_intercalada y pila_suma.
            Maneja excepciones que puedan ocurrir durante el proceso.
'''