from flask import Flask, request
from ibge import busca

app = Flask(__name__)

@app.route("/busca_nome")
def busca_nome():
    try:
        nome = request.args.get("nome")
        response = busca(nome)
        
        # percorrer o retorno do busca e somar todas as ocorrências do nome
        soma = 0
        for valor in response[0]["res"]:
            soma += valor.get("frequencia", 0)

        mensagem = f"A soma de todas as ocorrências do nome Jose é {soma}"
        return mensagem

    except Exception as e:
        return f"Falha na rota /busca_nome: {e}"
    

app.run(debug=True)
