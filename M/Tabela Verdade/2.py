possibilidades = [True, False]

print ('=' * 66)

print ('Fórmula: (p -> q) ^ (q -> r) -> (p -> r)')

print ('=' * 66)

linhas = 0
falso = 0
verdadeiro = 0

for p in possibilidades:
    for q in possibilidades:
        for r in possibilidades:
            if (((p == True) and (q == False)) and ((q == True) and (r == False) == True) and ((p == True) and (r == False) == False)):
                resultado = False
                falso += 1
            else:
                resultado = True
                verdadeiro += 1
            print (f'P = {p} \t Q = {q} \t R = {r} \t Resultado = {resultado}')
            linhas += 1

print ('=' * 66)

print (f'A tabela tem {linhas} linhas.')
print (f'{verdadeiro} linhas são verdadeiras.')
print (f'{falso} linhas são falsas.')

print ('=' * 66)
