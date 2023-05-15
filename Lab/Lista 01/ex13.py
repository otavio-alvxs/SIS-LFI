"""Faça um algoritmo que receba o preço de custo de um produto e mostre o valor de venda.
Sabe-se que o preço de custo receberá um acréscimo de acordo com um percentual informado
pelo usuário."""

custo = float(input('Preço de custo do produto: R$'))
percentual = float(input('Percentual de acréscimo: '))
venda = custo + ((custo / 100) * percentual)

print (f'O valor de venda do produto será de R${round(venda)}')
