opcao = 1
bd_estoque = []  # bd -> banco de dados

while opcao != 4:
    print('=' * 10)
    print("1- Adicionar")
    print('2- Consultar estoque')
    print('3- Consultar Valor Total do Estoque')
    print('4- Sair')
    opcao = int(input('Opcao >>>> '))
    
    if opcao == 1:
        print('-----Adicionar produto-----')
        codigo = int(input('Codigo: '))
        nome = input('Nome: ')
        descricao = input('Descricao: ')
        preco = float(input('Preco: R$ '))
        quantidade = int(input('Quantidade: '))
        
        # Adicionar a quantidade do produto no estoque
        produto = [codigo, nome, descricao, preco, quantidade]
        bd_estoque.append(produto)  # Adicionar produto na lista estoque
        print('-----Adicionado com sucesso-----')
    
    elif opcao == 2:
        print('-----Estoque-----')
        # Percorrer o bd
        print('Codigo\tNome\tDescricao\tPreco\tQuantidade')
        for prod in bd_estoque:
            print(prod[0], end='\t')  # \t tab
            print(prod[1], end='\t')
            print(prod[2], end='\t')
            print(prod[3], end='\t')
            print(prod[4])
        print('-----Fim estoque-----')
    
    elif opcao == 3:
        # Consultar Valor Total do Estoque
        total_estoque = 0
        for prod in bd_estoque:
            total_estoque += prod[4] * prod[3]  # quantidade * preco
        print(f'Valor Total do Estoque: R$ {total_estoque:.2f}')
    
    elif opcao == 4:
        print('Saindo....')
    
    else:
        print('Opcao incorreta')
