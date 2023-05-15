possibilidade = [True, False]

print ('Fórumula (A v B) <-> (¬A ^ ¬B)')

linhas = 0
verdade = 0
mentira = 0

for a in possibilidade:
    for b in possibilidade:
        if (a or b) == (not a and not b) : 
            resultadoF=True
            verdade+=1
        else:
            resultadoF=False
            mentira+=1
        print(f'A = {a} \t B = {b} \t Fórmula: {resultadoF}.')
        linhas+=1


print(f'A tabela tem {linhas} linhas.')
print(f'{verdade} linhas verdadeiras\n{mentira} linhas falsas.')
