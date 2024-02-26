""" Uma pista de Kart permite 10 voltas para cada um de 6 corredores. 
Faça um programa que leia os nomes e os tempos (em segundos) de cada 
volta de cada corredor e guarde as informações em uma matriz. 
Ao final, o programa deve informar:

a) De quem foi a melhor volta da prova, e em que volta
b) Classificação final em ordem (1º o campeão)
c) Qual foi a volta com a média mais rápida  """

def ler_tempos():
    tempos = []
    for i in range(6):
        nome = input(f"Digite o nome do corredor {i + 1}: ")
        tempos_corredor = []
        for volta in range(1, 11):
            tempo = float(input(f"Digite o tempo da volta {volta} (em segundos) para {nome}: "))
            tempos_corredor.append(tempo)
        tempos.append((nome, tempos_corredor))
    return tempos


def melhor_volta(tempos):
    melhor_tempo = float('inf')
    melhor_corredor = ""
    volta_melhor_tempo = 0
    for i in range(6):
        for volta, tempo in enumerate(tempos[i][1], 1):
            if tempo < melhor_tempo:
                melhor_tempo = tempo
                melhor_corredor = tempos[i][0]
                volta_melhor_tempo = volta
    return melhor_corredor, volta_melhor_tempo


def classificacao_final(tempos):
    tempos_medios = [(nome, sum(tempos_corredor) / len(tempos_corredor)) for nome, tempos_corredor in tempos]
    tempos_medios = sorted(tempos_medios, key=lambda x: x[1])
    return tempos_medios


def volta_media_rapida(tempos):
    media_rapida = float('inf')
    volta_media_rapida = 0
    for volta in range(1, 11):
        media_volta = sum(tempos[i][1][volta - 1] for i in range(6)) / 6
        if media_volta < media_rapida:
            media_rapida = media_volta
            volta_media_rapida = volta
    return volta_media_rapida


def main():
    tempos = ler_tempos()
    
    
    melhor_corredor, volta_melhor_tempo = melhor_volta(tempos)
    print(f" Melhor volta da prova: {melhor_corredor}, Volta: {volta_melhor_tempo}")

    
    classificacao = classificacao_final(tempos)
    print(" Classificação final:")
    for i, (nome, _) in enumerate(classificacao, 1):
        print(f"{i}º lugar: {nome}")

    
    volta_media_rapida_num = volta_media_rapida(tempos)
    print(f" Volta com a média mais rápida: {volta_media_rapida_num}")

if __name__ == "__main__":
    main()