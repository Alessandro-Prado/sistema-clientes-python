from flask import Flask, request, jsonify, render_template
from database import criar_tabela, conectar

app = Flask(__name__)

criar_tabela()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/clientes", methods=["GET"])
def listar_clientes():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM clientes")
    clientes = cursor.fetchall()
    conn.close()

    lista = []

    for cliente in clientes:
        lista.append({
            "id": cliente[0],
            "nome": cliente[1],
            "telefone": cliente[2],
            "email": cliente[3]
        })

    return jsonify(lista)


@app.route("/clientes", methods=["POST"])
def cadastrar_cliente():
    dados = request.get_json()

    nome = dados["nome"]
    telefone = dados["telefone"]
    email = dados["email"]

    conn = conectar()
    cursor = conn.cursor()

    try:
        cursor.execute(
            "INSERT INTO clientes (nome, telefone, email) VALUES (?, ?, ?)",
            (nome, telefone, email)
        )
        conn.commit()
        return jsonify({"mensagem": "Cliente cadastrado!"}), 201

    except:
        return jsonify({"erro": "Email já cadastrado!"}), 400

    finally:
        conn.close()


if __name__ == "__main__":
    app.run(debug=True)