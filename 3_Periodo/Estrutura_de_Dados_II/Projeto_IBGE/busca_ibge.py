from flask import Flask, request
import ibge

app = Flask(__name__)

@app.route("/calcular_ocorrencias")
def calcular_ocorrencias():
    try:
        nome = request.args.get("nome")
        objeto_retorno = ibge.calcula_ocorrencias(nome)
        return objeto_retorno
    except Exception as e:
        return f"Falha na rota /busca_nome: {e}"

@app.route("/frequencia_max")
def frequencia_max():
    try:
        nome = request.args.get("nome")
        objeto = ibge.maior_frequencia(nome)
        return objeto
    except Exception as e:
        return f"Falha na rota /frequencia_max: {e}"

@app.route("/frequencia_min")
def frequencia_min():
    try:
        nome = request.args.get("nome")
        objeto = ibge.menor_frequencia(nome)
        return objeto
    except Exception as e:
        return f"Falha na rota /frequencia_min: {e}"

app.run(debug=True)
