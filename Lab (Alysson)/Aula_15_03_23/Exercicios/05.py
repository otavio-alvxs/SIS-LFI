valor = int(input("Informe o valor em centavos: "))

real = valor // 100
valor %= 100

cinquenta = valor // 50
valor %= 50

vinteCinco = valor // 25
valor %= 25

dez = valor // 10
valor %= 10

cinco = valor // 5
valor %= 5

um = valor // 1

print("A menor quantidade de moedas é:")
print(real, "moeda(s) de 1 real")
print(cinquenta, "moeda(s) de 50 centavos")
print(vinteCinco, "moeda(s) de 25 centavos")
print(dez, "moeda(s) de 10 centavos")
print(cinco, "moeda(s) de 5 centavos")
print(um, "moeda(s) de 1 centavo")
