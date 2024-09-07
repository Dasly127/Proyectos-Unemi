


import random

# Crear una matriz 3x3 vacía
def crear_matriz():
    return [["_" for _ in range(3)] for _ in range(3)]

# Mostrar la matriz en consola
def mostrar_matriz(matriz):
    for fila in matriz:
        print(" ".join(map(str, fila)))
    print()

# Verificar si hay un ganador
def verificar_ganador(matriz):
    # Verificar filas y columnas
    for i in range(3):
        if matriz[i][0] == matriz[i][1] == matriz[i][2] != "_":
            return True, matriz[i][0]
        if matriz[0][i] == matriz[1][i] == matriz[2][i] != "_":
            return True, matriz[0][i]

    # Verificar diagonales
    if matriz[0][0] == matriz[1][1] == matriz[2][2] != "_":
        return True, matriz[0][0]
    if matriz[0][2] == matriz[1][1] == matriz[2][0] != "_":
        return True, matriz[0][2]

    return False, None

# Colocar un elemento en una posición aleatoria vacía
def colocar_elemento(matriz, elemento):
    vacias = [(i, j) for i in range(3) for j in range(3) if matriz[i][j] == "_"]
    if vacias:
        i, j = random.choice(vacias)
        matriz[i][j] = elemento

# Simulación del juego
def jugar():
    matriz = crear_matriz()
    turno = 0  # 0 para el jugador 1 (0), 1 para el jugador 2 (1)
    ganador = False

    print("Simulación del juego:\n")
    
    while not ganador and any("_" in fila for fila in matriz):
        # Alternar entre 0 y 1
        elemento = turno % 2  # 0 o 1
        print(f"Turno del jugador {elemento + 1} ({elemento})")
        
        # Colocar el elemento en una posición aleatoria vacía
        colocar_elemento(matriz, elemento)
        
        # Mostrar la matriz actual
        mostrar_matriz(matriz)

        # Verificar si hay un ganador
        ganador, jugador = verificar_ganador(matriz)
        
        # Cambiar de turno
        turno += 1
    
    if ganador:
        print(f"¡Ganó el jugador {int(jugador) + 1} que utilizaba el elemento {jugador}!")
    else:
        print("¡Empate! No hay ganador.")

# Ejecutar el juego
jugar()
