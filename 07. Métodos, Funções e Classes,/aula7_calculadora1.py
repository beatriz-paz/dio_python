    # DECLARANDO UM MÉTADO - DEF

class Calculadora: # CLASSE
    def __init__(self, num1, num2):
        self.valor_a = num1
        self.valor_b = num2
    def soma(self):
        return self.valor_a + self.valor_b

    def subtracao(self):
        return self.valor_a - self.valor_b

    def multiplicacao(self):
        return self.valor_a * self.valor_b

    def divisao(self):
        return self.valor_a / self.valor_b

calculadora = Calculadora(10, 2)
print(calculadora.valor_a)
print(calculadora.subtracao())
print(calculadora.divisao())
print(calculadora.multiplicacao())
