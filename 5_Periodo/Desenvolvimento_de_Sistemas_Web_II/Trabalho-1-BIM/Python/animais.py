import pymysql
import pymysql.cursors
from dbConfig import connect_db
from flask import jsonify
from flask import request, Blueprint

animal_bp = Blueprint("/animal_bp", __name__)

@cidade_bp.route("/animal")
def animal():
    try:
        conn = connect_db()
        cur = conn.cursor(pymysql.cursors.DictCursor)
        cur.execute("SELECT * FROM animais")
        rows = cur.fetchall()
        resp = jsonify(rows)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cur.close()
        conn.close()

@cidade_bp.route("/animal/<id>")
def cidadeById(id):
    try:
        conn = connect_db()
        cur = conn.cursor(pymysql.cursors.DictCursor)
        cur.execute("SELECT * FROM animais WHERE idAnimal = %s", (id))
        rows = cur.fetchall()
        resp = jsonify(rows[0])
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cur.close()
        conn.close()
        


@cidade_bp.route("/animal", methods = ["POST"])
def cidadeNovo():
    try:
        conn = connect_db()
        cur = conn.cursor(pymysql.cursors.DictCursor)
        animal = request.json
        nomeAnimal = animal["nomeAnimal"]
        reino = animal["reino"]
        especie = animal["especie"]
        classificacao = animal["classificacao"]
        biomas = animal["biomas"]
        cur.execute("INSERT INTO animais (nomeAnimal, reino, especie, classificacao, biomas) VALUES (%s,%s,%s,%s,%s)",(nomeAnimal, reino, especie, classificacao, biomas))
        conn.commit()
        resp = jsonify({"message": "inserido"})
        
        
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cur.close()
        conn.close()

@cidade_bp.route("/animal/<id>/", methods = ["PUT"])
def cidadeAlterar(id):
    try:
        conn = connect_db()
        cur = conn.cursor(pymysql.cursors.DictCursor)
        animal = request.json
        nomeAnimal = animal["nomeAnimal"]
        reino = animal["reino"]
        especie = animal["especie"]
        classificacao = animal["classificacao"]
        biomas = animal["biomas"]
        cur.execute("UPDATE animais SET nomeAnimal = %s, reino = %s, especie = %s, classificacao = %s, biomas = %s WHERE idAnimal = %s ",(nomeAnimal, reino, especie, classificacao, biomas, id))
        conn.commit()
        resp = jsonify({"message": "alterado"})
        rows = cur.fetchall()
        resp = jsonify(rows)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
        return e
    finally:
        cur.close()
        conn.close()

@cidade_bp.route("/animal/<id>/", methods = ["DELETE"])
def cidadeExcluir(id):
    try:
        conn = connect_db()
        cur = conn.cursor(pymysql.cursors.DictCursor)
        cur.execute("DELETE FROM animais WHERE idAnimal = %s", (id))
        conn.commit()
        resp = jsonify({"message": "excluido"})
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cur.close()
        conn.close()
