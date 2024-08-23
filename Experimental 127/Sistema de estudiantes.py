


class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.materias = {}

    def inscribir_materia(self, materia):
        if materia not in self.materias:
            self.materias[materia] = []

    def registrar_calificacion(self, materia, calificacion):
        if materia in self.materias:
            if 0 <= calificacion <= 100:
                self.materias[materia].append(calificacion)
            else:
                print("Calificación fuera de rango. Debe estar entre 0 y 100.")
        else:
            print(f"La materia {materia} no está inscrita.")

    def calcular_promedio(self, materia):
        if materia in self.materias:
            calificaciones = self.materias[materia]
            if calificaciones:
                return sum(calificaciones) / len(calificaciones)
            else:
                return 0
        else:
            print(f"La materia {materia} no está inscrita.")
            return None

class Sistema:
    def __init__(self):
        self.estudiantes = []

    def añadir_estudiante(self, nombre):
        estudiante = Estudiante(nombre)
        self.estudiantes.append(estudiante)

    def encontrar_estudiante(self, nombre):
        for estudiante in self.estudiantes:
            if estudiante.nombre == nombre:
                return estudiante
        return None

    def inscribir_materia(self, nombre_estudiante, materia):
        estudiante = self.encontrar_estudiante(nombre_estudiante)
        if estudiante:
            estudiante.inscribir_materia(materia)
        else:
            print(f"Estudiante {nombre_estudiante} no encontrado.")

    def registrar_calificacion(self, nombre_estudiante, materia, calificacion):
        estudiante = self.encontrar_estudiante(nombre_estudiante)
        if estudiante:
            estudiante.registrar_calificacion(materia, calificacion)
        else:
            print(f"Estudiante {nombre_estudiante} no encontrado.")

    def mostrar_promedio(self, nombre_estudiante, materia):
        estudiante = self.encontrar_estudiante(nombre_estudiante)
        if estudiante:
            promedio = estudiante.calcular_promedio(materia)
            if promedio is not None:
                print(f"El promedio de {materia} para {nombre_estudiante} es {promedio:.2f}")

    def mostrar_menu(self):
        while True:
            print("\nMenú de Opciones:")
            print("1. Añadir un nuevo estudiante al sistema")
            print("2. Inscribir materias a un estudiante específico")
            print("3. Registrar calificaciones para las materias de un estudiante")
            print("4. Mostrar el promedio de calificaciones por materia de un estudiante")
            print("5. Salir del programa")
            opcion = input("Seleccione una opción: ")

            if opcion == '1':
                nombre = input("Ingrese el nombre del estudiante: ")
                self.añadir_estudiante(nombre)
            elif opcion == '2':
                nombre = input("Ingrese el nombre del estudiante: ")
                materia = input("Ingrese la materia a inscribir: ")
                self.inscribir_materia(nombre, materia)
            elif opcion == '3':
                nombre = input("Ingrese el nombre del estudiante: ")
                materia = input("Ingrese la materia: ")
                calificacion = float(input("Ingrese la calificación: "))
                self.registrar_calificacion(nombre, materia, calificacion)
            elif opcion == '4':
                nombre = input("Ingrese el nombre del estudiante: ")
                materia = input("Ingrese la materia: ")
                self.mostrar_promedio(nombre, materia)
            elif opcion == '5':
                print("Saliendo del programa...")
                break
            else:
                print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    sistema = Sistema()
    sistema.mostrar_menu()
