import json
import os

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

def carregar_clientes():
    if not os.path.exists("clientes.json"):
        with open("clientes.json", "w") as arquivo:
            json.dump([], arquivo)
    try:
        with open("clientes.json", "r") as arquivo:
            return json.load(arquivo)
    except json.decoder.JSONDecodeError:
        return []

def salvar_clientes(clientes):
    with open("clientes.json", "w") as arquivo:
        json.dump(clientes, arquivo)

def adicionar_cliente(cliente):
    cliente_banco.append(cliente)
    salvar_clientes(cliente_banco)

cliente_banco = carregar_clientes()