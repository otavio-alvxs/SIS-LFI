#9- Uma concessionária de veículos está vendendo os seus veículos com desconto. Faça um algoritmo que calcule e exiba o valor do desconto e o valor a ser pago pelo cliente de vários carros. O desconto deverá ser calculado de acordo com o ano do veículo. Até 2000 - 12% e acima de 2000 - 7%. O sistema deverá perguntar se deseja continuar calculando desconto até que a resposta seja: “(N) Não”. Informar total de carros com ano até 2000 e total geral.

resposta = 'S'

while resposta == 'S':
    valorc = float(input('Valor do carro: '))
    anoc = int(input('Ano do carro: '))

    if anoc <= 2000:
        desconto = (valorc / 100) * 12
    elif anoc > 2000:
        desconto = (valorc / 100) * 7
    
    valort = valorc - desconto

    print (f'O desconto dado foi de {desconto} e o valor total a ser pago é de {valort}')

    resposta = str(input('Deseja continuar calculando (S) ou (N)? '))

print ('Fim da execução.')