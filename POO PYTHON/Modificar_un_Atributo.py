# Modificar un atributo

class Email:
    def __init__(self):
        self.enviado = False
    
    def enviar_correo(self):
        self.enviado = True  # Cambiado de ENVIADO a enviado

# Crear una instancia de la clase Email
mi_correo = Email()

# Llamar al método enviar_correo para cambiar el estado a enviado
mi_correo.enviar_correo()

# Imprimir el estado actual del atributo enviado
print(mi_correo.enviado)  # Cambiado de eviado a enviado
