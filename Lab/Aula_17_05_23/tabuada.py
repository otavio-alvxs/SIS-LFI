
for contador in range(1,11):
    print ("=" * 20)
    print (f"Tabuada do {contador}")
    for fator in range(1,11):
        resultado = contador * fator
        print (f"{contador} x {fator}\t=\t{resultado}")
