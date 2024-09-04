

'''
Usamos SymPy, una librería en Python que nos permite hacer cálculos simbólicos, 
lo que es ideal para trabajar con expansiones de Taylor.
'''
import sympy as sp

'''
Definimos una variable simbólica x usando sp.symbols(). 
Esta variable representará el valor de x que vamos a utilizar 
en nuestras funciones y series.
'''
x = sp.symbols('x')


'''
Definimos la Función f(x) de manera simbólica utilizando
sp.exp(x) que nos ayuda a crear una representación de la función
exponencial
'''
f_exp = sp.exp(x)


'''
Esta función toma como entrada una función, una variable, 
un punto de expansión y el orden de la serie de Taylor.
Usa sp.series() para calcular la serie de Taylor de la función alrededor 
del punto especificado y devuelve la serie sin el término de orden superior.
'''
def serie_de_taylor(funcion, variable, punto, orden): # Usamos sp.series() para obtener la serie de Taylor y eliminamos el término de orden superior (O)
    return sp.series(funcion, variable, punto, orden).removeO()


'''
Esta función calcula el error de truncamiento, que es la diferencia entre la función original 
y su aproximación por la serie de Taylor.
Evalúa este error en un punto específico dado por punto_evaluacion.
'''
def error_de_truncamiento(funcion, variable, punto, orden, punto_evaluacion):
    # Calculamos la serie de Taylor truncada usando la función definida anteriormente
    taylor_truncada = serie_de_taylor(funcion, variable, punto, orden)

    termino_error = funcion - taylor_truncada # Restamos la serie truncada de la función original para obtener el término de error

    error_evaluado = termino_error.subs(variable, punto_evaluacion) # Evaluamos el término de error en el punto dado (punto_evaluacion) para calcular el error
    
    return error_evaluado  # Devolvemos el valor del error en el punto de evaluación


'''
Definimos una lista con los órdenes de la serie que queremos calcular
Por ejemplo, orden = 2 significa que estamos calculando hasta el segundo término
'''
ordenes = [2, 3, 4, 5]


'''
Calculamos la Serie de Taylor de la función dada alrededor del punto 0 hasta los órdenes indicados
Usamos una comprensión de lista para calcular la serie de Taylor para cada uno de los órdenes
'''
expansiones_taylor = [serie_de_taylor(f_exp, x, 0, orden) for orden in ordenes]


'''
Imprimimos las expansiones de Taylor para cada uno de los órdenes
#Esto nos permite visualizar la aproximación de la función para cada nivel de truncamiento
'''
for i, expansion in enumerate(expansiones_taylor):
    print(f"Serie de Taylor de e^x hasta el orden {i+1}: {expansion}")




'''
Definimos el valor de 'x' en el cual queremos evaluar el error de truncamiento
Este es el punto en el que comparamos la aproximación de Taylor con el valor real de e^x
'''
valor_x = 0.1  # Podemos cambiar este valor para evaluar otro punto


'''
Calculamos el error de truncamiento para cada orden usando la función que definimos anteriormente
Nuevamente usamos una comprensión de lista para calcular el error para cada orden
'''
errores_truncamiento = [error_de_truncamiento(f_exp, x, 0, orden, valor_x) for orden in ordenes]


'''
Imprimimos los errores de truncamiento para cada orden en el punto x = valor_x
Esto nos muestra cuánto nos estamos alejando de la función real con cada aproximación de Taylor
'''
for i, error in enumerate(errores_truncamiento):
    print(f"Error de truncamiento en el orden {i+1} para x={valor_x}: {error.evalf()}")
