opcao = 1
banco_de_dados_estoque = []
while opcao != 4:
    print("="*30)
    print("1-Adicionar")
    print("2-Consultar produto")
    print("3-Consltar valor total do estoque")
    print("4-Sair")
    opcao = int(input("Opcao >>>> "))
    if opcao == 1:
        print("....adicionar")
        codigo = int(input("codigo: "))
        nome = input("Nome: ")
        descricao = input("Descricao: ")
        preco = float(input("Preco: R$ "))
        produto = [codigo,nome,descricao,preco]
        banco_de_dados_estoque.append(produto)
        print("----Adicionar produto----")    
    elif opcao == 2:
        print("....mostrar estoque")
        print("Codigo\tNome\tDescricao\tPreco")
        for prod in banco_de_dados_estoque:
            print(prod[0],end="\t")
            print(prod[1],end="\t")
            print(prod[2],end="\t")
            print(prod[3])
    
    elif opcao == 4 :
        print("saindo.....")
    else:
        print("opcao invalida")
        