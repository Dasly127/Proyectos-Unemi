

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
    posiciones_ganadoras = [
        (0, 1, 2),  # Filas
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),  # Columnas
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),  # Diagonales
        (2, 4, 6)
    ]
    for posiciones in posiciones_ganadoras:
        if tablero[posiciones[0]] == tablero[posiciones[1]] == tablero[posiciones[2]] != " ":
            return tablero[posiciones[0]]  # Devuelve el símbolo del jugador ganador (0 o 1)
    return None

def tablero_lleno(tablero):
    """Verifica si el tablero está lleno (empate)"""
    return " " not in tablero  # Si no quedan espacios vacíos, es empate

def juego_del_3_en_rayas():
    """Simula el juego del 3 en rayas"""
    tablero = [" "] * 9  # Inicializamos un tablero vacío
    jugador_actual = "0"  # El jugador 0 empieza
    jugada = 0

    while True:
        imprimir_tablero(tablero)
        print(f"Turno del jugador {jugador_actual} (jugada {jugada+1})")

        # Escoger una posición aleatoria vacía
        posicion = random.choice([i for i, x in enumerate(tablero) if x == " "])
        tablero[posicion] = jugador_actual
        jugada += 1

        # Verificar si hay un ganador después de la jugada
        ganador = verificar_ganador(tablero)
        if ganador:
            imprimir_tablero(tablero)
            print(f"¡Ganó el jugador {ganador} con la jugada {jugada}!")
            break

        # Verificar si el tablero está lleno (empate)
        if tablero_lleno(tablero):
            imprimir_tablero(tablero)
            print("¡Empate! No quedan más jugadas posibles.")
            break

        # Cambiar al siguiente jugador (alternar entre "0" y "1")
        jugador_actual = "1" if jugador_actual == "0" else "0"

# Ejecutar el juego
juego_del_3_en_rayas()

