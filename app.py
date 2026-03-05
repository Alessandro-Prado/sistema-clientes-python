from flask import Flask, jsonify, request, render_template
from database import conectar, criar_tabela

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

    dados = request.json

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO clientes (nome, telefone, email) VALUES (?, ?, ?)",
        (dados["nome"], dados["telefone"], dados["email"])
    )

    conn.commit()
    conn.close()

    return jsonify({"mensagem": "Cliente cadastrado"})


@app.route("/clientes/<int:id>", methods=["DELETE"])
def deletar_cliente(id):

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM clientes WHERE id = ?", (id,))

    conn.commit()
    conn.close()

    return jsonify({"mensagem": "Cliente deletado com sucesso"})

@app.route("/clientes/<int:id>", methods=["PUT"])
def editar_cliente(id):

    dados = request.json

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE clientes
        SET nome = ?, telefone = ?, email = ?
        WHERE id = ?
        """,
        (dados["nome"], dados["telefone"], dados["email"], id)
    )

    conn.commit()
    conn.close()

    return jsonify({"mensagem": "Cliente atualizado com sucesso"})

if __name__ == "__main__":
    app.run(debug=True)