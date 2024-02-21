#5- Faça um programa que calcule e mostre a média aritmética de N notas. N equivale ao total de avaliações.

N = int(input('Quantidade de avaliações: '))
T = float(input('Nota total: '))

M = T / N

print (f'A média aritmética das notas das {N} avaliações foi de {M} pontos.')
