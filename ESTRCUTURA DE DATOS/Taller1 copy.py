



import random

def imprimir_tablero(tablero):
    """Imprime el tablero de juego"""
    print(f" {tablero[0]} | {tablero[1]} | {tablero[2]} ")
    print("---+---+---")
    print(f" {tablero[3]} | {tablero[4]} | {tablero[5]} ")
    print("---+---+---")
    print(f" {tablero[6]} | {tablero[7]} | {tablero[8]} ")

def verificar_ganador(tablero):
    """Verifica si hay un ganador"""
    combinaciones = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for combinacion in combinaciones:
        if tablero[combinacion[0]] == tablero[combinacion[1]] == tablero[combinacion[2]] != " ":
            return tablero[combinacion[0]]
    return None

def juego_del_3_en_rayas():
    """Simula el juego del 3 en rayas"""
    tablero = [" "] * 9
    jugador = "0"
    jugada = 0
    while True:
        imprimir_tablero(tablero)
        print(f"Jugada {jugada+1}: Jugador {jugador}")
        posicion = random.randint(0, 8)
        while tablero[posicion] != " ":
            posicion = random.randint(0, 8)
        tablero[posicion] = jugador
        ganador = verificar_ganador(tablero)
        if ganador:
            imprimir_tablero(tablero)
            print(f"Ganó el jugador {ganador} con la jugada {jugada+1}")
            break
        jugador = "1" if jugador == "0" else "0"
        jugada += 1

juego_del_3_en_rayas()