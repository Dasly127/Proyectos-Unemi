import random

class CartonBingo:
    """
    Clase que representa un cartón de Bingo.

    Atributos:
    - carton (list): Matriz de 5x5 que contiene los números del cartón.
    """

    def __init__(self):
        """
        Inicializa una nueva instancia de la clase CartonBingo.
        """
        self.carton = self.generar_carton()

    def generar_carton(self):
        """
        Genera un cartón de Bingo con 25 números aleatorios únicos entre 1 y 75.

        Retorno:
        - list: Matriz de 5x5 con los números del cartón.
        """
        numeros = random.sample(range(1, 76), 25)
        carton = [numeros[i:i+5] for i in range(0, 25, 5)]
        return carton

    def marcar_numero(self, numero):
        """
        Marca un número en el cartón, reemplazándolo por 'X' si está presente.

        Parámetros:
        - numero (int): Número a marcar en el cartón.
        """
        for i in range(5):
            for j in range(5):
                if self.carton[i][j] == numero:
                    self.carton[i][j] = 'X'

    def mostrar_carton(self):
        """
        Muestra el cartón de Bingo en consola.
        """
        for fila in self.carton:
            print(" ".join(f"{num:2}" for num in fila))
        print()


class Bingo:
    """
    Clase que representa el juego de Bingo.

    Atributos:
    - num_jugadores (int): Número de jugadores en el juego.
    - cartones (list): Lista de instancias de CartonBingo, uno por jugador.
    - numeros_sorteados (list): Lista de números que han sido sorteados.
    """

    def __init__(self, num_jugadores):
        """
        Inicializa una nueva instancia de la clase Bingo.

        Parámetros:
        - num_jugadores (int): Número de jugadores en el juego.
        """
        self.num_jugadores = num_jugadores
        self.cartones = [CartonBingo() for _ in range(num_jugadores)]
        self.numeros_sorteados = []

    def sortear_numero(self):
        """
        Sortea un número aleatorio entre 1 y 75 que no haya sido sorteado antes.

        Retorno:
        - int: Número sorteado.
        """
        while True:
            numero = random.randint(1, 75)
            if numero not in self.numeros_sorteados:
                self.numeros_sorteados.append(numero)
                return numero

    def actualizar_cartones(self, numero):
        """
        Actualiza todos los cartones de Bingo marcando el número sorteado.

        Parámetros:
        - numero (int): Número sorteado.
        """
        for idx, carton in enumerate(self.cartones):
            carton.marcar_numero(numero)
            if self.esta_numero_en_carton(carton, numero):
                print(f"El número {numero} marcado en el cartón del jugador {idx + 1}")

    def esta_numero_en_carton(self, carton, numero):
        """
        Verifica si un número está en el cartón de Bingo.

        Parámetros:
        - carton (CartonBingo): Instancia del cartón de Bingo.
        - numero (int): Número a verificar.

        Retorno:
        - bool: True si el número está en el cartón, False en caso contrario.
        """
        for fila in carton.carton:
            if numero in fila:
                return True
        return False

    def verificar_bingo(self):
        """
        Verifica si algún jugador ha ganado (ha completado una fila o columna).

        Retorno:
        - tuple: (bool, int) donde el primer elemento indica si hay un ganador,
                 y el segundo elemento es el índice del jugador ganador (o -1 si no hay ganador).
        """
        for idx, carton in enumerate(self.cartones):
            # Verificar filas
            for fila in carton.carton:
                if all(x == 'X' for x in fila):
                    return True, idx
            # Verificar columnas
            for col in range(5):
                if all(carton.carton[row][col] == 'X' for row in range(5)):
                    return True, idx
        return False, -1

    def mostrar_cartones(self):
        """
        Muestra todos los cartones de Bingo en consola.
        """
        for idx, carton in enumerate(self.cartones):
            print(f"Cartón del Jugador {idx + 1}:")
            carton.mostrar_carton()


def iniciar_juego():
    """
    Inicia el juego de Bingo, permitiendo la interacción del usuario para configurar el número de jugadores
    y sorteando números hasta que algún jugador gane o el juego termine.
    """
    print("Bienvenido al Bingo!")
    while True:
        try:
            num_jugadores = int(input("Ingrese el número de jugadores: "))
            if num_jugadores < 1:
                raise ValueError("Debe haber al menos un jugador.")
            break
        except ValueError as e:
            print(f"Entrada no válida: {e}")

    juego = Bingo(num_jugadores)

    print("\nCartones de Bingo generados para cada jugador:\n")
    juego.mostrar_cartones()
    
    bingo = False

    while not bingo:
        opcion = input("Presione Enter para sortear un nuevo número (o escriba 'salir' para terminar): ").strip().lower()
        if opcion == 'salir':
            print("Gracias por jugar. ¡Hasta la próxima!")
            break

        numero = juego.sortear_numero()
        print(f"\nNúmero sorteado: {numero}")
        juego.actualizar_cartones(numero)
        print()
        juego.mostrar_cartones()
        
        bingo, ganador = juego.verificar_bingo()
        if bingo:
            print(f"¡Bingo! El jugador {ganador + 1} ha ganado.")
            break


if __name__ == "__main__":
    iniciar_juego()
