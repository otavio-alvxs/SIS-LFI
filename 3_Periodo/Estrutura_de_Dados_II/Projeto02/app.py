from flask import Flask, Response
import search

app = Flask(__name__)

@app.route("/merge_sort")
def merge_sort():
    pass

@app.route("/teste")
def teste():
    response = search.busca()
    return response

app.run(debug=True)