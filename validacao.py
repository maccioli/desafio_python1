import clientesDB

def listar_clientes():
    
    for cliente in clientesDB.cliente_banco:
        print(f"Conta: {cliente['conta']} Cliente: {cliente['nome']}\n")

def adicionar_nova_conta():
    quantidade_clientes = len(clientesDB.cliente_banco)

    if quantidade_clientes < 1:
        return 1
    else:
        return len(clientesDB.cliente_banco) + 1 
    
def verifica_cpf_existente(cpf_cliente):
    for cliente in clientesDB.cliente_banco:

        while cliente['cpf'] == cpf_cliente:
            print("Ja existe um cadastro com este CPF")
            cpf_cliente = input("Digite o CPF (apenas números): ")