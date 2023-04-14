"""Uma fábrica de camisetas produz os tamanhos pequeno, médio e grande, cada uma sendo vendida respectivamente
por 10, 12 e 15 reais. Construa um algoritmo em que o usuário forneça a quantidade de camisetas pequenas,
médias e grandes referentes a uma venda, e a máquina informe quanto será o valor arrecadado."""

p = int(input('Quantidade de camisetas pequenas: '))
m = int(input('Quantidade de camisetas médias: '))
g = int(input('Quantidade de camisetas grandes: '))

valor = (p * 10) + (m * 12) + (g * 15)

print (f'O valor arrecadado foi de R${valor}.')
