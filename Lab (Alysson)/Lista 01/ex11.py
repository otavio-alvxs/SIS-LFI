"""Faça um algoritmo que receba um valor que foi depositado e exiba o valor com rendimento
após um mês. Considere fixo o juro da poupança em 0,70% a. m."""

valori = float(input('Valor depositado: '))
valorf = ((valori / 100) * 0.70) + valori

print (f'O valor total após 1 mês de rendimento é R${round(valorf)}')

"""Algoritmo que lê o valor e a quantidade de meses que o dinheiro estava aplicado, e exibe
o valor total depois da quantidade de meses informada"""

valori = float(input('Valor depositado: '))
meses = int(input('Meses aplicado: '))
taxa = 0.007

montante = valori * ((1 + taxa) ** meses)

print (f'O montante ao final dos {meses} meses será R${round(montante)}. ')
