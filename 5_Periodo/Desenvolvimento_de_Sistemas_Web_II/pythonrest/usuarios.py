import pymysql
import pymysql.cursors
from db_config import connect_db
from flask import Blueprint, jsonify

usuario_bp = Blueprint("usuario", __name__)

@usuario_bp.route("/usuario")
def get_usuario():
    try:
        conn = connect_db()
        cur = conn.cursor(pymysql.cursors.DictCursor)
        cur.execute("SELECT * FROM usuario ")
        rows = cur.fetchall()
        resp = jsonify(rows)
        return resp
    except Exception as e:
        print(e)
    finally:
        cur.close()
        conn.close()

@usuario_bp.route("/usuario/<id>")
def get_usuario_id(id):
    try:
        conn = connect_db()
        cur = conn.cursor(pymysql.cursors.DictCursor)
        cur.execute("""SELECT
                        *
                    FROM
                        usuario
                    WHERE
                        idusuario = %s"""
                    ,(id))
        rows = cur.fetchall()
        resp = jsonify(rows[0])
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cur.close()
        conn.close()

@usuario_bp.route("/usuario", methods = ["POST"])
def post_usuario():
    try:
        conn = connect_db()
        cur = conn.cursor(pymysql.cursors.DictCursor)

        usuario = request.json
        nome = usuario["nome"]
        email = usuario["email"]
        senha = usuario["senha"]
        telefone = usuario["telefone"]

        cur.execute("""INSERT INTO usuario
                       (nome, email, senha, telefone)
                       VALUES (%s, %s, %s, %s)""",
                       (nome, email, senha, telefone))
        conn.commit()
        resp = jsonify({"message": "inserido"})
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cur.close()
        conn.close()