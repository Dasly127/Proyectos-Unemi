class Atraccion:
    def __init__(self, nombre, capacidad_maxima, tiempo_espera):
        self.nombre = nombre
        self.capacidad_maxima = capacidad_maxima
        self.tiempo_espera = tiempo_espera
        self.visitantes_en_espera = []

class Visitante:
    def __init__(self, nombre, edad, altura):
        self.nombre = nombre
        self.edad = edad
        self.altura = altura

class Reserva:
    def __init__(self):
        self.atracciones = []
        self.visitantes = []

def ingresar_atraccion():
    nombre = input("Nombre de la atracción: ")

    while True:
        capacidad_maxima_str = input("Capacidad máxima: ")

        # Verificar si la entrada es un número
        if capacidad_maxima_str.isdigit():
            capacidad_maxima = int(capacidad_maxima_str)
            break
        else:
            print("Por favor, ingresa un número válido para la capacidad máxima.")

    while True:
        tiempo_espera_str = input("Tiempo de espera (en minutos): ")

        # Verificar si la entrada es un número
        if tiempo_espera_str.isdigit():
            tiempo_espera = int(tiempo_espera_str)
            break
        else:
            print("Por favor, ingresa un número válido para el tiempo de espera.")

    return Atraccion(nombre, capacidad_maxima, tiempo_espera)


def ingresar_visitante():
    nombre = input("Nombre del visitante: ")

    while True:
        edad_str = input("Edad del visitante: ")

        # Verificar si la entrada es un número
        if edad_str.isdigit():
            edad = int(edad_str)
            break
        else:
            print("Por favor, ingresa un número válido para la edad.")

    while True:
        altura_str = input("Altura del visitante (en cm): ")

        # Verificar si la entrada es un número
        if altura_str.isdigit():
            altura = int(altura_str)
            break
        else:
            print("Por favor, ingresa un número válido para la altura.")

    return Visitante(nombre, edad, altura)

def mostrar_atracciones(atracciones):
    if not atracciones:
        print("No existen registros de Atracciones.")
    else:
        for atraccion in atracciones:
            print(f"Atracción: {atraccion.nombre}, Capacidad: {atraccion.capacidad_maxima}, Tiempo de espera: {atraccion.tiempo_espera} minutos")

def mostrar_visitantes(visitantes):
    for visitante in visitantes:
        print(f"Visitante: {visitante.nombre}, Edad: {visitante.edad}, Altura: {visitante.altura} cm")

def mostrar_reservas(reserva):
    print("Atracciones reservadas:")
    mostrar_atracciones(reserva.atracciones)
    print("\nVisitantes:")
    mostrar_visitantes(reserva.visitantes)

def realizar_reserva(atraccion, visitante, reserva):
    # Verificar si el visitante cumple con las restricciones de la atracción
    if visitante.edad < 18 and atraccion.nombre == "AtraccionSoloAdultos":
        print("Lo siento, esta atracción es solo para adultos.")
        return

    if visitante.altura < 120 and atraccion.nombre == "AtraccionAlturaMinima":
        print("Lo siento, el visitante no cumple con la altura mínima requerida.")
        return

    # Verificar si la atracción tiene espacio disponible
    if len(atraccion.visitantes_en_espera) < atraccion.capacidad_maxima:
        atraccion.visitantes_en_espera.append(visitante)
        reserva.atracciones.append(atraccion)
        reserva.visitantes.append(visitante)
        print(f"{visitante.nombre} ha realizado una reserva en {atraccion.nombre}.")
    else:
        print(f"Lo siento, {atraccion.nombre} está lleno. {visitante.nombre} se ha añadido a la cola de espera.")



def manejar_capacidad(atraccion, reserva):
    if len(atraccion.visitantes_en_espera) > 0:
        visitante_siguiente = atraccion.visitantes_en_espera.pop(0)
        reserva.visitantes.append(visitante_siguiente)
        print(f"{visitante_siguiente.nombre} ha ingresado a {atraccion.nombre} desde la cola de espera.")

