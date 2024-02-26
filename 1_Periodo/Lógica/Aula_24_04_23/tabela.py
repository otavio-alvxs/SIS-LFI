possibilidade = [True, False]

linhas = 0
verdadeiro = 0
falso = 0

quantidade = int(input('Quantas variáveis tem sua fórmula: '))

while quantidade != 3 and quantidade !=2:
    quantidade = int(input('Quantidade inválida, digite 2 ou 3: '))

formula = input('Digite a fórmula: ')


if quantidade == 2:
    for a in possibilidade:
        for b in possibilidade:
            if eval(formula):
                resultado = True
                verdadeiro += 1
            else:
                resultado = False
                falso += 1

            print (f'A = {a} \t B = {b} \t H = {resultado}')
            linhas += 1

elif quantidade == 3:
    for a in possibilidade:
        for b in possibilidade:
            for c in possibilidade:
                if eval(formula):
                    resultado = True
                    verdadeiro += 1
                else:
                    resultado = False
                    falso += 1

                print (f'A = {a} \t B = {b} \t C = {c} \t H = {resultado}')
                linhas += 1

print (f'Total de lnhas com resultado VERDADEIRO: {verdadeiro}.')
print (f'Total de linhas com resultado FALSO: {falso}.')
print (f'Total e linhas da tabela: {linhas}.')

if verdadeiro == 0:
    print ('Essa tabela é contraditória.')

elif falso == 0:
    print ('Essa tabela é tautológica.')

else:
    print ('Essa tabela é satisfatória.')
