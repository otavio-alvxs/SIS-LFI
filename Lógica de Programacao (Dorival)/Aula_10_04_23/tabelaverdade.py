vetorPossibilidade = [True, False]

print('Fórmula 2: (A <-> B) ^ ¬(A v B)')

linhas = 0
verdade = 0
mentira = 0

for a in vetorPossibilidade:
    for b in vetorPossibilidade:
        if (a == b) and not (a or b) :
            resultadoF=True
            verdade+=1
        else:
            resultadoF=False
            mentira+=1
        print(f'A = {a} \t B = {b} \t Fórmula: {resultadoF}.')
        linhas+=1
print(f'A tabela tem {linhas} linhas.')
print(f'{verdade}linhas verdadeiras, {mentira}linhas falsas.')
