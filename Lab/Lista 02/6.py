"""6- Escrever um algoritmo que lê o número de identificação, as 3 notas entre 0 e 10 obtidas por um aluno nas 3 verificações e a nota dos exercícios (ME) tambem entre 0 e 10 que fazem parte da avaliação. Calcular a média de aproveitamento, usando a fórmula:
MA = (Nota1 + Nota2 x 2 + Nota3 x 3 + ME )/7
A atribuição de conceitos obedece a tabela abaixo:

Média de Aproveitamento | Conceito
MA >= 9,0               | A
7,5 <= MA < 9,0         | B
6,0 <= MA < 7,5         | C
4,0 <= MA < 6,0         | D
MA < 4,0                | E """

while True:
    iden = int(input('Número de identificação: '))

    n1 = float(input('Primeira nota (0 - 10): '))
    n2 = float(input('Segunda nota (0 - 10): '))
    n3 = float(input('Terceira nota (0 - 10): '))
    ME = float(input('Nota dos exercícios (0 - 10): '))

    MA = (n1 + (n2 * 2) + (n3 * 3) + ME) / 7

    if MA >= 9:
        conceito = "A"
    elif MA < 9 and MA >= 7.5:
        conceito = "B"
    elif MA < 7.5 and MA >= 6:
        conceito = "C"
    elif MA < 6 and MA >= 4:
        conceito = "D"
    elif MA < 4:
        conceito = "E"

    print (MA)
    print (f'As notas do aluno identificado pelo número {iden} foram: \nAvaliação 1: {n1}\nAvaliação 2: {n2}\nAvaliação 3: {n3}')
    print (f'Sua média de aproveitamento foi: {MA:.2f} e conceito: {conceito}')

    if conceito == "A" or conceito == "B" or conceito == "C":
        status = "Aprovado"
    else:
        status = "Reprovado"

    print (f'O aluno foi {status}')

    resposta = input("\nDeseja digitar as notas de outro aluno? (S/N): ")
    if resposta.lower() != 's':
        break

print ('Fim da execução.')
