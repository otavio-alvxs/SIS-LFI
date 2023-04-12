"""Escrever um algoritmo que leia o nome de um aluno e as notas das três provas que ele obteve no semestre.
No final informar o nome do aluno e a sua média (aritmética)."""

nome = input ('Digite o nome do aluno: ')
nota1 = float(input('Digite o valor da primeira nota: '))
nota2 = float(input('Valor da segunda nota: '))
nota3 = float(input('Valor da terceira nota: '))

media = (nota1 + nota2 + nota3) / 3

print (f'A média das notas do aluno {nome} foi de : {media}')
