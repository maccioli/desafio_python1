import clientesDB
from colorama import Fore, Style

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
            print("\n - Ja existe um cadastro com este CPF\n")
            cpf_cliente = input("- Digite o CPF (apenas números): ")

def localiza_conta_cliente(conta_cliente, tipo):
    
    for cliente in clientesDB.cliente_banco:
        
        if cliente['conta'] == conta_cliente:
            print(f"{tipo} na conta de {cliente['nome']}\n")
            resposta = input(" confirma?(s/n)")
            if resposta == "s":
                return True
            else:
                return False
    
    print(f"\n - {Fore.RED}Conta não encontrada\n {Style.RESET_ALL}")
    return False
    