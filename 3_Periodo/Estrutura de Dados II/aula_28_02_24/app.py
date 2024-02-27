from flask import Flask, request

app = Flask(__name__)

@app.route("/usuario")
def index():
    try:
        user = request.args.get("nome")
        return f"Ola {user}"
    except:
        