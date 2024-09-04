
# Importamos la librería sympy para hacer cálculos simbólicos
import sympy as sp

# Definir la variable simbólica
# Esta variable será nuestra variable independiente en las funciones que definamos
x = sp.symbols('x')


# Definir el punto de expansión a = pi/4 
a = sp.pi / 4


# Definimos la función f(x) = cos(x) usando la función coseno de SymPy.
f_cos = sp.cos(x)


'''
Creamos la función para calcular la Serie de Taylor

Esta función recibe como parámetros:
- funcion: La función simbólica que se desea expandir.
- variable: La variable independiente (en este caso, 'x').
- punto: El punto alrededor del cual se calculará la expansión (en este caso, pi/4).
- orden: El número de términos hasta el cual se expandirá la serie (orden de la serie).
'''
def serie_de_taylor(funcion, variable, punto, orden):
    # Utilizamos sp.series() para calcular la serie de Taylor y eliminamos el término de orden superior.
    return sp.series(funcion, variable, punto, orden).removeO()


'''
Creamos una función para calcular el error de truncamiento.
Esta función toma como parámetros:
- funcion: La función original (en este caso, cos(x)).
- variable: La variable independiente (en este caso, 'x').
- punto: El punto alrededor del cual se expande la serie (pi/4).
- orden: El orden de la serie de Taylor hasta donde calculamos.
- punto_evaluacion: El valor de 'x' donde queremos evaluar el error de truncamiento.
'''
def error_de_truncamiento(funcion, variable, punto, orden, punto_evaluacion):
    
    # Calculamos la serie de Taylor truncada usando la función serie_de_taylor.
    taylor_truncada = serie_de_taylor(funcion, variable, punto, orden)

    # Calculamos el término de error restando la serie truncada de la función original.
    termino_error = funcion - taylor_truncada

    # Evaluamos el error en el punto especificado.
    error_evaluado = termino_error.subs(variable, punto_evaluacion)

    # Retornamos el valor del error de truncamiento en el punto de evaluación.
    return error_evaluado

# Creamos la lista con los órdenes de la serie que queremos calcular
ordenes = [2, 3, 4]

# Calculamos la Serie de Taylor de cos(x) alrededor de pi/4 para los órdenes indicados.
expansiones_taylor = [serie_de_taylor(f_cos, x, a, orden) for orden in ordenes]  # Compresión de lista


# Imprimimos las expansiones de Taylor para cada uno de los ordenes 
for i, expansion in enumerate(expansiones_taylor):
    print(f"Serie de Taylor de cos(x) hasta el orden {i+1}: {expansion}")

# Definimos el valor de 'x' donde queremos evaluar el error de truncamiento.
valor_x = sp.pi / 4 + 0.1  # Se puede cambiar este valor para evaluar en otro punto

# Calculamos el error de truncamiento para cada orden usando la función definida
errores_truncamiento = [error_de_truncamiento(f_cos, x, a, orden, valor_x) for orden in ordenes] # Compresión de lista para calcular error en cada orden

# Mostramos los errores de truncamiento para cada orden en el punto x
for i, error in enumerate(errores_truncamiento):
    print(f"Error de truncamiento en el orden {i+1} para x={valor_x}: {error.evalf()}")
