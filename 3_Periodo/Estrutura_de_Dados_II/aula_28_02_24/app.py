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
    print(str(request))
    print(request.args)
    print(request.args.get("qtd"))
    
    quantidade = (request.args.get("qtd"))
    preco = (request.args.get("preco"))

    if quantidade is not None and preco is not None:    
        return f"R$ {int(quantidade)*int(preco)}"
    return "Um dos parâmetros não foi passado!"
    return "OK"

@app.route("/paridade", methods=["GET"])
def paridade():
    valor = request.args.get("valor")
    #return valor % 2 == 0
    if int(valor) % 2 == 0:
        return f"{valor} é par"
    else:
        return f"{valor} é ímpar"
    
    
# def verifica_par(valor):
#     valor = request.args.get("valor")
#     #return valor % 2 == 0
#     if int(valor) % 2 == 0:
#         return f"{valor} é par"
#     else:
#         return f"{valor} é ímpar"
    
@app.route("/somar_ate", methods=["GET"])
def somar_ate():
    valor = int(request.args.get("valor"))
    soma = 0
    for i in range(1, valor + 1):
        soma += i
    return f"A soma de 0 até {valor} é igual a {soma}"

# rodar a app
# debug == True para nao ser necessario recarregar a app no navegador por ex.
# So utilizar em ambiente de desenvolvimento

app.run(debug=True)
