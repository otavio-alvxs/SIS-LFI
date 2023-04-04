#1
L_VAZIA = []
#2
possibilidadeBoleanos = [True, False]
#3
valores_Diversos = [1, -2, True, "Obabão", False, 1947, 5.3, -10]
#4
print(valores_Diversos[1], ",", valores_Diversos[6])
#5
print(valores_Diversos[1], ",", valores_Diversos[3])
#6
tamanho = len(valores_Diversos)
#7
for x in valores_Diversos:
    print(x)
print (f"Foram encontrados {tamanho} itens na lista.") 
#8
BEBIDAS = ["Água", "Refrigerante", "Café", "Suco"]
#9
COMIDAS = ["Pizza", "Hambúrger", "Esfiha", "Cachorro Quente"]
#10
for i, bebida in enumerate(BEBIDAS):
    for j, comida in enumerate(COMIDAS):
        print(f"Combinação {i*len(COMIDAS)+j+1}: {bebida} e {comida}")
#11
A = int(input("Digite um número inteiro: "))
B = int(input("Digite um número inteiro: "))
C = int(input("Digite um número inteiro: "))

if A == 0 or B == 0 or C and A != 7:    
    print("OK")
else:
    print("NEGATIVO")
#12
altura = int(input("Altura: "))
largura = int(input("Largura: "))

if largura > altura or largura == altura:
    print("Verdadeiro")
else:
    print("Falso")
