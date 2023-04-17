possibilidades = [True, False]

print ('=' * 94)

print ('Fórmula: (p ^ q) -> (p v q)')

print ('=' * 94)

linhas = 0
verdadeiro = 0
falso = 0

for p in possibilidades:
    for q in possibilidades:
        if ((p and q) == True) and ((p or q) == False):
            resultado = False
            falso += 1
        else:
            resultado = True
            verdadeiro += 1

        print (f'P = {p} \t Q = {q} \t (p ^ q) = {p and q} \t (p v q) = {p or q} \t Fórmula = {resultado}')
        linhas += 1

print ('=' * 94)

print (f'A tabela tem {linhas} linhas.')
print (f'{verdadeiro} linhas são verdadeiras.')
print (f'{falso} linhas são falsas.')

print ('=' * 94)
