class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
    
    def mostra_info(self):
        print (f"""Nome: {self.nome}
Preco: {self.preco}
Quantidade: {self.quantidade}
""")

    def mostra_valor_total_estoque(self):
        valor_total = self.preco * self.quantidade
        print (f"O valor total de estoque deste produto é R${valor_total:.2f}.")


class ProdutoPerecivel(Produto):
    def __init__(self, nome, preco, quantidade, datavalidade):
        super().__init__(nome, preco, quantidade)
        self.datavalidade = datavalidade

    def mostrar_validade(self):
        print (f"O produto vence no dia {self.datavalidade}")

    def mostra_info(self):
        super().mostra_info()
        print ("Este produto É perecível")
        print ("")

p1 = Produto ("Àgua", 1.99, 200)
p2 = Produto ("Refrigerante", 4.99, 25)
p3 = ProdutoPerecivel ("Leite", 7.99, 10, "10/05/2024")
p4 = ProdutoPerecivel ("Maçã", 0.99, 15, "05/05/2024")

# p1.mostra_info()
# p1.mostra_valor_total_estoque()
# p2.mostra_info()
# p2.mostra_valor_total_estoque()
# p3.mostra_info()
# p3.mostra_valor_total_estoque()
# p3.mostrar_validade()
# p4.mostra_info()
# p4.mostra_valor_total_estoque()
# p4.mostrar_validade()

carrinho_produtos = {
    Produto ("Àgua", 1.99, 200),
    Produto ("Refrigerante", 4.99, 25),
    ProdutoPerecivel ("Leite", 7.99, 10, "10/05/2024"),
    ProdutoPerecivel ("Maçã", 0.99, 15, "05/05/2024"),
}

for i in carrinho_produtos:
    i.mostra_info()
