# Constructores

class Persona():
    def __init__(self, nombre, año):
        self.nombre = nombre  # Utiliza el parámetro nombre en lugar de Lalo
        self.año = año        # Utiliza el parámetro año en lugar de 25

    def descripcción(self):
        return "{} tiene {}".format(self.nombre, self.año)

    def comentario(self, frase):
        return "{} dice: {}".format(self.nombre, frase)

# Debes pasar dos argumentos al instanciar Persona, nombre y año
doctor = Persona("Lalo", 25)

# Llama al método descripcción y muestra el resultado
print(doctor.descripcción())
print(doctor.comentario("Hola que tal"))