

## Creamos una función llamada encontrar_suma_máxima

def encontrar_suma_maxima(secuencia):
    ## Inicializamos la suma máxima como un valor muy pequeño
    suma_max = float('-inf')  # Inicializamos la suma máxima como un valor muy pequeño
    
    ## Iteramos sobre la secuencia para encontrar la suma máxima de números adyacentes
    for i in range(len(secuencia) - 1):

        ## Calculamos la suma de los números adyacentes en la posición actual y la siguiente
        suma_actual = secuencia[i] + secuencia[i + 1]

        ## Condicional para actualizar la suma máxima si encontramos una suma mayor
        if suma_actual > suma_max:
            suma_max = suma_actual
    
    return suma_max ##Llamada a la Función

## Creamos una función para solicitar los números
def main():

     ## Se solicita al usuario que ingrese los números separados por espacios
    numeros = input("Ingrese los números separados por espacios: ").split()

    # Condicional para validar si se ingresaron suficientes números
    if len(numeros) < 2: #Validación de números
        print("Debe ingresar al menos dos números. Inténtelo de nuevo.")
        return
    
    try:
        numeros = list(map(int, numeros))
    except ValueError:
        print("Ingrese números enteros separados por espacios. Inténtelo de nuevo.")
        return

    suma_maxima = encontrar_suma_maxima(numeros) #Llamada a la función
    
    print("La suma máxima de números adyacentes es:", suma_maxima)

if __name__ == "__main__":
    main()


