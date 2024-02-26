op = input ('Deseja somar (S) ou multiplicar (M)? ')
if (op == 'S' or op == 'M'):
    x = float(input('Digite o primeiro numero: '))
    y = float(input('Digite o segundo numero: '))
    if (op == 'S'):
        r = x + y
    else:
        r = x * y
    print (f'O resultado é {r}')
else:
    print ('Opção inválida.')
