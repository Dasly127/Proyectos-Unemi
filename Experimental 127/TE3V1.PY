

class PILAS_NUM:
  """
  Clase que representa una estructura de datos compuesta por dos pilas. Permite llenar las pilas con 5 y 7 elementos numéricos cada una, intercalarlas o sumar sus valores.
  """
  def __init__(self):
    # Creamos las pilas
    self.pila1 = []
    self.pila2 = []

  def llenar_pilas(self):
    # Llenamos la pila1 con 5 elementos
    for i in range(5):
      self.pila1.append(int(input(f"Ingrese un número para la pila 1: ")))

    # Llenamos la pila2 con 7 elementos
    for i in range(7):
      self.pila2.append(int(input(f"Ingrese un número para la pila 2: ")))

  def intercalar_pilas(self):
    # Definimos la pila final
    pila_final = []

    # Combinamos los elementos de las pilas, iniciando con la que tiene más elementos
    if len(self.pila1) >= len(self.pila2):
      pila_mayor = self.pila1
      pila_menor = self.pila2
    else:
      pila_mayor = self.pila2
      pila_menor = self.pila1

    # Intercalamos los elementos
    while len(pila_mayor) > 0 or len(pila_menor) > 0:
      if len(pila_mayor) > 0:
        pila_final.append(pila_mayor.pop())
      if len(pila_menor) > 0:
        pila_final.append(pila_menor.pop())

    # Imprimimos los datos de las pilas originales
    print(f"Datos de la pila 1: {self.pila1}")
    print(f"Datos de la pila 2: {self.pila2}")

    # Mostramos la pila final
    print(f"Intercalación de pilas: {pila_final}")

  def sumar_pilas(self):
    # Definimos la pila final
    pila_final = []

    # Sumamos los elementos de las pilas, manteniendo el orden original
    for i in range(len(self.pila1)):
      pila_final.append(self.pila1[i] + self.pila2[i])

    # Imprimimos los datos de las pilas originales
    print(f"Datos de la pila 1: {self.pila1}")
    print(f"Datos de la pila 2: {self.pila2}")

    # Mostramos la pila final
    print(f"Suma de pilas: {pila_final}")


# Creamos una instancia de la clase PILAS_NUM
pilas_num = PILAS_NUM()

# Llenamos las pilas
pilas_num.llenar_pilas()

# Elegimos la operación a realizar
opcion = int(input("""Seleccione la operación que desea realizar:
1. Intercalar pilas
2. Sumar pilas

Ingrese su opción: """))

if opcion == 1:
  pilas_num.intercalar_pilas()
elif opcion == 2:
  pilas_num.sumar_pilas()
else:
  print("Opción inválida.")
