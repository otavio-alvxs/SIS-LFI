"""A lanchonete Gostosura vende apenas um tipo de sanduíche, cujo recheio inclui duas fatias de queijo, uma
fatia de presunto e uma rodela de hambúrguer. Sabendo que cada fatia de queijo ou presunto pesa 50 gramas, e
que a rodela de hambúrguer pesa 100 gramas, faça um algoritmo em que o dono forneça a quantidade de sanduíches
a fazer, e a máquina informe as quantidades (em quilos) de queijo, presunto e carne necessários para compra"""

sanduiches = int(input('Informe a quantidade de sanduíches a serem feitos: '))
queijo = (2 * sanduiches) * 0.05
presunto = sanduiches * 0.05
hamburger = sanduiches * 0.1

print (f'Serão necessários: \n{queijo}Kgs de Queijo\n{presunto}Kgs de Presunto\n{hamburger}Kgs de hambúrguer.')
