possibilidade = [True, False]

linhas = 0
verdadeiro = 0
falso = 0

l1 = []
l2 = []

quantidade = int(input('Quantas variáveis tem suas fórmulas: '))

while quantidade != 3 and quantidade !=2:
    quantidade = int(input('Quantidade inválida, digite 2 ou 3: '))

formula1 = str(input('Digite a primeira fórmula: '))
formula2 = str(input('Digite a segunda fórmula: '))

if quantidade == 2:

    print ('Tabela 1: ')

    for a in possibilidade:
        for b in possibilidade:
            if eval(formula1):
                resultado = True
                verdadeiro += 1
                l1.append ('True')
            else:
                resultado = False
                falso += 1
                l1.append ('False')
            print (f'A = {a} \t B = {b} \t H = {resultado}')
            linhas += 1
    
    print (f'Total de linhas com resultado VERDADEIRO: {verdadeiro}.')
    print (f'Total de linhas com resultado FALSO: {falso}.')
    print (f'Total e linhas da tabela: {linhas}.')

    if verdadeiro == 0:
        print ('Essa tabela é contraditória.')
    elif falso == 0:
        print ('Essa tabela é tautológica.')
    else:
        print ('Essa tabela é satisfatória.')

    verdadeiro = 0
    falso = 0
    linhas = 0

    print ('Tabela 2:')

    for a in possibilidade:
        for b in possibilidade:
            if eval(formula2):
                resultado = True
                verdadeiro += 1
                l2.append ('True')
            else:
                resultado = False
                falso += 1
                l2.append ('False')

            print (f'A = {a} \t B = {b} \t H = {resultado}')
            linhas += 1

    print (f'Total de linhas com resultado VERDADEIRO: {verdadeiro}.')
    print (f'Total de linhas com resultado FALSO: {falso}.')
    print (f'Total e linhas da tabela: {linhas}.')

    if verdadeiro == 0:
        print ('Essa tabela é contraditória.')
    elif falso == 0:
        print ('Essa tabela é tautológica.')
    else:
        print ('Essa tabela é satisfatória.')

elif quantidade == 3:

    print ('Tabela 1')

    for a in possibilidade:
        for b in possibilidade:
            for c in possibilidade:
                if eval(formula1):
                    resultado = True
                    verdadeiro += 1
                    l1.append('True')
                else:
                    resultado = False
                    falso += 1
                    l1.append('False')
                
                print (f'A = {a} \t B = {b} \t C = {c} \t H = {resultado}')
                linhas += 1

    print (f'Total de linhas com resultado VERDADEIRO: {verdadeiro}')
    print (f'Total de linhas com resultado FALSO: {falso}')
    print (f'Total de linhas da tabela: {linhas}')
        
    if verdadeiro == 0:
        print ('Essa tabela é contraditória.')
    elif falso == 0:
        print ('Essa tabela é tautológica.')
    else:
        print ('Essa tabela é satisfatória.')

    verdadeiro = 0
    falso = 0
    linhas = 0

    print ('Tabela 2')

    for a in possibilidade:
        for b in possibilidade:
            for c in possibilidade:
                if eval(formula2):
                    resultado = True
                    verdadeiro += 1
                    l2.append('True')
                else:
                    resultado = False
                    falso += 1
                    l2.append('False')
                
                print (f'A = {a} \t B = {b} \t C = {c} \t H = {resultado}')
                linhas += 1

    print (f'Total de linhas com resultado VERDADEIRO: {verdadeiro}')
    print (f'Total de linhas com resultado FALSO: {falso}')
    print (f'Total de linhas da tabela: {linhas}')
        
    if verdadeiro == 0:
        print ('Essa tabela é contraditória.')
    elif falso == 0:
        print ('Essa tabela é tautológica.')
    else:
        print ('Essa tabela é satisfatória.')

print (l1)
print (l2)

if l1 == l2:
    print ('As tabelas são equivalentes.')
else:
    print ('As tabelas não são equivalentes')
