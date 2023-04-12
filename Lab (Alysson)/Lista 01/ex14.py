"""A padaria Hotpão vende uma certa quantidade de pães franceses e uma quantidadede bolos a
cada dia. Cada pãozinho custa R$ 0,12 e o pedaço de bolo custa R$ 1,50. Ao final do dia, o
dono quer saber quanto arrecadou com a venda dos pães e bolos (juntos), e quanto' deve guardar
numa conta de poupança (10% do total arrecadado). Você foi contratado para fazer os cálculos
para o dono. Com base nestes fatos, faça um algoritmo para ler as quantidades de pães e de bolos
vendidos, e depois calcular quanto arrecadou naquele dia e quanto deve guardar na poupança."""

paes = int(input('Quantidade de pães vendidos: '))
bolos = int(input('Quantidade de bolos vendidos: '))

total = round((paes * 0.12) + (bolos * 1.5))

print (f'O valor a ser guardado na poupança é de R${total / 10}')
