import requests

def busca():
    url = "https://servicodados.ibge.gov.br/api/v1/localidades/municipios?view=nivelado"
    response = requests.get(url)
    return response.json()

def filtra_informacoes():
    json = busca()
    chaves_a_manter = ['municipio-nome', 'UF-nome']
    resultado = [{k: d[k] for k in chaves_a_manter} for d in json]
    return resultado

