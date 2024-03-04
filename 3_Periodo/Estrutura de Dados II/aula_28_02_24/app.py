from flask import Flask, request
import requests

# instanciar a aplicação
app = Flask(__name__)

@app.route("/") ### / --> root
def index():
    return "aplicacao online"

@app.route("/calcula", methods=["GET"])
def calcula():
    #http://127.0.0.1:5000/calcula?qtd=50&preco=2
    quantidade = int(request.args.get("qtd"))
    preco = int(request.args.get("preco"))
    return f"R$ {quantidade*preco}"

#rodar a app
#debug == True para nao ser necessario recarregar a app no navegadorm por ex. So utilizar em ambiente de desenvolvimento

app.run(debug=True)
