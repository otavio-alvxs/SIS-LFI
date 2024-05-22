class Caneta:
    def __init__(self, modelo, cor, ponta, carga, tampada):
        self.modelo = modelo
        self.cor = cor
        self.__ponta = ponta
        self.carga = carga
        self.tampada = tampada

    def rabiscar(self):
        if self.tampada is True:
            print ('Error ! Não é possível rabiscar, a caneta está tampada!')
        else:
            print ('<<< Estou rabiscando >>>')

    def tampar(self):
        self.tampada = True
    
    def destampar(self):
        self.tampada = False

    def __str__(self) -> str:
        print ('-=' * 15)
        return f'Modelo: {self.modelo}\nTampada: {self.tampada}'
    
    def Getponta(self):
        return f'Ponta: {self.__ponta}'
    
    def Setponta(self, p):
        self.__ponta = p