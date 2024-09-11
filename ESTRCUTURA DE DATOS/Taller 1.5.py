
import random

def imprimir_tablero(tablero):
    """Imprime el tablero de juego"""
    for fila in tablero:
        print(f" {fila[0]} | {fila[1]} | {fila[2]} ")
        if tablero.index(fila) < 2:
            print("---+---+---")

def verificar_ganador(tablero):
    """Verifica si hay un ganador"""
    # Verificar filas
    for fila in tablero:
        if fila[0] == fila[1] == fila[2] and fila[0] != " ":
            return fila[0]

    # Verificar columnas
    for col in range(3):
        if tablero[0][col] == tablero[1][col] == tablero[2][col] and tablero[0][col] != " ":
            return tablero[0][col]

    # Verificar diagonales
    if tablero[0][0] == tablero[1][1] == tablero[2][2] and tablero[0][0] != " ":
        return tablero[0][0]
    if tablero[0][2] == tablero[1][1] == tablero[2][0] and tablero[0][2] != " ":
        return tablero[0][2]

    return None

def juego_del_3_en_rayas():
    """Simula el juego del 3 en rayas"""
    tablero = [[" " for _ in range(3)] for _ in range(3)]
    jugador = "0"
    jugada = 0

    while True:
        imprimir_tablero(tablero)
        print(f"Jugada {jugada+1}: Jugador {jugador}")
        fila, columna = random.randint(0, 2), random.randint(0, 2)
        while tablero[fila][columna] != " ":
            fila, columna = random.randint(0, 2), random.randint(0, 2)
        tablero[fila][columna] = jugador
        ganador = verificar_ganador(tablero)
        if ganador:
            imprimir_tablero(tablero)
            print(f"Ganó el jugador {ganador} con la jugada {jugada+1}")
            break
        jugador = "1" if jugador == "0" else "0"
        jugada += 1

juego_del_3_en_rayas()
