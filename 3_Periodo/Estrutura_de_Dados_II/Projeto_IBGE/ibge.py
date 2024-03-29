import requests

def busca(nome):
    url = f"https://servicodados.ibge.gov.br/api/v2/censos/nomes/{nome}"
    resposta = requests.get(url)
    return resposta.json()

def get_res(nome):
    json = busca(nome)
    conteudo = json[0]
    resposta = conteudo.get("res", [])
    return resposta

def calcula_ocorrencias(nome):
    res = get_res(nome)
    soma = []
    for elemento in res:
        frequencia = elemento.get("frequencia", 0)
        soma.append(frequencia)
    objeto_retorno = {
        "nome_requisitado" : nome,
        "ocorrencias_totais" : sum(soma)
    }
    return objeto_retorno

def maior_frequencia(nome):
    resposta = get_res(nome)
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
    resposta = get_res(nome)
    menor_periodo = ""
    menor_frequencia = float('inf')
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

def ordem_crescente(nome):
    lista = get_res(nome)
    print (lista)
    for i in range(0, len(lista) -1):
        menor = i
        for j in range(i+1, len(lista)):
            if lista[menor]["frequencia"] > lista[j]["frequencia"]:
                menor = j
            lista[i], lista[menor] = lista[menor], lista[i]
    return lista

def bubble_sort(nome):
    lista = get_res(nome)
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j]['frequencia'] > lista[j+1]['frequencia']:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

