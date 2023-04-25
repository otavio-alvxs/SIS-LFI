possibilidade = [True, False]

linhas = 0
verdadeiro = 0
falso = 0

formula = input('Digite a fórmula: ')

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

print (f'Total de lnhas com resultado VERDADEIRO: {resultado}.')
print (f'Total de linhas com resultado FALSO: {falso}.')
print (f'Total e linhas da tabela: {linhas}.')

