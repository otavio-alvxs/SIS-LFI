from math import log

def conversortaxa():
    taxa = input('A taxa será aplicada a.m. , a.a. ou a.d (M para mês) (A para ano) (D para dia) ? ')
    if taxa.lower() == 'm':
        taxa = (float(input('Taxa (em %): '))) / 100
    elif taxa.lower() == 'a':
        taxa = (float(input('Taxa (em %): ')) / 100) * 12
    elif taxa.lower() == 'd':
        taxa = (float(input('Taxa (em %): ')) / 100) / 30
    return taxa

def conversortempo():
    tempo = input('O tempo será medido em meses anos ou dias? (M para meses) (A para anos) (D para dias) ? ')
    if tempo.lower() == 'm':
        tempo = float(input('Tempo da aplicação: '))
    elif tempo.lower() == 'a':
        tempo = (float(input('Tempo da aplicação: '))) * 12
    elif tempo.lower() == 'd':
        tempo = (float(input('Tempo da aplicação: '))) / 30
    return tempo

while True:
    print ('ATENÇÃO')
    print ('SEPARE CASAS DECIMAIS APENAS COM .(PONTO).')
    print ('Selecione uma das opções:')

    opcao = 0
    while opcao != 1 or opcao != 2 or opcao != 3:
        print ('(1) Juros simples.')
        print ('(2) Juros compostos.')
        print ('(3) Desconto simples.')

        opcao = int(input('Opção selecionada: '))
        if opcao != 1 or opcao != 2 or opcao != 3:
            print('Opção inválida, digite 1, 2 ou 3')
    

        if opcao == 1:
                opcao = 0
                while opcao != 1 or opcao != 2 or opcao != 3 or opcao != 4 or opcao != 5:
                    print ('Opções: ')

                    print ('(1) Capital inicial.')
                    print ('(2) Juros simples.')
                    print ('(3) Tempo da aplicação.')
                    print ('(4) Taxa de juros.')
                    print ('(5) Montante.')
                    
                    opcao = int(input('O que deseja calcular ? '))
                    if opcao != 1 or opcao != 2 or opcao != 3 or opcao != 4 or opcao != 5:
                        print('Opção inválida, digite 1, 2, 3, 4 ou 5.')

                    elif opcao == 1:
                        print ('Dados necessários: Juros simples, Tempo e Taxa de juros.')

                        juros = float(input('Juros simples: R$'))
                        taxa = conversortaxa()
                        tempo = conversortempo()
                        capital = (juros / (taxa * tempo))

                        print (f'O capital inicial é de : R${capital:.2f}')

                    elif opcao == 2:
                        opcao = int(input('Deseja utilizar: \n(1) Montante e Capital inicial. \n(2) Capital inicial, Taxa e Tempo. \nOpção selecionada: '))
                        if opcao == 1:
                            montante = float(input('Montante : R$'))
                            capital = float(input('Capital inicial : R$'))

                            juros = montante - capital

                            print (f'Os juros simples são R${juros:.2f}')
                        elif opcao == 2:
                            capital = float(input('Capital inicial : R$'))
                            taxa = conversortaxa()
                            tempo = conversortempo()
                            juros = (capital * taxa * tempo)

                            print (f'Os juros simples são de R${juros:.2f}')
                    
                    elif opcao == 3:
                        print ('Dados necessários: Capital inicial, Juros simples e Taxa.')
                        capital = float(input('Capital inicial : R$'))
                        juros = float(input('Juros simples : R$'))
                        taxa = conversortaxa()

                        tempo = (juros / (capital * taxa))

                        opcao = 0
                        while opcao != 'a' or opcao != 'm' or opcao != 'd':
                            opcao = input ('Deseja saber o tempo em anos, meses ou dias (A para anos) (M para meses) (D para dias)?')
                            if opcao.lower() == 'a':
                                print (f'O tempo de aplicação é de {(tempo / 12):.2f} anos.')
                            elif opcao.lower() == 'm':
                                print (f'O tempo de aplicação é de {tempo:.2f} meses.')
                            elif opcao.lower() == 'd':
                                print (print (f'O tempo de aplicação é de {tempo:.2f * 30} dias.'))
                        
                    elif opcao == 4:
                        print ('Dados necessários: Capital inicial, Juros simples e Tempo da aplicação.')
                        capital = float(input('Capital inicial : R$'))
                        juros = float(input('Juros simples : R$'))
                        tempo = conversortempo()

                        taxa = ((juros / (capital * tempo)) * 100)

                        print (f'A taxa de juros é de {taxa:.2f}%')

                    elif opcao == 5:
                        print ('Dados necessários: Capital inicial e Juros simples.')
                        capital = float(input('Cpital inicial : R$'))
                        juros = float(input('Juros simples : R$'))

                        montante = capital + juros

                        print (f'O montante é R${montante:.2f}.')
                    
        elif opcao == 2:
                opcao = 0
                while opcao != 1 or opcao != 2 or opcao != 3 or opcao != 4 or opcao != 5:
                    print ('Opções')

                    print ('(1) Capital inicial.')
                    print ('(2) Juros compostos.')
                    print ('(3) Tempo da aplicação.')
                    print ('(4) Taxa de juros.')
                    print ('(5) Montante.')

                    opcao = int(input('O que deseja calcular ? '))
                    if opcao != 1 or opcao != 2 or opcao != 3 or opcao != 4 or opcao != 5:
                        print('Opção inválida, digite 1, 2, 3, 4 ou 5.')

                    elif opcao == 1:
                        print ('Dados necessárias : Montante, Taxa e Tempo de aplicação.')

                        montante = float(input('Montante : R$'))
                        taxa = conversortaxa()
                        tempo = conversortempo()

                        #C = M / ((1+i) ** t)
                        capital = (montante / ((1 + taxa) ** tempo))

                        print (f'O capital inicial é de R${capital:.2f}.')
                    
                    elif opcao == 2:

                        print ('Dados necessários: Capital inicial, Taxa e Tempo de aplicação.')

                        capital = float(input('Capital inicial : R$'))
                        taxa = conversortaxa()
                        tempo = conversortempo()

                        #M = (C * (1 + i) ** t)
                        montante = (capital * ((1 + taxa) ** tempo))
                        #J = M - C
                        juros = montante - capital

                        print (f'Os juros compostos foram R${juros:.2f}.')

                    elif opcao == 3:
                        print ('Dados necessários : Capital inicial, Taxa e Montante.')

                        capital = float(input('Capital inicial : R$'))
                        taxa = conversortaxa()
                        montante = float(input('Montante : R$'))
                        
                        tempo = ((log(montante / capital)) / (log(1 + taxa)))

                        opcao = 0
                        while opcao != 'a' or opcao != 'm' or opcao != 'd':
                            opcao = input ('Deseja saber o tempo em anos, meses ou dias (A para anos) (M para meses) (D para dias)?')
                            if opcao.lower() == 'a':
                                print (f'O tempo de aplicação é de {(tempo / 12):.2f} anos.')
                            elif opcao.lower() == 'm':
                                print (f'O tempo de aplicação é de {tempo:.2f} meses.')
                            elif opcao.lower() == 'd':
                                print (print (f'O tempo de aplicação é de {tempo:.2f * 30} dias.'))

                    elif opcao == 4:
                        print ('Dados necessários : Montante, Capital inicial e Tempo de aplicação.')

                        montante = float(input('Montante : R$'))
                        capital = float(input('Capital inicial : R$'))
                        tempo = conversortempo()

                        #i = ((M/C) ** (1 / t) -1)
                        taxa = (((montante / capital) ** (1 / tempo) - 1) * 100)

                        print (f'A taxa de juros é de {taxa:.2f}.')

                    elif opcao == 5:
                        print ('Dados necessários : Capital inicial, Tempo de aplicação e Taxa de juros')

                        capital = float(input('Capital inicial : R$'))
                        tempo = conversortempo()
                        taxa = conversortaxa()

                        #M = C ((1 + i) ** t)
                        montante = (capital * ((1 + taxa) ** tempo))

                        print (f'O montante é de R${montante:.2f}.')

        elif opcao == 3:
            while opcao != 1 or opcao != 2 or opcao != 3 or opcao != 4:
                print ('Opções: ')

                print ('(1) Valor do desconto.')
                print ('(2) Valor nominal.')
                print ('(3) Taxa de desconto.')
                print ('(4) Tempo (antecipação do desconto).')
                
                opcao = int(input('O que deseja calcular ? '))
                if opcao != 1 or opcao != 2 or opcao != 3 or opcao != 4:
                    print('Opção inválida, digite 1, 2, 3 ou 4.')
                
                elif opcao == 1:
                    print ('Dados necessários : Valor nominal, Taxa de desconto e Tempo(antecipação do desconto).')

                    nominal = float(input('Valor nominal do título : R$'))
                    taxa = conversortaxa()
                    tempo = conversortempo()

                    #d = N * i * n
                    desconto = (nominal * taxa * tempo)

                    print (f'O valor do desconto é de R${desconto:.2f}.')
                
                elif opcao == 2:
                    print ('Dados necessários : Valor do desconto, Taxa de desconto e Tempo(antecipação do desconto)')

                    desconto = float(input('Valor do desconto : R$'))
                    taxa = conversortaxa()
                    tempo = conversortempo()

                    #N = d / (i * n)
                    nominal = (desconto / (taxa * tempo))

                    print (f'O valor nominal é de R${nominal:.2f}.')
                
                elif opcao == 3:
                    print ('Dados necessários : Valor do desconto, Valor nominal e Tempo(antecipação do desconto).')

                    desconto = float(input('Valor do desconto : R$'))
                    nominal = float(input('Valor nominal do título : R$'))
                    tempo = conversortempo()

                    #i = d / (i * N)
                    taxa = ((desconto / (tempo * nominal)) * 100)

                    print (f'O valor da taxa é de {taxa:.2f}%.')
                
                elif opcao == 4:
                    print ('Dados necessários : Valor do desconto, Valor nominal e Taxa de desconto.')

                    desconto = float(input('Valor do desconto : R$'))
                    nominal = float(input('Valor nominal do título : R$'))
                    taxa = conversortaxa()

                    #n = d / (i * N)
                    tempo = (desconto / (taxa * nominal))

                    opcao = 0
                    while opcao != 'a' or opcao != 'm' or opcao != 'd':
                        opcao = input ('Deseja saber o tempo em anos, meses ou dias (A para anos) (M para meses) (D para dias)?')
                        if opcao.lower() == 'a':
                            print (f'O tempo (antecipação do desconto) é de {(tempo / 12):.2f} anos.')
                        elif opcao.lower() == 'm':
                            print (f'O tempo (antecipação do desconto) é de {tempo:.2f} meses.')
                        elif opcao.lower() == 'd':
                            print (print (f'O tempo (antecipação do desconto) é de {tempo:.2f * 30} dias.'))
