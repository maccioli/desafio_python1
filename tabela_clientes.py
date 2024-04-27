import json

def print_tabela(titulo, colunas, lista):

    print(f"{titulo.center(50)}\n")

    for coluna in colunas:
        print(f"{coluna.ljust(20)}", end="")
    print("")

    print("-" * 20 * len(colunas))

    for linha in lista:
        for valor in linha:
            if isinstance(valor, int):
                print(f"{str(valor).ljust(20)}", end="")
            else:
                print(f"{str(valor).ljust(20)}", end="")
        print("")

def reload_dados():
    clientes_dados_arquivo = []
    with open('clientes.json', 'r') as arquivo:
        clientes_dados_arquivo = json.load(arquivo)
    return clientes_dados_arquivo

titulo = "Clientes Banco Digital"
colunas = ["Nome", "Conta", "Saldo"]
dados = []
atualiza_lista_clientes = reload_dados()

def constroi_dados():
    for cliente in atualiza_lista_clientes:
        nome = cliente['nome']
        conta = cliente['conta']
        saldo = cliente['saldo']
        dados.append([nome, conta, saldo])
    return dados

lista = constroi_dados()