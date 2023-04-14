"""Faça um algoritmo para ler o salário de um funcionário e aumentá-Io em 15%. Após o aumento, desconte 8% de
impostos. Imprima o salário inicial, o salário com o aumento e o salário final."""

inicial = float(input('Salário do funcionário: R$'))

aumento = inicial + ((inicial / 100) * 15)

final = aumento - ((aumento / 100) * 8)

print (f'O salário inicial era R${inicial}, o salário depois do aumento é de R${aumento}, e depois do desconto dos impostos o salário final é de R${final}')
