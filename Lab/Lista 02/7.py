#7- Ler 80 números e ao final informar quantos número(s) est(á)ão no intervalo entre 10 (inclusive) e 150 (inclusive).

contador = 0

for _ in range(80):
    numero = int(input("Digite um número: "))
    if 10 <= numero <= 150:
        contador += 1

print(f"Existem dentre os 80 números lidos {contador} números no intervalo entre 10 e 150")
