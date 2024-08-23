

class Vehiculo:
    def __init__(self, color, ruedas) -> None:
        self.color = color 
        self.ruedas = ruedas 

class coche(Vehiculo):
    def __init__(self, color, ruedas) -> None:
        super().__init__(color, ruedas)
    def mostrar_Especs():
        return print(f"El color del coche es {ColorCoche}")
    pass

class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas) -> None:
        super().__init__(color, ruedas)