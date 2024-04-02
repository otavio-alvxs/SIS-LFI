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

@app.route("/ordem_crescente")
def ordem_crescente():
    try:
        nome = request.args.get("nome")
        objeto = ibge.ordem_crescente(nome)
        return objeto
    except Exception as e:
        return f"Falha na rota /ordem_crescente: {e}"

@app.route("/bubble_sort")
def bubble_sort():
    try:
        nome  = request.args.get("nome")
        objeto = ibge.bubble_sort(nome)
        return objeto
    except Exception as e:
        return f"Falha na rota /bubble_sort: {e}"

@app.route("/teste")
def teste():
    try:
        nome = request.args.get("nome")
        teste = ibge.busca(nome)
        return teste
    except Exception as e:
        return f"Falha na rota /teste: {e}"

app.run(debug=True)
