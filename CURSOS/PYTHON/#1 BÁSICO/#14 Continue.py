"""
Recuerda que Range te indica que rango de números quieres mostrar
Recuerda que "Continue" Sirve para que si la condición no se cumple
vaya directo a la proxíma línea de código
"""


# for i in range(6):
#     if i % 2 == 0: si es divisible para 2 es un número par
#         print(f'Valor: {i}')

for i in range(6):
    if i % 2 != 0:
        continue
    print(f'Valor: {i}')