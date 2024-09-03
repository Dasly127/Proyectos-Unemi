
'''
El módulo math en Python contiene funciones matemáticas estándar. 
Aquí, lo utilizamos para obtener el valor verdadero de pi (math.pi).
'''

import math # Importamos la librería Math de Python


'''
Esta Función realiza dos tareas
'''

# Funciones para calcular el error absoluto y relativo
'''
Creamos la función para calcular los errores
Esta función recibe como parámetro el valor real y el valor estimado
'''
def calcular_errores(valor_real, valor_estimado):


    # Cálculo del error Absoluto
    '''
    Se calcula como la diferencia en valor absoluto entre el valor verdadero (valor_real) 
    y el valor estimado (valor_estimado).
    Utilizamos la función abs() para asegurar que el error siempre sea un valor positivo, 
    independientemente de si la aproximación es mayor o menor que el valor verdadero.
    Fórmula: error_absoluto = abs(valor_real - valor_estimado)
    '''
    error_absoluto = abs(valor_real - valor_estimado)


    # Cálculo del error Relativo
    '''
    Se calcula como el error absoluto dividido por el valor verdadero, 
    luego se multiplica por 100 para expresarlo como un porcentaje.
    Esto nos indica qué tan grande es el error en relación con el valor verdadero.
    Fórmula: error_relativo = abs((valor_real - valor_estimado) / valor_real) * 100
    '''
    error_relativo = abs((valor_real - valor_estimado) / valor_real) * 100


    # Retornamos ambos errores
    return error_absoluto, error_relativo




# Definimos el valor verdadero de pi con math.pi
valor_real_pi = math.pi



# Ejercicio 1.1 - Aproximación de pi como 3.14
aproximacion_1 = 3.14 # Definimos la primera aproximación de pi
ea_1, er_1 = calcular_errores(valor_real_pi, aproximacion_1) # Cálculamos los errores absolutos


# Usamo un f'String para mostrar los resultados por pantalla al usuario del ejercicio 1.1
print("Ejercicio 1.1 - Aproximación de π: 3.14")
print(f"Error absoluto: {ea_1}")
print(f"Error relativo: {er_1}%\n")



# Ejercicio 1.2 - Aproximación de pi usando 22/7
aproximacion_2 = 22 / 7 # Definimos la segunda aproximación de pi usando la fracción 22/7
ea_2, er_2 = calcular_errores(valor_real_pi, aproximacion_2)  # Calculamos los errores para esta aproximación


# Usamo un f'String para mostrar los resultados por pantalla al usuario del ejercicio 1.2
print("Ejercicio 1.2 - Aproximación de π: 22/7")
print(f"Error absoluto: {ea_2}")
print(f"Error relativo: {er_2}%\n")



# Ejercicio 1.3 - Aproximación de pi como 3.1416
aproximacion_3 = 3.1416 # Definimos la tercera aproximación de pi
ea_3, er_3 = calcular_errores(valor_real_pi, aproximacion_3) # Calculamos los errores para esta aproximación


# Usamo un f'String para mostrar los resultados por pantalla al usuario del ejercicio 1.3
print("Ejercicio 1.3 - Aproximación de π: 3.1416")
print(f"Error absoluto: {ea_3}")
print(f"Error relativo: {er_3}%")
