

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
def serie_de_taylor(funcion, variable, punto, orden):
    return sp.series(funcion, variable, punto, orden).removeO()



'''
Esta función calcula el error de truncamiento, que es la diferencia entre la función original 
y su aproximación por la serie de Taylor.
Evalúa este error en un punto específico dado por punto_evaluacion.
'''
def error_de_truncamiento(funcion, variable, punto, orden, punto_evaluacion):
    taylor_truncada = serie_de_taylor(funcion, variable, punto, orden)
    termino_error = funcion - taylor_truncada
    error_evaluado = termino_error.subs(variable, punto_evaluacion)
    return error_evaluado



'''

'''
ordenes = [2, 3, 4, 5]
expansiones_taylor = [serie_de_taylor(f_exp, x, 0, orden) for orden in ordenes]

# Imprimir las expansiones de Taylor
for i, expansion in enumerate(expansiones_taylor):
    print(f"Serie de Taylor de e^x hasta el orden {i+1}: {expansion}")

# Calcular y mostrar el error de truncamiento para cada orden
valor_x = 0.1  # Puedes cambiar este valor para evaluar en otro punto
errores_truncamiento = [error_de_truncamiento(f_exp, x, 0, orden, valor_x) for orden in ordenes]

for i, error in enumerate(errores_truncamiento):
    print(f"Error de truncamiento en el orden {i+1} para x={valor_x}: {error.evalf()}")
