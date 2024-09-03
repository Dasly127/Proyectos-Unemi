

import random

def inicializar_matriz():
    return [[None, None, None], [None, None, None], [None, None, None]]

def verificar_ganador(matriz, jugador):
    # Verificar filas y columnas
    for i in range(3):
        if matriz[i][0] == matriz[i][1] == matriz[i][2] == jugador:
            return True, f"Ganó el jugador que utiliza el {jugador} en una fila"
        if matriz[0][i] == matriz[1][i] == matriz[2][i] == jugador:
            return True, f"Ganó el jugador que utiliza el {jugador} en una columna"
    
    # Verificar diagonales
    if matriz[0][0] == matriz[1][1] == matriz[2][2] == jugador:
        return True, f"Ganó el jugador que utiliza el {jugador} en una diagonal"
    if matriz[0][2] == matriz[1][1] == matriz[2][0] == jugador:
        return True, f"Ganó el jugador que utiliza el {jugador} en una diagonal inversa"
    
    return False, ""

def imprimir_matriz(matriz):
    for fila in matriz:
        print(fila)

def jugar():
    matriz = inicializar_matriz()
    posiciones_disponibles = [(i, j) for i in range(3) for j in range(3)]
    jugadores = [0, 1]
    
    turno = 0
    while posiciones_disponibles:
        jugador_actual = jugadores[turno % 2]
        posicion = random.choice(posiciones_disponibles)
        posiciones_disponibles.remove(posicion)
        
        matriz[posicion[0]][posicion[1]] = jugador_actual
        imprimir_matriz(matriz)
        print("\n")
        
        ganador, mensaje = verificar_ganador(matriz, jugador_actual)
        if ganador:
            print(mensaje)
            break
        
        turno += 1

# Iniciar el juego
jugar()
