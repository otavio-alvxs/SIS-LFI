class Cliente:
    def __init__(self, nome, cpf, idade, rg) -> None:
        self.nome = nome
        self.cpf = cpf
        self.idade = idade
        self.rg = rg

    def mostrar_dados(self):
        print(f"Nome: {self.nome} \nCPF: {self.cpf} \nIdade: {self.idade} \nRG: {self.rg}")
