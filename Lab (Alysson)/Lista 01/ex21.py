"""Uma loja de roupas está fazendo uma liquidação e está oferecendo um desconto de 30% em todas as peças.
Faça um programa em que o vendedor informe o valor da roupa e o programa retorna quanto ela custará durante
a liquidação?"""

valor = float(input('Valor da peça ou das peças compradas: R$'))
desconto = (valor / 100) * 30
final = valor - desconto

print (f'O valor a ser pago será R${final}.')
