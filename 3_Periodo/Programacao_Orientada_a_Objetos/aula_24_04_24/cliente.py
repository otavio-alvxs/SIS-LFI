class Cliente:
    lista_planos = ["basic", "premium"]
    def __init__(self, nome, email, plano) -> None:
        self.nome = nome
        self.email = email
        if plano in self.lista_planos:
            self.plano = plano
        else:
            raise Exception("Plano inválido!!!")

    def mudar_plano(self, novo_plano):
        if novo_plano in self.lista_planos:
            print(f"Plano alterado de {self.plano} para {novo_plano}")
            self.plano = novo_plano
        else:
            print ("Plano inválido!!!")

    def ver_filme(self, filme, plano_filme):
        if self.plano == plano_filme:
            print (f"Ver filme {filme}")
        elif self.plano == "premium":
            print (f"Ver filme {filme}")
        elif self.plano == "basic" and plano_filme == "premium":
            print ("Faça um upgrade para premium para ver esse filme")
        else:
            print ("Plano inválido!!!")
            

cliente = Cliente("Juliano", "juliano.silva@libertas.edu.br", "premium")
print (f"Nome: {cliente.nome}")
print (f"Plano: {cliente.plano}")
cliente.mudar_plano("basic")
print (f"Nome: {cliente.nome}")
print (f"Plano: {cliente.plano}")
cliente.ver_filme("Harry Potter", "premium")
cliente.mudar_plano("premium")
print (f"Nome: {cliente.nome}")
print (f"Plano: {cliente.plano}")
cliente.ver_filme("Harry Potter", "premium")
