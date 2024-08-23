
class Materia:
    """
    Clase que representa una materia.

    Atributos:
    - nombre (str): Nombre de la materia.
    - calificaciones (list): Lista de calificaciones de la materia.
    """

    def __init__(self, nombre):
        """
        Inicializa una nueva instancia de la clase Materia.

        Parámetros:
        - nombre (str): Nombre de la materia.
        """
        self.nombre = nombre
        self.calificaciones = []

    def añadir_calificacion(self, calificacion):
        """
        Añade una calificación a la lista de calificaciones de la materia.

        Parámetros:
        - calificacion (float): Calificación a añadir, debe estar en el rango de 0 a 100.

        Lanza:
        - ValueError: Si la calificación no está en el rango de 0 a 100.
        """
        if 0 <= calificacion <= 100:
            self.calificaciones.append(calificacion)
        else:
            raise ValueError("La calificación debe estar en el rango de 0 a 100.")

    def calcular_promedio(self):
        """
        Calcula el promedio de las calificaciones de la materia.

        Retorno:
        - float: Promedio de las calificaciones. Si no hay calificaciones, retorna 0.
        """
        if not self.calificaciones:
            return 0
        return sum(self.calificaciones) / len(self.calificaciones)


class Estudiante:
    """
    Clase que representa a un estudiante.

    Atributos:
    - cedula (str): Cédula del estudiante.
    - nombre (str): Nombre del estudiante.
    - apellido (str): Apellido del estudiante.
    - materias (list): Lista de materias en las que está inscrito el estudiante.
    """

    def __init__(self, cedula, nombre, apellido):
        """
        Inicializa una nueva instancia de la clase Estudiante.

        Parámetros:
        - cedula (str): Cédula del estudiante.
        - nombre (str): Nombre del estudiante.
        - apellido (str): Apellido del estudiante.
        """
        self.cedula = cedula
        self.nombre = nombre
        self.apellido = apellido
        self.materias = []

    def añadir_materia(self, materia):
        """
        Añade una materia a la lista de materias del estudiante.

        Parámetros:
        - materia (Materia): Instancia de la clase Materia a añadir.
        """
        self.materias.append(materia)

    def buscar_materia(self, nombre_materia):
        """
        Busca una materia en la lista de materias del estudiante por su nombre.

        Parámetros:
        - nombre_materia (str): Nombre de la materia a buscar.

        Retorno:
        - Materia: Instancia de la clase Materia si se encuentra, de lo contrario None.
        """
        for materia in self.materias:
            if materia.nombre == nombre_materia:
                return materia
        return None

    def calcular_promedio_general(self):
        """
        Calcula el promedio general de todas las materias del estudiante.

        Retorno:
        - float: Promedio general del estudiante. Si no hay materias, retorna 0.
        """
        if not self.materias:
            return 0
        total_promedio = sum(materia.calcular_promedio() for materia in self.materias)
        return total_promedio / len(self.materias)


def mostrar_menu():
    """
    Muestra el menú de opciones del sistema.
    """
    print("\n--- Sistema de Gestión Académica ---")
    print("1. Añadir un nuevo estudiante")
    print("2. Inscribir materias a un estudiante")
    print("3. Registrar calificaciones para las materias de un estudiante")
    print("4. Mostrar el promedio de calificaciones por materia de un estudiante")
    print("5. Mostrar el promedio general del estudiante")
    print("6. Salir")


def validar_entrada(mensaje, tipo):
    """
    Valida la entrada del usuario.

    Parámetros:
    - mensaje (str): Mensaje a mostrar al usuario.
    - tipo (type): Tipo de dato esperado (int, float, str).

    Retorno:
    - int, float, str: Entrada validada del usuario.
    """
    while True:
        entrada = input(mensaje)
        try:
            if tipo == int:
                return int(entrada)
            elif tipo == float:
                return float(entrada)
            else:
                return entrada
        except ValueError:
            print(f"Entrada inválida. Por favor, ingrese un valor {tipo.__name__}.")


def añadir_estudiante(estudiantes):
    """
    Añade un nuevo estudiante a la lista de estudiantes.

    Parámetros:
    - estudiantes (list): Lista de estudiantes.
    """
    cedula = validar_entrada("Ingrese la cédula del estudiante: ", str)
    nombre = validar_entrada("Ingrese el nombre del estudiante: ", str)
    apellido = validar_entrada("Ingrese el apellido del estudiante: ", str)
    estudiante = Estudiante(cedula, nombre, apellido)
    estudiantes.append(estudiante)
    print(f"Estudiante {nombre} {apellido} añadido exitosamente.")


