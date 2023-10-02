import json 

#função que adiciona ou atualiza dados no json.
def atualizarbanco(): 
    with open('estoque.json', 'w') as arquivo:
                    json.dump(bancodados, arquivo, indent=4)

bancodados = {}

try:
    with open('estoque.json', 'r') as arquivo:
        bancodados = json.load(arquivo)

except:
    print('O Arquivo não existe.')

opcao = 9

opcoes = {
    1: 'Adicionar',
    2: 'Consultar por Código',
    3: 'Consultar Todos',
    4: 'Excluir Itens',
    5: 'Alterar Preço',
    6: 'Aplicar Acréscimos e Descontos',
    0: 'Sair'
}

while opcao != 7:  # Você estava usando 7 como saída, então mantive essa lógica.
    print('=' * 35)
    for numero, descricao in opcoes.items():
        print(f'{numero} - {descricao}')
    print('=' * 35)
    opcao = int(input('Escolha a opção: '))

    if opcao not in opcoes:
        print('Opção inválida')

    if opcao ==1:
        print('=' * 12)
        print('= CADASTRO =')
        print('=' * 12)

        codigo = input('Código do produto : ').lower()
    
        if codigo in bancodados.keys():
            print ('O CÓDIGO DIGITADO JÁ ESTÁ CADASTRADO.')
        else:        
            nome = input('Digite o nome do produto : ')
            preco = float(input('Digite o preco do kg/unidade : '))
            bancodados[codigo] = {'NOME': nome,'PRECO': preco}
            
            atualizarbanco()

            print ('=' * 34)
            print ('= PRODUTO CADASTRADO COM SUCESSO =')
            print ('=' * 34)

    elif opcao ==2:
        print ('=' * 24)
        print ('= CONSULTAR POR CÓDIGO =')
        print ('=' * 24)
        cod = input('Digite o numero do código : ').lower()
        print('=' * 35)
        if cod in bancodados.keys():
            print ('CÓDIGO EXISTE')
            print ('-' * 35)
            produto = bancodados[cod]
            print (produto['NOME'])
            print ('-' * 35)
            print (produto['PRECO'])
        else:
            print ('Código Inexistente')

    elif opcao ==3:
        print ('=' * 19)
        print ('= CONSULTAR TODOS =')
        print ('=' * 19)
        print ("Produtos cadastrados :")
        for codigo in bancodados.values():
            print ('-' * 20)
            print (codigo['NOME'])
            print (codigo['PRECO'])
        print ('=' * 20) 

    elif opcao ==4:
        print ('=' * 20)
        print ('EXCLUIR ITEM')
        print ('=' * 20)
        delete = input('Digite o Código do produto : ').lower()
        # ve se existe essa chave no banco de dados antes de remover
        if delete in bancodados:
            del bancodados[delete]
            print ('=' * 35)
            print (f"Item {delete} removido com sucesso.")
            print ('=' * 35)
        else:
            print('=' * 35)
            print(f"Item {delete} não encontrado no estoque.")
            print('=' * 35)
        atualizarbanco()

    elif opcao == 5:
        print ('=' * 17)
        print ('= ALTERAR PREÇO =')
        print ('=' * 17)
        print('Deseja alterar o preco de qual item? ')
        print('-' * 35)
        alterar_preco = input('Digite o código do produto : ').lower()
        print('-' * 35)
        novo_preco = float(input('Digite o novo preco : '))
        print('-' * 35)
        if alterar_preco in bancodados:
            bancodados[alterar_preco]["PRECO"] = novo_preco
            print('Preço alterado com Sucessso')  
            atualizarbanco()
        else:
            print('CÓDIGO INEXISTENTE')
    elif opcao ==6:
        print('=' * 35)
        print('= APLICAR DESCONTOS OU ACRESCIMOS =')
        print('=' * 35)
        print('Deseja aplicar um acrescimo ou um desconto nos produtos? 1/2')
        print(' ')
        print('1 - Aplicar Acrescimos')
        print('-' * 35)
        print('2 - Aplicar Descontos')
        print('=' * 35)
        resp = int(input('Opção selecionada : '))
        print('=' * 35)
        if resp == 1:
            print('Deseja Aplicar Acrescimo em TODOS os produtos ou somente um? 1/2')
            print('-' * 35)
            print('1 - Somente em um')
            print('-' * 35)
            print('2 - TODOS')
            print('-' * 35)
            resp_opcao = int(input('Opção selecionada : '))
            print('=' * 35)
            
            if resp_opcao == 1:
                app_acre = input('Digite o código do produto : ').lower()
                print('-' * 35)
                acrescimo = float(input('Digite qual a porcentagem do acréscimo : '))
                if app_acre in bancodados:
                    acrescimo1 = (acrescimo / 100) * bancodados[app_acre]['PRECO']
                    novo_valor = bancodados[app_acre]['PRECO'] + acrescimo1
                    bancodados[app_acre]['PRECO'] = novo_valor
                    print('PREÇO ALTERADO COM SUCESSO')
                    atualizarbanco()
                else:
                    print("CÓDIGO INEXISTENTE")
            elif resp_opcao == 2:
                acrescimo = float(input('Digite qual a porcentagem do acrescimo : '))
                print('-' * 35)
                for produto_id, produto_info in bancodados.items():
                    if "PRECO" in produto_info:
                        preco_atual = produto_info["PRECO"]
                        novo_preco = round(preco_atual * (1 + acrescimo / 100), 2)
                        produto_info["PRECO"] = novo_preco
                        print('PRECO AJUSTADO COM SUCESSO')
                atualizarbanco()
            else:
                print("OPÇÃO INVALIDA")
        
        elif resp == 2:
            print('Deseja Aplicar Desconto em TODOS os produtos ou somente um? 1/2')
            print('-' * 35)
            print('1 - Somente em um')
            print('-' * 35)
            print('2 - TODOS')
            print('-' * 35)
            resp_opcao1 = int(input('Opção selecionada : '))
            print('=' * 35)

            if resp_opcao1 == 1:
                print('=' * 35)
                app_desc = input('Digite o código do item desejado : ').lower()
                print('-' * 35)
                desconto = float(input('Digite qual a porcentagem de desconto : '))
                print('-' * 35)
                if app_desc in bancodados:
                    desconto1 = (desconto / 100) * bancodados[app_desc]['PRECO']
                    descontado =  bancodados[app_desc]['PRECO'] - desconto1
                    bancodados[app_desc]['PRECO'] = descontado
                    print("PREÇO AJUSTADO COM SUCESSO")
                atualizarbanco()

            elif resp_opcao1 == 2:
                desconto = float(input('Digite qual a porcentagem do desconto : '))
                print('-' * 35)
                for produto_id, produto_info in bancodados.items():
                    if "PRECO" in produto_info:
                        preco_atual = produto_info["PRECO"]
                        novo_preco = round(preco_atual * (desconto / 100)) 
                        novo_preco1 = preco_atual - novo_preco
                        produto_info["PRECO"] = novo_preco1
                        print("PREÇO AJUSTADO COM SUCESSO")
                atualizarbanco()
            else:
                print('OPCAO INVÁLIDA')
    elif opcao ==0:
        print('=' * 20)
        print('SAIR')
        break
    else:
        print('OPCAO INVÁLIDA')
