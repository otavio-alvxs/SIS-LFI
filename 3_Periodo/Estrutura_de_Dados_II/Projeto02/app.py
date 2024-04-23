from flask import Flask, jsonify
import search

app = Flask(__name__)

@app.route("/listar_cidades")
def listar_cidades():
    return jsonify(search.filtra_informacoes())

@app.route("/insertion_sort")
def insertion_sort():
    json = search.remover_acentos()
    json_ordenado, comparacoes, tempo_execucao = search.insertion_sort(json)
    return jsonify({"json_ordenado": json_ordenado, "comparacoes": comparacoes, "tempo_execucao": tempo_execucao})

@app.route("/selection_sort")
def selection_sort():
    json = search.remover_acentos()
    json_ordenado, comparacoes, tempo_execucao = search.selection_sort(json)
    return jsonify({"json_ordenado": json_ordenado, "comparacoes": comparacoes, "tempo_execucao": tempo_execucao})

@app.route("/bubble_sort")
def bubble_sort():
    json = search.remover_acentos()
    json_ordenado, comparacoes, tempo_execucao = search.bubble_sort(json)
    return jsonify({"json_ordenado": json_ordenado, "comparacoes": comparacoes, "tempo_execucao": tempo_execucao})

@app.route("/merge_sort")
def merge_sort():
    json = search.remover_acentos()
    json_ordenado, comparacoes, tempo_execucao = search.merge_sort(json)
    return jsonify({"json_ordenado": json_ordenado, "comparacoes": comparacoes, "tempo_execucao": tempo_execucao})

@app.route("/quick_sort")
def quick_sort():
    json = search.remover_acentos()
    json_ordenado, comparacoes, tempo_execucao = search.quick_sort(json, 0, len(json)-1)
    return jsonify({"json_ordenado": json_ordenado, "comparacoes": comparacoes, "tempo_execucao": tempo_execucao})

if __name__ == "__main__":
    app.run(debug=True)
