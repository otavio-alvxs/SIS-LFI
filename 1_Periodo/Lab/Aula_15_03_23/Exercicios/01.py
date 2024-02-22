nome = input('Digite o seu nome: ')
idade = int(input('Qual a sua idade: '))
altura = float(input('Sua altura: '))
peso = float(input('Seu peso: '))
nacionalidade = input('Sua nacionalidade: ')

print('Olá, meu nome é {}, tenho {} anos, {} de altura, peso {:.2f} Kgs, e sou {}.'.format(nome, idade, altura, peso, nacionalidade))
