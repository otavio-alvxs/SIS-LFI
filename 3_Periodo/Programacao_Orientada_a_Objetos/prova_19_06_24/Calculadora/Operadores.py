class Operadores:
    def __init__(self, valor01, valor02):
        self.valor01 = valor01
        self.valor02 = valor02
    
    def soma(self):
        total = self.valor01 + self.valor02
        return total
    
    def subtracao(self):
        total = self.valor01 - self.valor02
        return total
    
    def multiplicacao(self):
        total = self.valor01 * self.valor02
        return total
    
    def divisao(self):
        total = self.valor01 / self.valor02
        return total
