import requests

def busca(nome):
    url = f"https://servicodados.ibge.gov.br/api/v2/censos/nomes/{nome}"
    resposta = requests.get(url)
    return resposta.json()

def calcula_ocorrencias(json):
    conteudo = json[0]
    resposta = conteudo.get("res", [])
    soma = []
    for elemento in resposta:
        frequencia = elemento.get("frequencia", 0)
        soma.append(frequencia)
    return sum(soma)

def maior_frequencia(json):
    conteudo = json[0]
    resposta = conteudo.get("res", [])
    maior_periodo = ""
    maior_frequencia = 0
    for elemento in resposta:
        if elemento["frequencia"] > maior_frequencia:
            maior_frequencia = elemento["frequencia"]
            maior_periodo = elemento["periodo"]
    objeto = {
        "maior_frequencia" : maior_frequencia,
        "periodo" : maior_periodo
    }
    return objeto

def menor_frequencia(nome):
    json = busca(nome)
    conteudo = json[0]
    resposta = conteudo.get("res", [])
    print (resposta)
    menor_periodo = ""
    menor_frequencia = 999999999999
    for elemento in resposta:
        if elemento["frequencia"] < menor_frequencia:
            menor_frequencia = elemento["frequencia"]
            menor_periodo = elemento["periodo"]
    objeto = {
        f"Nome requisitado: {nome}"
        "menor_frequencia" : menor_frequencia,
        "periodo" : menor_periodo
    }
    return objeto

