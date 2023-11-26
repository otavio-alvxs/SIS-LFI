lista = ['Zacarias', 'Dede', 'Mussum', 'Didi']
print (lista[2])

notas = [[10,20,90],
         [30,40],
         [50,60,80,90],
         [70,80]]

print (notas[1])
notas[3][0] = notas[3][0]*10
print (notas)

for linha in range(4):
    print(notas[linha])

print (f'Total de linhas: {len(notas)}')
for linha in range(len(notas)):
    notas_aluno = notas[linha]
    for coluna in range(len(notas_aluno)):
        print(notas[linha][coluna])
    print()
