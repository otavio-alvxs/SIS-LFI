possibilidade = [True, False]

print ('Fórumula (A v B) <-> (¬A ^ ¬B)')

linhas = 0
verdade = 0
mentira = 0

for a in possibilidade:
    for b in possibilidade:
        for c in possibilidade:
            for d in possibilidade:
                for e in possibilidade:
                    if (a == (not (b and c))) or (not (not a or d) == (not e and b)) :
                        resultadoF=True
                        verdade+=1
                    else:
                        resultadoF=False
                        mentira+=1
                    print(f'A = {a} \t B = {b} \t C = {c} \t D = {d} \t E = {e} \t Fórmula: {resultadoF}.')
                    linhas+=1

print(f'A tabela tem {linhas} linhas.')
print(f'{verdade} linhas verdadeiras\n{mentira} linhas falsas.')
