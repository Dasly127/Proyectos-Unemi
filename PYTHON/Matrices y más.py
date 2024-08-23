

# Crear una matriz 3x3 donde cada elemento es la suma de su fila y columna (1-indexed)
matriz = [[i + j for j in range(1, 4)] for i in range(1, 4)]

# Imprimir la matriz
for fila in matriz:
    print(fila)
