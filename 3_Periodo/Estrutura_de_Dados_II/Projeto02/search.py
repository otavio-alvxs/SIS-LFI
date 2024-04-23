import requests
import unidecode
import time

def busca():
    url = "https://servicodados.ibge.gov.br/api/v1/localidades/municipios?view=nivelado"
    response = requests.get(url)
    return response.json()

def filtra_informacoes():
    json = busca()
    chaves_a_manter = ['municipio-nome', 'UF-nome']
    resultado = [{k: d[k] for k in chaves_a_manter} for d in json]
    return resultado

def remover_acentos():
    json = filtra_informacoes()
    for item in json:
        item['municipio-nome'] = unidecode.unidecode(item['municipio-nome'])
        item['UF-nome'] = unidecode.unidecode(item['UF-nome'])
    return json

def insertion_sort(json):
    comp = 0
    start_time = time.time()
    for i in range(1, len(json)):
        key = json[i]
        j = i - 1
        while j >= 0 and json[j]["municipio-nome"] > key["municipio-nome"]:
            json[j + 1] = json[j]
            j -= 1
            comp += 1
        json[j + 1] = key
    end_time = time.time()
    return json, comp, end_time - start_time

def selection_sort(json):
    comp = 0
    start_time = time.time()
    n = len(json)
    for i in range(n):
        menor_idx = i
        for j in range(i+1, n):
            if json[j]["municipio-nome"] < json[menor_idx]["municipio-nome"]:
                menor_idx = j
                comp += 1
        json[i], json[menor_idx] = json[menor_idx], json[i]
    end_time = time.time()
    return json, comp, end_time - start_time

def bubble_sort(json):
    comp = 0
    start_time = time.time()
    n = len(json)
    for i in range(n):
        for j in range(0, n-i-1):
            if json[j]["municipio-nome"] > json[j+1]["municipio-nome"]:
                json[j], json[j+1] = json[j+1], json[j]
                comp += 1
    end_time = time.time()
    return json, comp, end_time - start_time

def merge_sort(json):
    def merge_sort_helper(json, comp):
        if len(json) > 1:
            meio = len(json)//2
            L = json[:meio]
            R = json[meio:]

            merge_sort_helper(L, comp)
            merge_sort_helper(R, comp)

            i = j = k = 0

            while i < len(L) and j < len(R):
                if L[i]["municipio-nome"] < R[j]["municipio-nome"]:
                    json[k] = L[i]
                    i += 1
                else:
                    json[k] = R[j]
                    j += 1
                k += 1
                comp[0] += 1

            while i < len(L):
                json[k] = L[i]
                i += 1
                k += 1

            while j < len(R):
                json[k] = R[j]
                j += 1
                k += 1

    comp = [0]
    start_time = time.time()
    merge_sort_helper(json, comp)
    end_time = time.time()
    return json, comp[0], end_time - start_time

def particao(json, baixo, alto, comp):
    i = (baixo-1)
    pivo = json[alto]["municipio-nome"]

    for j in range(baixo, alto):

        if json[j]["municipio-nome"] <= pivo:

            i = i+1
            json[i], json[j] = json[j], json[i]
            comp[0] += 1

    json[i+1], json[alto] = json[alto], json[i+1]
    return (i+1)

def quick_sort(json, baixo, alto):
    def quick_sort_helper(json, baixo, alto, comp):
        if len(json) == 1:
            return json
        if baixo < alto:
            pi = particao(json, baixo, alto, comp)
            quick_sort_helper(json, baixo, pi-1, comp)
            quick_sort_helper(json, pi+1, alto, comp)

    comp = [0]
    start_time = time.time()
    quick_sort_helper(json, baixo, alto, comp)
    end_time = time.time()
    return json, comp[0], end_time - start_time
