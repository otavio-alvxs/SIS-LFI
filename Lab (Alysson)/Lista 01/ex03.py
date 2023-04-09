"""O custo ao consumidor de um carro novo é a soma do custo de fábrica com a percentagem do distribuidor e dos
impostos (aplicados ao custo de fábrica). Supondo que a percentagem do distribuidor seja de 28% e os impostos
de 45%, escrever um algoritmo que leia o custo de fábrica de um carro e escreva o custo ao consumidor."""
cf = float(input('Digite o valor do custo de fábrica do carro: '))
dis = (cf / 100) * 28
imp = (cf / 100) * 45
final = cf + dis + imp
print (f'O valor do veículo para o consumidor vai ser de R${final}')
