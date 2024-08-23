class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self) -> str:
        return f"Persona: {self.nombre}, Edad: {self.edad}"
    
class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)  # Se pasan los parámetros a la clase base
        self.sueldo = sueldo

    def __str__(self) -> str:
        return f"Empleado: {self.nombre}, Edad: {self.edad}, Sueldo: {self.sueldo}"

# Crear y mostrar detalles de un Empleado
empleado1 = Empleado("Juan", 30, 5000)
print(empleado1)


"""
Explicación
Inicialización Correcta de Persona:

Cuando creas la instancia de Persona, debes pasar dos argumentos separados: "Juan" y 28.
Método __str__:

En la clase Persona, el método __str__ devuelve una representación legible del objeto.
En la clase Empleado, el método __str__ también incluye el atributo sueldo.
Herencia en la Clase Empleado:

Empleado hereda de Persona, y su constructor usa super().__init__(nombre, edad) para inicializar los atributos heredados.
El método __str__ en Empleado llama a la versión de la clase base y añade información adicional específica de Empleado.

"""