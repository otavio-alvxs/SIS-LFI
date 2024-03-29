def contagem_regressiva(n):
    #caso base - caso de parada
    if n == 0:
        print("Fogo!!")
    else:
        print(n)
        #chamada recursiva - funcao chama ela mesma
        return contagem_regressiva(n - 1)

def fatorial(n):
    #caso base
    if n == 0:
        return 1
    else:
        return n*fatorial(n-1)

r = fatorial(5)
print(r)
