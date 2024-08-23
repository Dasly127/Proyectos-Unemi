class Materia:
    def __init__(self, nombre):
        self.nombre = nombre
        self.calificaciones = []

    def agregar_calificacion(self, calificacion):
        if 0 <= calificacion <= 100:
            self.calificaciones.append(calificacion)
        else:
            raise ValueError("La calificación debe estar entre 0 y 100")

    def calcular_promedio(self):
        if not self.calificaciones:
            return 0
        return sum(self.calificaciones) / len(self.calificaciones)

if __name__ == "__main__":
    # Ejemplo de uso
    materia = Materia("Matemáticas")
    materia.agregar_calificacion(80)
    materia.agregar_calificacion(90)
    materia.agregar_calificacion(70)

    promedio = materia.calcular_promedio()
    print(f"El promedio de la materia {materia.nombre} es {promedio:.2f}")
