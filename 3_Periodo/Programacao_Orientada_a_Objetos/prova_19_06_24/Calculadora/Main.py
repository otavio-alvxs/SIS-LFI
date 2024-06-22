from Operadores import Operadores

def menu():
    print("-" * 5, "Calculadora", "-" * 5)
    print("[1] - Adição")
    print("[2] - Subtração")
    print("[3] - Multiplicação")
    print("[4] - Divisão")
    print("[0] - Sair")
    print("-" * 21)
    return int(input("Digite a operação desejada: "))

def pegaValores():
    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))
    numeros = Operadores(n1, n2)
    return numeros

opcao = 5

while opcao != 0:
    opcao = menu()

    if opcao == 1:
        numeros = pegaValores()
        total = numeros.soma()
        print(f"A soma de {numeros.valor01} e {numeros.valor02} é: {total}")
        print()
    elif opcao == 2:
        numeros = pegaValores()
        total = numeros.subtracao()
        print(f"A subtração de {numeros.valor01} e {numeros.valor02} é: {total}")
        print()
    elif opcao == 3:
        numeros = pegaValores()
        total = numeros.multiplicacao()
        print(f"A multiplicação de {numeros.valor01} e {numeros.valor02} é: {total}")
        print()
    elif opcao == 4:
        numeros = pegaValores()
        total = numeros.divisao()
        print(f"A divisão de {numeros.valor01} e {numeros.valor02} é: {total}")
        print()
    elif opcao == 0:
        print("Saindo...")
    else:
        print("OPÇÃO INVÁLIDA")
        print()

print("Programa encerrado.")
