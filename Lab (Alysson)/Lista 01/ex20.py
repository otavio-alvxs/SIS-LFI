"""Pedrinho tem um cofrinho com muitas moedas, e deseja saber quantos reais conseguiu poupar. Faça um programa
para ler a quantidade de cada tipo de moeda, e imprimir o valor total economizado, em reais. Considere que
existam moedas de 1, 5, 10, 25 e 50 centavos, e ainda moedas de 1 real. Não havendo moeda de um tipo, a
quantidade respectiva é zero."""

m1r = int(input('Quantidade de moedas de 1 real: '))
m50 = int(input('Quantidade de moedas de 50 centavos: ')) * 50
m25 = int(input('Quantidade de moedas de 25 centavos: ')) * 25
m10 = int(input('Quantidade de moedas de 10 centavos: ')) * 10
m5 = int(input('Quantidade de moedas de 5 centavos: ')) * 5
m1 = int(input('Quantidade de moedas de 1 centavo: ')) * 1

total = ((m50 + m25 + m10 + m5 + m1) / 100) + m1r

print (f'A quantidade total economizada foi de R${round(total)}.')
