def retornomenu():
    resp = input('Deseja realizar a operação novamente (S para sim e qualquer outra coisa para voltar ao menu)?')
    if resp.lower() != 's':
        opcao = 9
        return opcao

opcoes = {
    1: 'Somar',
    2: 'Subtrair',
    3: 'Multiplicar',
    4: 'Dividir',
    5: 'Limpar memória',
    0: 'Sair'
}

memoria = 0
opcao = 9

while opcao == 9:
    print('=' * 35)
    print(f'Estado da memória: {memoria}')
    print('=' * 35)
    for numero, descricao in opcoes.items():
        print(f'{numero} - {descricao}')
    print('=' * 35)
    opcao = int(input('Escolha a opção: '))

    if opcao not in opcoes:
        print('Opção inválida')

    while opcao == 1:
        num = float(input('Quanto deseja somar à memória? '))
        memoria = memoria + num
        """opcao = retornomenu()
        if opcao == 1:
            continue"""
        