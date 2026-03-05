from database import criar_tabela
from services import (
    cadastrar_cliente,
    listar_clientes,
    atualizar_cliente,
    deletar_cliente
)

criar_tabela()

while True:
    print("""
1 - Cadastrar cliente
2 - Listar clientes
3 - Atualizar cliente
4 - Deletar cliente
0 - Sair
""")

    opcao = input("Escolha: ")

    if opcao == "1":
        cadastrar_cliente()

    elif opcao == "2":
        clientes = listar_clientes()
        for cliente in clientes:
            print(cliente)

    elif opcao == "3":
        atualizar_cliente()

    elif opcao == "4":
        deletar_cliente()

    elif opcao == "0":
        print("Sistema encerrado!")
        break

    else:
        print("Opção inválida!")