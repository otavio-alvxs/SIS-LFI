from flask import Flask, Response, jsonify
import search

app = Flask(__name__)

@app.route("/listar_cidades")
def listar_cidades():
    try:
        response = search.listar_alfabetica()
        return Response(response, content_type="application/json; charset=utf-8")
    except Exception as e:
        return f"Falha na rota /listar_cidades: {e}"

@app.route("/listar_estados")
def listar_estados():
    try:
        response = search.listar_cidades_por_estado()
        return jsonify(response)
    except Exception as e:
        return f"Falha na rota /listar_estados: {e}"

@app.route("/teste")
def teste():
    response = search.teste()
    return response

if __name__ == "__main__":
    app.run(debug=True)
