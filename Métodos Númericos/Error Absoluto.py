

"""
 Ejercicio 1:
Implementar un programa en Python para calcular el error absoluto y
relativo para diferentes aproximaciones de una constante matemática (como π).
"""

# Creamos la función para calcular el error absoluto
def error_absoluto(valor_real, valor_estimado): # Recibe como parámetro las variables de la fórmula

    # Agregamos una condición para que se validen los datos
    if valor_real < 0:  # Si el valor real es menor que 0
        return "Ingrese un valor real correcto." # nos retornará un mensaje de error
   
   
    if valor_estimado < 0: # Si el valor estimado es menor que 0 
        return "Ingrese un valor estimado correcto." # nos retornará un mensaje de error
    
    # Si todas las condiciones se cumplen el programa retorna la fórmula
    return abs(valor_real - valor_estimado) # Hacienso uso de la Función ABS logramos calcular la formula con valor absoluto



# Creamos la función para calcular el error relativo
def error_relativo(valor_real, valor_estimado): # Recibe como parámetro las variables de la fórmula 2

    # Agregamos una condición para que se validen los datos
    if valor_real == 0: # Si valor real es igual a 0
        return "El valor real no puede ser cero." # nos retornará este mensaje de error
    
    # Si no hay problema con la condición la función retorna la operación de la fórmula
    return abs((valor_real - valor_estimado) / valor_real)


# Hacemos uso de un Bucle While para crear el menú de opciones
while True:

    # Mandamos a imprimir por pantalla el menú de opciones
    print("Menú de opciones Grupo 5".center(60, '-'))
    print("1. Calcular el error absoluto")
    print("2. Calcular el error relativo")
    print("3. Salir del Programa")


    # Creamos un bloque de código para manejar excepciones en el menú
    try:
        opción = int(input("\nSelecciona una opción: ")) # Creamos una variable para almacenar la opción seleccionada
    except ValueError:
        print("Por favor, ingresa un número válido para la opción.")
        continue
    
    # Creamos una condición para poder validar las opciones y que el programa ejecute lo que el usuario escoga

    # Condición 1: si el usuario ingresa 1 se ejecuta la función del error Absoluto
    if opción == 1:
        try:

            ### Solicitamos al usuario ingresar el número y lo convertimos a flotante
            ### Usamos .replace para cambiar la coma por punto ya que Python solo reconoce Puntos y no comas
            ### Asignamos la variable de error que hará el llamado a la función y hará el cálculo
            valor_real = float(input("Ingrese el valor real por favor: ").replace(',', '.'))
            valor_estimado = float(input("Ingrese el valor estimado por favor: ").replace(',', '.'))
            error1 = error_absoluto(valor_real, valor_estimado)
            print("El error absoluto es:", error1)
        except ValueError:
            print("Por favor, ingrese valores numéricos válidos.")
    
    # Condición 2: si el usuario ingresa 2 se ejecuta la función del error Relativo
    elif opción == 2:
        try:

            ### Solicitamos al usuario ingresar el número y lo convertimos a flotante
            ### Usamos .replace para cambiar la coma por punto ya que Python solo reconoce Puntos y no comas
            ### Asignamos la variable de error que hará el llamado a la función y hará el cálculo
            valor_real = float(input("Ingrese el valor real por favor: ").replace(',', '.'))
            valor_estimado = float(input("Ingrese el valor estimado por favor: ").replace(',', '.'))
            error2 = error_relativo(valor_real, valor_estimado)
            print("El error relativo es:", error2)
        # Agregamos una excepción para mostrar al usuario que ingresó una opción no válida
        except ValueError:
            print("Por favor, ingrese valores numéricos válidos.")
    
    # Condición 3: Si el usuario ingresa el número 3 se cierra el programa
    elif opción == 3:
        print("Gracias por usar nuestro programa, buen día") # Mandamos un mensaje por pantalla
        
        
        # Rompemos el Bucle con un break
        break
    # Condición else: servirá para que se muestre un mensaje de error 
    else:
        print("Opción no válida, por favor seleccione una opción válida del menú.")



  
