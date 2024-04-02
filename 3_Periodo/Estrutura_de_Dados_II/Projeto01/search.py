import requests
from unicode import unicode_dict
import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

def busca():
    url = "https://servicodados.ibge.gov.br/api/v1/localidades/municipios?view=nivelado"
    response = requests.get(url)
    return response.json()

def corrigir_unicode(string):
    for key, value in unicode_dict.items():
        string = string.replace(key, value)
    return string

def remover_acentos(texto):
    mapeamento = {
        ord('á'): 'a', ord('à'): 'a', ord('â'): 'a', ord('ã'): 'a', ord('ä'): 'a',
        ord('é'): 'e', ord('è'): 'e', ord('ê'): 'e', ord('ë'): 'e',
        ord('í'): 'i', ord('ì'): 'i', ord('î'): 'i', ord('ï'): 'i',
        ord('ó'): 'o', ord('ò'): 'o', ord('ô'): 'o', ord('õ'): 'o', ord('ö'): 'o',
        ord('ú'): 'u', ord('ù'): 'u', ord('û'): 'u', ord('ü'): 'u',
        ord('ñ'): 'n', ord('ç'): 'c',
        ord('Á'): 'A', ord('À'): 'A', ord('Â'): 'A', ord('Ã'): 'A', ord('Ä'): 'A',
        ord('É'): 'E', ord('È'): 'E', ord('Ê'): 'E', ord('Ë'): 'E',
        ord('Í'): 'I', ord('Ì'): 'I', ord('Î'): 'I', ord('Ï'): 'I',
        ord('Ó'): 'O', ord('Ò'): 'O', ord('Ô'): 'O', ord('Õ'): 'O', ord('Ö'): 'O',
        ord('Ú'): 'U', ord('Ù'): 'U', ord('Û'): 'U', ord('Ü'): 'U',
        ord('Ñ'): 'N', ord('Ç'): 'C'
    }
    return texto.translate(mapeamento)

def listar_alfabetica():
    json = busca()
    lista = []
    for cidade in json:
        nome_cidade = cidade["municipio-nome"]
        nome_cidade_corrigido = corrigir_unicode(nome_cidade)
        lista.append(nome_cidade_corrigido)
    lista_ordenada = sorted(lista, key=locale.strxfrm)
    return ',\n'.join(lista_ordenada)

def listar_cidades_por_estado():
    json = busca()
    estados = {}

    for cidade in json:
        estado = cidade["UF-nome"]
        nome_cidade = cidade["municipio-nome"]
        nome_cidade_sem_acentos = remover_acentos(nome_cidade)

        if estado in estados:
            estados[estado].append(nome_cidade_sem_acentos)
        else:
            estados[estado] = [nome_cidade_sem_acentos]

    return estados

def teste():
    json = busca()
    return json
