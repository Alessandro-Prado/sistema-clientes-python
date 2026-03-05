import sqlite3
from database import conectar
from utils import email_valido


def cadastrar_cliente():
    nome = input("Nome: ").strip().title()
    telefone = input("Telefone: ").strip()

    while True:
        email = input("Email: ").strip().lower()
        if email_valido(email):
            break
        else:
            print("Email inválido!")

    conn = conectar()
    cursor = conn.cursor()

    try:
        cursor.execute(
            "INSERT INTO clientes (nome, telefone, email) VALUES (?, ?, ?)",
            (nome, telefone, email)
        )
        conn.commit()
        print("Cliente cadastrado com sucesso!")

    except sqlite3.IntegrityError:
        print("Email já cadastrado!")

    finally:
        conn.close()


def listar_clientes():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM clientes")
    clientes = cursor.fetchall()

    conn.close()
    return clientes