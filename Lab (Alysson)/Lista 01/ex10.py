"""Escrever um algoritmo que leia o nome de um vendedor, o seu salário fixo e o total de vendas
efetuadas por ele no mês (em dinheiro). Sabendo que este vendedor ganha 15% de comissão sobre
suas vendas efetuadas, informar o seu nome, o salário fixo e salário no final do mês."""

nome = input ('Nome do vendedor: ')
salario = float(input('Qual é o valor do seu salário fixo? '))
vendas = int(input('Total de vendas no mês: '))
vvendas = float(input('Valor de cada venda: '))

comissao = (vvendas / 100 * 15) * vendas
final = comissao + salario

print (f'O salario inicial de {nome} é de R${salario}, e o salario final (salario + comissao) é de R${final}.')
