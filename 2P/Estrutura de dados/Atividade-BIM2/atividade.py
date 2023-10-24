def retornomenu(a):
    resp = input('Deseja realizar a operação novamente (S para sim e qualquer outra coisa para voltar ao menu) ? ')
    if resp.lower() != 's':
        opcao = 9
        return opcao
    else:
        opcao = a
        return opcao

def estado():
    print (f'Valor na memória: {memoria}')

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
    print ('=' * 35)
    estado()
    print ('=' * 35)
    for numero, descricao in opcoes.items():
        print (f'{numero} - {descricao}')
    print ('=' * 35)
    opcao = int(input('Escolha a opção: '))

    if opcao not in opcoes:
        print('Opção inválida')

    elif opcao == 0:
        print ('Programa finalizado.')
        break

    while opcao == 1:
        estado()
        num = float(input('Quanto deseja somar ao valor na memória? '))
        resultado = memoria + num
        print (f'{memoria} + {num} = {resultado}')
        memoria = resultado
        opcao = retornomenu(1)
    
    while opcao == 2:
        estado()
        num = float(input('Quanto deseja subtrair do valor na memória? '))
        resultado = memoria - num
        print (f'{memoria} - {num} = {resultado}')
        memoria = resultado
        opcao = retornomenu(2)

    while opcao == 3:
        estado()
        num = float(input('Por quanto deseja multiplicar o valor na memória? '))
        resultado = memoria * num
        print (f'{memoria} * {num} = {resultado}')
        memoria = resultado
        opcao = retornomenu(3)
    
    while opcao == 4:
        estado()
        num = float(input('Por quanto deseja dividir o valor na memória? '))
        resultado = memoria / num
        print (f'{memoria} / {num} = {resultado}')
        memoria = resultado
        opcao = retornomenu(4)

    while opcao == 5:
        memoria = 0
        print ('Memória limpa \nVoltando ao menu')
        opcao = 9
