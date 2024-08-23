

class Aritmetica:
    """
    Clase aritmetica para realizar las operaciones básicas
    """
    def __init__(self, operandoA, operandoB):
        self.operandoA = operandoA
        self.operandoB = operandoB
    
    def sumar(self):
        return self.operandoA + self.operandoB
    def restar(self):
        return self.operandoA - self.operandoB
    def multiplicar(self):
        return self.operandoA * self.operandoB
    def dividir(self):
        return self.operandoA / self.operandoB

Aritmetica1 = Aritmetica(5,3)

print(f"La suma de los números es {Aritmetica1.sumar()}")
print(f"La resta de los números es {Aritmetica1.restar()}")
print(f"La multiplicación de los números es {Aritmetica1.multiplicar()}")
print(f"La división de los números es {Aritmetica1.dividir():.2f}")