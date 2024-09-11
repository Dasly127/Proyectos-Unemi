
#Importamosl a librería random
import random

def imprimir_tablero(tablero):
    """
    Función que nos muestra el estado actual del tablero de juego en una estructura de 3x3.
    
    El tablero se muestra con las posiciones ocupadas por los jugadores y 
    se organizan las líneas horizontales y verticales con los separadores adecuados.
    
    Parámetros:
        tablero (list): Lista anidada de 3x3 que representa el estado del juego.
    """
    for fila in tablero:
        print(f" {fila[0]} | {fila[1]} | {fila[2]} ")  # Imprime los valores de la fila actual
        if tablero.index(fila) < 2:
            print("---+---+---")  # Imprime separadores entre filas, excepto en la última

def verificar_ganador(tablero):
    """
    Esta función nos ayuda a verificar si algún jugador ha ganado la partida.
    
    Se revisan las filas, columnas y diagonales del tablero para determinar si 
    un jugador ha alineado tres símbolos consecutivos.

    Parámetros:
        tablero (list): Lista anidada de 3x3 que representa el estado del juego.

    Retorna:
        string: Retorna el símbolo del jugador ganador ('0' o '1') si hay un ganador.
        None: Si no hay ganador aún.
    """
    # Verifica si alguna fila tiene tres símbolos iguales
    for fila in tablero:
        if fila[0] == fila[1] == fila[2] and fila[0] != " ":
            return fila[0]

    # Verifica si alguna columna tiene tres símbolos iguales
    for col in range(3):
        if tablero[0][col] == tablero[1][col] == tablero[2][col] and tablero[0][col] != " ":
            return tablero[0][col]

    # Verifica las dos diagonales posibles
    if tablero[0][0] == tablero[1][1] == tablero[2][2] and tablero[0][0] != " ":
        return tablero[0][0]
    if tablero[0][2] == tablero[1][1] == tablero[2][0] and tablero[0][2] != " ":
        return tablero[0][2]

    return None  # Retorna None si no hay ningún ganador

def juego_del_3_en_rayas():
    """
    Función que nos ayuda a simular el juego de 3 en raya automático entre dos jugadores (0 y 1).
    
    El juego se desarrolla con jugadas aleatorias en el tablero hasta que 
    un jugador gane o se complete el tablero. Los jugadores alternan turno 
    después de cada jugada.
    
    Se muestra el progreso del juego y se declara al ganador cuando se cumplan
    las condiciones de victoria.
    """
    # Inicializa un tablero vacío de 3x3
    tablero = [[" " for _ in range(3)] for _ in range(3)]
    jugador = "0"  # El jugador '0' comienza el juego
    jugada = 0  # Contador de jugadas

    # Bucle principal del juego
    while True:
        imprimir_tablero(tablero)
        print(f"Jugada {jugada+1}: Jugador {jugador}")

        # Se elige una posición aleatoria vacía para colocar el símbolo del jugador
        fila, columna = random.randint(0, 2), random.randint(0, 2)
        while tablero[fila][columna] != " ":
            fila, columna = random.randint(0, 2), random.randint(0, 2)

        tablero[fila][columna] = jugador  # Se coloca el símbolo en el tablero

        # Verifica si algún jugador ha ganado
        ganador = verificar_ganador(tablero)
        if ganador:
            imprimir_tablero(tablero)
            print(f"Ganó el jugador {ganador} con la jugada {jugada+1}")
            break  # Sale del bucle si hay un ganador

        # Alterna el turno entre los jugadores '0' y '1'
        jugador = "1" if jugador == "0" else "0"
        jugada += 1  # Incrementa el contador de jugadas

# Inicia el juego
juego_del_3_en_rayas()
