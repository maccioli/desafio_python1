import json

def verifica_conta():
    with open('clientes.json', 'r') as arquivo:
        dados_clientes = json.load(arquivo)
    
    for cliente in dados_clientes:
        print(f"Conta: {cliente['conta']} Cliente: {cliente['nome']}\n")
