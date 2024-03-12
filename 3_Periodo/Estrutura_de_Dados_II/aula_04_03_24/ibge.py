import requests

def busca(nome):
    url = f"https://servicodados.ibge.gov.br/api/v2/censos/nomes/{nome}"
    resposta = requests.get(url)
    return resposta.json()

def calcula_ocorrencias(nome):
    json = busca(nome)
    conteudo = json[0]
    resposta = conteudo.get("res", [])
    soma = []
    for elemento in resposta:
        frequencia = elemento.get("frequencia", 0)
        soma.append(frequencia)
    objeto_retorno = {
        "nome_requisitado" : nome,
        "ocorrencias_totais" : sum(soma)
    }
def maior_frequencia(nome):
    json = busca(nome)
    conteudo = json[0]
    resposta = conteudo.get("res", [])
    maior_periodo = ""
    maior_frequencia = 0
    for elemento in resposta:
        if elemento["frequencia"] > maior_frequencia:
            maior_frequencia = elemento["frequencia"]
            maior_periodo = elemento["periodo"]
    objeto_retorno = {
        "nome_requisitado" : nome,
        "maior_frequencia" : maior_frequencia,
        "periodo" : maior_periodo
    }
    return objeto_retorno

def menor_frequencia(nome):
    json = busca(nome)
    conteudo = json[0]
    resposta = conteudo.get("res", [])
    menor_periodo = ""
    menor_frequencia = 999999999999
    for elemento in resposta:
        if elemento["frequencia"] < menor_frequencia:
            menor_frequencia = elemento["frequencia"]
            menor_periodo = elemento["periodo"]
    objeto_retorno = {
        "nome_requisitado" : nome,
        "menor_frequencia" : menor_frequencia,
        "periodo" : menor_periodo
        }
    return objeto_retorno
