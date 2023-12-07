# criar uma matriz N X M preenchidas com zeros
# N -> numero de linhas
# M -> numero de colunas
# E imprimir na forma de matriz
N = 5
M = 4

matriz = []

for linha in range(N):
    linha = []
    for coluna in range(M):   
        linha.append(0)
    matriz.append(linha)

print("Matriz:")
for linha in matriz:
    for valor in linha:
        print(valor, end=" ")
    print()
