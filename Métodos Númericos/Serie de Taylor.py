
import sympy as sp

def serie_de_taylor(funcion, variable, punto, orden):
    """
    :param funcion: La función simbólica de SymPy.
    :param variable: La variable simbólica de SymPy.
    :param punto: El punto alrededor del cual se expande la serie (por ejemplo, 0).
    :param orden: El orden hasta el cual expandir la serie.
    :return: La Serie de Taylor truncada.
    """
    expansion_taylor = sp.series(funcion, variable, punto, orden).removeO()  # Quita el término de orden superior (O)
    return expansion_taylor

def error_de_truncamiento(funcion, variable, punto, orden, punto_evaluacion):
    """
    Calcula el error de truncamiento al truncar la Serie de Taylor en un cierto orden.
    
    :param funcion: La función simbólica de SymPy.
    :param variable: La variable simbólica de SymPy.
    :param punto: El punto alrededor del cual se expande la serie.
    :param orden: El orden en el cual se truncó la serie.
    :param punto_evaluacion: El punto en el cual se evalúa el error.
    :return: El error de truncamiento evaluado en el punto dado.
    """
    # Expansión de Taylor truncada
    taylor_truncada = serie_de_taylor(funcion, variable, punto, orden)
    
    # Calcular el término de error (f(x) - Serie de Taylor truncada)
    termino_error = funcion - taylor_truncada
    error_evaluado = termino_error.subs(variable, punto_evaluacion)
    
    return error_evaluado

# Definir la variable simbólica
x = sp.symbols('x')

# Función 1: f(x) = e^x
f_exp = sp.exp(x)

# Función 2: f(x) = sin(x)
f_seno = sp.sin(x)

# Función 3: f(x) = ln(1 + x)
f_ln = sp.ln(1 + x)

# Calcular la Serie de Taylor y el error de truncamiento para cada función

# 1. f(x) = e^x
taylor_exp_exp = serie_de_taylor(f_exp, x, 0, 2)
error_exp = error_de_truncamiento(f_exp, x, 0, 2, 0.1)
print(f"Serie de Taylor truncada de e^x (hasta x^1): {taylor_exp_exp}")
print(f"Error de truncamiento en e^x para x=0.1: {error_exp.evalf()}")

# 2. f(x) = sin(x)
taylor_exp_seno = serie_de_taylor(f_seno, x, 0, 2)
error_seno = error_de_truncamiento(f_seno, x, 0, 2, 0.1)
print(f"Serie de Taylor truncada de sin(x) (hasta x^1): {taylor_exp_seno}")
print(f"Error de truncamiento en sin(x) para x=0.1: {error_seno.evalf()}")

# 3. f(x) = ln(1 + x)
taylor_exp_ln = serie_de_taylor(f_ln, x, 0, 2)
error_ln = error_de_truncamiento(f_ln, x, 0, 2, 0.1)
print(f"Serie de Taylor truncada de ln(1+x) (hasta x^1): {taylor_exp_ln}")
print(f"Error de truncamiento en ln(1+x) para x=0.1: {error_ln.evalf()}")
