# 2- Faça um programa que leia uma matriz 3x3 e multiplique os elementos da diagonal principal da matriz por um
# número k. Imprima a matriz na tela antes e depois da multiplicação.

import random

matriz = [[12,37,91],
          [9,62,76],
          [87,45,23]]

for x in matriz:
    print(x)

print('-------------')

print('Diagonal principal da matriz multiplicada por 2: ')

for x in range(3):
    for y in range(3):
        matriz[x][y]
    if x == y:
        matriz[0][0] = matriz[0][0]*2
        matriz[1][1] =  matriz[1][1]*2
        matriz[2][2] = matriz[2][2]*2

for x in matriz:
    print(x)
