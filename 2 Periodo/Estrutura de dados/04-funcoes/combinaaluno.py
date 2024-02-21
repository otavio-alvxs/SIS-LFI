def media(x):

    if x >6:
        return 'Aprovado'
    elif x >=4 and x <=6:
        return 'Verificação Suplementar'
    elif x< 4:
        return 'Reprovado'
    else:
        return 'Nota inválida'
    
x = float(input('digite sua média:'))
média = media(x)
print(média)