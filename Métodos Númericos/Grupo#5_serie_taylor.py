


import sympy as sp

# Definir la variable simbólica
x = sp.symbols('x')

# Definir la función f(x) = e^x
f_exp = sp.exp(x)

# Función para calcular la Serie de Taylor
def serie_de_taylor(funcion, variable, punto, orden):
    return sp.series(funcion, variable, punto, orden).removeO()

# Función para calcular el error de truncamiento
def error_de_truncamiento(funcion, variable, punto, orden, punto_evaluacion):
    taylor_truncada = serie_de_taylor(funcion, variable, punto, orden)
    termino_error = funcion - taylor_truncada
    error_evaluado = termino_error.subs(variable, punto_evaluacion)
    return error_evaluado

# Calcular la Serie de Taylor de e^x alrededor de 0 hasta el orden 4
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
