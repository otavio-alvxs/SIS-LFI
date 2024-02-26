possibilidade = [True, False]

print ('=' * 95)

print ('Fórmula: ((M ^ N) v (¬O <-> P)) ^ (¬(Q ^ M) v (N <-> P))')

print ('=' * 95)

linhas = 0
verdadeiro = 0
falso = 0

for m in possibilidade:
    for n in possibilidade:
        for o in possibilidade:
            for p in possibilidade:
                for q in possibilidade:
                    if ((m and n) or (not o == p) and (not(q and m) or (n == p))):
                        resultadoF = True
                        verdadeiro += 1
                    else:
                        resultadoF = False
                        falso += 1
                    print(f'M = {m} \t N = {n} \t O = {o} \t P = {p} \t Q = {q} \t Fórmula = {resultadoF}')
                    linhas += 1

print ('=' * 95)

print(f'A tabela tem {linhas} linhas.')
print(f'{verdadeiro} linhas verdadeiras\n{falso} linhas falsas.')

print ('=' * 95)

print ('Fim da execução')