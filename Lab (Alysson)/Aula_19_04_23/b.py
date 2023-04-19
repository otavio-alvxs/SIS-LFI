mes = int(input('Entre com um mês (1 a 12): '))

if (mes == 1 or mes == 5 or mes == 7 or  mes == 8 or mes == 10 or mes == 12):
    print ('Esse mês tem 31 dias.')
elif (mes == 4 or mes == 6 or mes == 9 or mes == 11):
    print ('Esse mes tem 30 dias.')
elif mes == 2:
    ano = int(input('Entre com o ano (4 digitos): '))
    if ano % 400 == 0 or ano % 4 == 0 and ano % 100 != 0:
        print ('Esse mes tem 29 dias.')
    else:
        print ('Esse mes tem 28 dias.')
else:
    print ('Mês Inválido!')
