possibilidades = [True, False]

print ('Fórmula ((((A ^ B) v (A ^ ¬C)) ^ (¬A <-> D)) <-> (((¬A v E) ^ (¬E ^ F)) v (¬D ^ ¬F))) ^ (¬B v G)')

linhas = 0
falso = 0
verdadeiro = 0

for a in possibilidades:
    for b in possibilidades:
        for c in possibilidades:
            for d in possibilidades:
                for e in possibilidades:
                    for f in possibilidades:
                        for g in possibilidades:
                            if (((a and b) or (a and not c)) and (not a == d)) == (((not a or e) and (not e and f) or (not d and not f))) and (not b or g):
                                resultado = True
                                verdadeiro += 1
                            else:
                                resultado = False
                                falso += 1
                            print (f'A = {a} \t B = {b} \t C = {c} \t D = {d} \t E = {e} \t F = {f} \t G = {g} \t Fórmula = {resultado}')
                            linhas += 1

print (f'A tabela tem {linhas} linhas.')
print (f'{verdadeiro} linhas são verdadeiras.')
print (f'{falso} linhas são falsas.')
