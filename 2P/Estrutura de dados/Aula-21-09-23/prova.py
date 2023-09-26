import json

with open ('dados_prova.json', 'r')as arquivo_json:
    dados = json.load(arquivo_json)

"""Exibe os nomes em ordem alfabética"""

print (dados)
