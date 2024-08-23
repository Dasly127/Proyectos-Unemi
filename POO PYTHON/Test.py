class Coche:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.velocidad = 0
    
    def acelerar(self, velocidad):
        self.velocidad += velocidad
    
    def frenar(self, velocidad):
        self.velocidad -= velocidad