#10 Faça um algoritmo que receba “N” números e mostre positivo, negativo ou zero para cada número

resposta = 'S'

while resposta.upper() == 'S':
    numero = float(input('Digite um número: '))
    if numero == 0:
        print ('O valor digitado é igual a 0.')
    elif numero < 0:
        print ('O valor digitado é negativo.')
    elif numero > 0:
        print ('O valor digitado é positivo.')
    
    resposta = str(input('Deseja digitar outro número (S ou N)? '))

print ('Fim da execução')