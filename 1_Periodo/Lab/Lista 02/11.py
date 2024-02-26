#11- Faça um algoritmo que receba o preço de custo e o preço de venda de 40 produtos. Mostre como resultado se houve lucro, prejuízo ou empate para cada produto. Informe a média de preço de custo e do preço de venda.

lcusto = []
lvenda = []

for produto in range (1,41):
    custo = float(input('Preço de custo do produto: R$'))
    lcusto.append (custo)
    venda = float(input('Preço de venda do produto: R$'))
    lvenda.append (venda)

    if venda - custo == 0:
        print ('O produto não deu lucro nem prejuízo.')
    elif venda - custo < 0:
        print ('O produto deu prejuízo.')
    elif venda - custo > 0:
        print ('O produto deu lucro.')

mcusto = (sum(lcusto)) / 40
mvenda = (sum(lvenda)) / 40

print (f'A média de preço de custo dos produtos foi de R${mcusto}.')
print (f'A média de preço de venda dos produtos foi de R${mvenda}.')
