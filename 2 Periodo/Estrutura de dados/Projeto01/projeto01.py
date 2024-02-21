
def leitura(nome_arquivo: str):
    try:
        lista = []
        with open(nome_arquivo, 'r') as arquivo:
            arquivo.seek(0)
            for linha in arquivo:
                linha = linha.strip()
                if linha.isdigit():
                    valor =  float(linha)
                    lista.append(valor)
            return lista
    except Exception as e:
        print("Houve uma falha na abertura do arquivo")
        print(e)
        return None

def soma_valores_arquivo():
    valores = leitura("entrada.txt")
    resultado = sum(valores)
    print ("Soma dos valores do arquivo: ", resultado)

def maior_valor_arquivo():
    lista = leitura("entrada.txt")
    print ("Maior valor do arquivo: ", max(lista))

def multiplica_valores_arquivo():
    lista = leitura("entrada.txt")
    produto = lista[0]
    for numero in lista[1:]:
        produto *= numero
    print ("Multiplicação dos valores do arquivo: ", produto)

if __name__ == '__main__':
    soma_valores_arquivo()
    maior_valor_arquivo()
    multiplica_valores_arquivo()
