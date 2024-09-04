

import math  # Importamos la librería Math de Python


# Función para calcular los errores
def calcular_errores(valor_real, valor_estimado):
    """
    Calculamos el error absoluto y relativo entre un valor real y un valor estimado.
    
    -paramametro1: valor_real: Valor verdadero de la magnitud
    -paramametro2: valor_estimado: Valor estimado o aproximado
    -retorna: Tupla con el error absoluto y el error relativo
    """

    # Cálculo de los errores
    error_absoluto = abs(valor_real - valor_estimado)
    error_relativo = (error_absoluto / valor_real) * 100
    return error_absoluto, error_relativo

def mostrar_resultados(ejercicio, valor_estimado, valor_real):
    """
    Muestra los resultados de error absoluto y relativo de una aproximación específica de pi.
    
    :parametro ejercicio: Número del ejercicio
    :parametro valor_estimado: Valor estimado de pi
    :parametro valor_real: Valor real de pi (math.pi)
    """

    # Llamamos a la función calcular_errores() para sacar los errores Abs, y relativo
    ea, er = calcular_errores(valor_real, valor_estimado)

    # Mostramos por pantalla los errores
    print(f"Ejercicio {ejercicio} - Aproximación de π: {valor_estimado}")
    print(f"Error absoluto: {ea}")
    print(f"Error relativo: {er}%\n")

# Definimos el valor verdadero de pi con math.pi
valor_real_pi = math.pi

# Ejercicio 1.1 - Aproximación de pi como 3.14
mostrar_resultados("1.1", 3.14, valor_real_pi)

# Ejercicio 1.2 - Aproximación de pi usando 22/7
mostrar_resultados("1.2", 22 / 7, valor_real_pi)

# Ejercicio 1.3 - Aproximación de pi como 3.1416
mostrar_resultados("1.3", 3.1416, valor_real_pi)
