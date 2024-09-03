
import sympy as sp

def taylor_series(function, var, point, order):
    """
    Calcula la Serie de Taylor de una función dada alrededor de un punto hasta un cierto orden.
    
    :param function: La función simbólica de SymPy.
    :param var: La variable simbólica de SymPy.
    :param point: El punto alrededor del cual se expande la serie (por ejemplo, 0).
    :param order: El orden hasta el cual expandir la serie.
    :return: La Serie de Taylor truncada.
    """
    taylor_expansion = sp.series(function, var, point, order).removeO()  # Quita el término de orden superior (O)
    return taylor_expansion

def truncation_error(function, var, point, order, eval_point):
    """
    Calcula el error de truncamiento al truncar la Serie de Taylor en un cierto orden.
    
    :param function: La función simbólica de SymPy.
    :param var: La variable simbólica de SymPy.
    :param point: El punto alrededor del cual se expande la serie.
    :param order: El orden en el cual se truncó la serie.
    :param eval_point: El punto en el cual se evalúa el error.
    :return: El error de truncamiento evaluado en el punto dado.
    """
    # Expansión de Taylor truncada
    taylor_truncated = taylor_series(function, var, point, order)
    
    # Calcular el término de error (f(x) - Serie de Taylor truncada)
    error_term = function - taylor_truncated
    error_evaluated = error_term.subs(var, eval_point)
    
    return error_evaluated

# Definir la variable simbólica
x = sp.symbols('x')

# Función 1: f(x) = e^x
f_exp = sp.exp(x)

# Función 2: f(x) = sin(x)
f_sin = sp.sin(x)

# Función 3: f(x) = ln(1 + x)
f_ln = sp.ln(1 + x)

# Calcular la Serie de Taylor y el error de truncamiento para cada función

# 1. f(x) = e^x
taylor_exp_exp = taylor_series(f_exp, x, 0, 2)
error_exp = truncation_error(f_exp, x, 0, 2, 0.1)
print(f"Serie de Taylor truncada de e^x (hasta x^1): {taylor_exp_exp}")
print(f"Error de truncamiento en e^x para x=0.1: {error_exp.evalf()}")

# 2. f(x) = sin(x)
taylor_exp_sin = taylor_series(f_sin, x, 0, 2)
error_sin = truncation_error(f_sin, x, 0, 2, 0.1)
print(f"Serie de Taylor truncada de sin(x) (hasta x^1): {taylor_exp_sin}")
print(f"Error de truncamiento en sin(x) para x=0.1: {error_sin.evalf()}")

# 3. f(x) = ln(1 + x)
taylor_exp_ln = taylor_series(f_ln, x, 0, 2)
error_ln = truncation_error(f_ln, x, 0, 2, 0.1)
print(f"Serie de Taylor truncada de ln(1+x) (hasta x^1): {taylor_exp_ln}")
print(f"Error de truncamiento en ln(1+x) para x=0.1: {error_ln.evalf()}")
