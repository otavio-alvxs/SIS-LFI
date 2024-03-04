from flask import Flask, request
import requests

app = Flask(__name__)

@app.route("/usuario", methods=["GET"])
def index():
    try:
        # http://127.0.0.5000/usuario?name=Cebolinha&idade=7
        user = request.args.get("name", "padrao")
        idade= int(request.args.get("idade"))
        return f"Ola {user} - {idade} anos"
    except:
        return "Falha!!!"

@app.route("/IBGE", methods="GET")
def consulta_ibge():
    nome = request.args.get("name")
    resposta = request()
    return resposta

app.run(debug=True)