def simular_paso_del_tiempo(atracciones, reserva):
    for atraccion in atracciones:
        if len(atraccion.visitantes_en_espera) > 0:
            atraccion.tiempo_espera -= 1
            if atraccion.tiempo_espera == 0:
                manejar_capacidad(atraccion, reserva)

    # Mostrar actualización de estado después de cada ciclo
    print("\n--- Actualización de Estado ---")
    print("Atracciones:")
    mostrar_atracciones(atracciones)
    print("\nCola de Espera:")
    mostrar_visitantes_en_espera(atracciones)

def mostrar_visitantes_en_espera(atracciones):
    for atraccion in atracciones:
        if len(atraccion.visitantes_en_espera) > 0:
            print(f"En espera para {atraccion.nombre}: {', '.join([v.nombre for v in atraccion.visitantes_en_espera])}")





def modificar_atraccion(atracciones):
    nombre = input("Ingrese el nombre de la atracción que desea modificar: ")
    atraccion = next((a for a in atracciones if a.nombre == nombre), None)

    if atraccion is not None:
        nueva_capacidad = input("Ingrese la nueva capacidad máxima: ")
        nueva_tiempo_espera = input("Ingrese el nuevo tiempo de espera (en minutos): ")

        if nueva_capacidad.isdigit():
            atraccion.capacidad_maxima = int(nueva_capacidad)
        else:
            print("La capacidad ingresada no es un número válido. No se ha modificado.")

        if nueva_tiempo_espera.isdigit():
            atraccion.tiempo_espera = int(nueva_tiempo_espera)
        else:
            print("El tiempo de espera ingresado no es un número válido. No se ha modificado.")
    else:
        print("Atracción no encontrada.")

def modificar_visitante(visitantes):
    nombre = input("Ingrese el nombre del visitante que desea modificar: ")
    visitante = next((v for v in visitantes if v.nombre == nombre), None)

    if visitante is not None:
        nueva_edad = input("Ingrese la nueva edad: ")
        nueva_altura = input("Ingrese la nueva altura (en cm): ")

        if nueva_edad.isdigit():
            visitante.edad = int(nueva_edad)
        else:
            print("La edad ingresada no es un número válido. No se ha modificado.")

        if nueva_altura.isdigit():
            visitante.altura = int(nueva_altura)
        else:
            print("La altura ingresada no es un número válido. No se ha modificado.")
    else:
        print("Visitante no encontrado.")

# Código principal
# Código principal
atracciones = []
visitantes = []
reserva = Reserva()

while True:
    print("\n1. Ingresar Atracción")
    print("2. Ingresar Visitante")
    print("3. Mostrar Atracciones")
    print("4. Mostrar Visitantes")
    print("5. Mostrar Reservas")
    print("6. Realizar Reserva")
    print("7. Modificar Atracción")
    print("8. Modificar Visitante")
    print("9. Simular Paso del Tiempo")
    print("10. Salir")

    try:
        opcion = int(input("\nSelecciona una opción: "))
    except ValueError:
        print("Por favor, ingresa un número válido para la opción.")
        continue

    if opcion == 1:
        atraccion = ingresar_atraccion()
        atracciones.append(atraccion)
    elif opcion == 2:
        visitante = ingresar_visitante()
        visitantes.append(visitante)
    elif opcion == 3:
        mostrar_atracciones(atracciones)
    elif opcion == 4:
        mostrar_visitantes(visitantes)
    elif opcion == 5:
        mostrar_reservas(reserva)
    elif opcion == 6:
        atraccion_nombre = input("Nombre de la atracción para reservar: ")
        visitante_nombre = input("Nombre del visitante que realiza la reserva: ")
        atraccion = next((a for a in atracciones if a.nombre == atraccion_nombre), None)
        visitante = next((v for v in visitantes if v.nombre == visitante_nombre), None)

        if atraccion is not None and visitante is not None:
            realizar_reserva(atraccion, visitante, reserva)
        else:
            print("Atracción o visitante no encontrados.")
    elif opcion == 7:
        modificar_atraccion(atracciones)
    elif opcion == 8:
        modificar_visitante(visitantes)
    elif opcion == 9:
        simular_paso_del_tiempo(atracciones, reserva)
    elif opcion == 10:
        break
    else:
        print("Opción no válida. Inténtalo de nuevo.")
