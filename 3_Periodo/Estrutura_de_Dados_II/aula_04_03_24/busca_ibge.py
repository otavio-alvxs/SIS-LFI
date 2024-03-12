from flask import Flask, request
import ibge

app = Flask(__name__)

@app.route("/busca_nome")
def busca_nome():
    try:
        nome = request.args.get("nome")
        response = ibge.busca(nome)
        soma = ibge.calcula_ocorrencias(response)
        objeto_retorno = {
            "nome_procurado": nome,
            "total_ocorrencias": soma
        }  
        return objeto_retorno
    except Exception as e:
        return f"Falha na rota /busca_nome: {e}"

@app.route("/frequencia_max")
def frequencia_max():
    try:
        nome = request.args.get("nome")
        json = ibge.busca(nome)
        objeto = ibge.maior_frequencia(json)
        return objeto
    except Exception as e:
        return f"Falha na rota /busca_nome: {e}"

@app.route("/frequencia_min")
def frequencia_min():
    try:
        nome = request.args.get("nome")
        objeto = ibge.menor_frequencia(nome)
        return objeto
    except Exception as e:
        return f"Falha na rota /frequencia_min: {e}"

app.run(debug=True)
