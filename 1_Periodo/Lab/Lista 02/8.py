#8- Faça um algoritmo que receba a idade de 75 pessoas e mostre mensagem informando “maior de idade” e “menor de idade” para cada pessoa. Considere a idade a partir de 18 anos como maior de idade.

for idade in range (1,76):
    idade = int(input('Qual a sua idade? '))
    if idade < 18:
        print ('Menor de idade.')
    elif idade >= 18: 
        print ('Maior de idade')
