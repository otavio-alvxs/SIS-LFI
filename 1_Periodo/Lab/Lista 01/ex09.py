"""Um motorista deseja colocar no seu tanque X reais de gasolina. Escreva um algoritmo para ler o preço
do litro da gasolina e o valor do pagamento, e exibir quantos litros ele conseguiu colocar no tanque."""

gas = float(input('Valor do litro da gasolina: '))
valor = float(input('Valor a ser abastecido: '))

print  (f'Serão colocados no tanque {valor / gas} litros de gasolina.')