def inscribir_materia(estudiantes):
    """
    Inscribe una materia a un estudiante.

    Parámetros:
    - estudiantes (list): Lista de estudiantes.
    """
    cedula = validar_entrada("Ingrese la cédula del estudiante: ", str)
    estudiante = buscar_estudiante(estudiantes, cedula)
    if estudiante:
        nombre_materia = validar_entrada("Ingrese el nombre de la materia: ", str)
        materia = Materia(nombre_materia)
        estudiante.añadir_materia(materia)
        print(f"Materia {nombre_materia} inscrita exitosamente.")
    else:
        print("Estudiante no encontrado.")


def registrar_calificaciones(estudiantes):
    """
    Registra calificaciones para las materias de un estudiante.

    Parámetros:
    - estudiantes (list): Lista de estudiantes.
    """
    cedula = validar_entrada("Ingrese la cédula del estudiante: ", str)
    estudiante = buscar_estudiante(estudiantes, cedula)
    if estudiante:
        nombre_materia = validar_entrada("Ingrese el nombre de la materia: ", str)
        materia = estudiante.buscar_materia(nombre_materia)
        if materia:
            while True:
                try:
                    calificacion = validar_entrada("Ingrese la calificación (0-100, -1 para terminar): ", float)
                    if calificacion == -1:
                        break
                    materia.añadir_calificacion(calificacion)
                except ValueError as e:
                    print(e)
        else:
            print("Materia no encontrada.")
    else:
        print("Estudiante no encontrado.")


def mostrar_promedio_materia(estudiantes):
    """
    Muestra el promedio de calificaciones por materia de un estudiante.

    Parámetros:
    - estudiantes (list): Lista de estudiantes.
    """
    cedula = validar_entrada("Ingrese la cédula del estudiante: ", str)
    estudiante = buscar_estudiante(estudiantes, cedula)
    if estudiante:
        nombre_materia = validar_entrada("Ingrese el nombre de la materia: ", str)
        materia = estudiante.buscar_materia(nombre_materia)
        if materia:
            promedio = materia.calcular_promedio()
            print(f"El promedio de la materia {nombre_materia} es {promedio:.2f}.")
        else:
            print("Materia no encontrada.")
    else:
        print("Estudiante no encontrado.")


def mostrar_promedio_general(estudiantes):
    """
    Muestra el promedio general del estudiante.

    Parámetros:
    - estudiantes (list): Lista de estudiantes.
    """
    cedula = validar_entrada("Ingrese la cédula del estudiante: ", str)
    estudiante = buscar_estudiante(estudiantes, cedula)
    if estudiante:
        promedio_general = estudiante.calcular_promedio_general()
        print(f"El promedio general del estudiante {estudiante.nombre} {estudiante.apellido} es {promedio_general:.2f}.")
    else:
        print("Estudiante no encontrado.")


def buscar_estudiante(estudiantes, cedula):
    """
    Busca un estudiante en la lista por su cédula.

    Parámetros:
    - estudiantes (list): Lista de estudiantes.
    - cedula (str): Cédula del estudiante a buscar.

    Retorno:
    - Estudiante: Instancia de la clase Estudiante si se encuentra, de lo contrario None.
    """
    for estudiante in estudiantes:
        if estudiante.cedula == cedula:
            return estudiante
    return None


def main():
    """
    Función principal del sistema de gestión académica. Ejecuta el menú y maneja las opciones seleccionadas.
    """
    estudiantes = []
    while True:
        mostrar_menu()
        opcion = validar_entrada("Seleccione una opción: ", str)
        if opcion == "1":
            añadir_estudiante(estudiantes)
        elif opcion == "2":
            inscribir_materia(estudiantes)
        elif opcion == "3":
            registrar_calificaciones(estudiantes)
        elif opcion == "4":
            mostrar_promedio_materia(estudiantes)
        elif opcion == "5":
            mostrar_promedio_general(estudiantes)
        elif opcion == "6":
            print("Saliendo del sistema.")
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")


if __name__ == "__main__":
    main()


