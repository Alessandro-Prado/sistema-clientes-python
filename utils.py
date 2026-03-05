import re

def gerar_id(clientes):
    if not clientes:
        return 1
    return max(cliente["id"] for cliente in clientes) + 1


def email_valido(email):
    padrao = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(padrao, email)