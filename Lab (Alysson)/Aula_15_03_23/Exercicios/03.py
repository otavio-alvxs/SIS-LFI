from math import pow, sqrt
x1 = float(input('Digite o valor de X no primeiro ponto: '))
y1 = float(input('Digite o valor de Y no primeiro ponto: '))
x2 = float(input('Digite o valor de X no segundo ponto: '))
y2 = float(input('Digite o valor de Y no segundo ponto: '))
d = sqrt((pow((x2 - x1), 2)) + (pow((y2 - y1), 2)))
print ('A distância entre os 2 pontos é de {:.2f}'.format(d))
