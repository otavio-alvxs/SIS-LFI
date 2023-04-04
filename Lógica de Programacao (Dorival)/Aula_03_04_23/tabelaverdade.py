vetorPossibilidade = [True, False]

print("Testador de Fórmulas Tabajara 1.0")
print("(A ^ B) v (¬A ^ ¬B)")

linhas = 0

for a in vetorPossibilidade:
    for b in vetorPossibilidade:
        if (a and b) or (not a and not b):
            resultadoF=True
        else:
            resultadoF=False
        print(f'A = {a} \t B = {b} \t H: {resultadoF}.')
        linhas+=1
print(f'A tabela tem {linhas} linhas.')

print('='*49)

print('Fórmula 2: (A <-> B) ^ ¬(A v B)')

linhas = 0

for a in vetorPossibilidade:
    for b in vetorPossibilidade:
        if (a == b) and not (a or b) :
            resultadoF=True
        else:
            resultadoF=False
        print(f'A = {a} \t B = {b} \t Fórmula: {resultadoF}.')
        linhas+=1
print(f'A tabela tem {linhas} linhas.')