import clientesDB

def cadastrar(conta_cliente, nome_cliente, nascimento_cliente, cpf_cliente, endereco_cliente, saldo_cliente, extrato_cliente):
        cliente = {"conta": conta_cliente, "nome": nome_cliente, "nascimento": nascimento_cliente, "cpf": cpf_cliente, "endereco": endereco_cliente, "saldo": saldo_cliente, "extrato": extrato_cliente}
        clientesDB.adicionar_cliente(cliente)

def depositar(valor):
        clientesDB.saldo += valor
        clientesDB.extrato += f"Deposito: R${valor:.2f}\n" 
        print(f"Saldo atual: {clientesDB.saldo:.2f}")

def sacar(valor):
        if clientesDB.saldo >= valor and valor > 0 and valor <= clientesDB.limite and clientesDB.numero_saques <= clientesDB.LIMITE_SAQUES:
            clientesDB.saldo = clientesDB.saldo - valor
            clientesDB.extrato += f"Saque: {valor:.2f}\n"
            print(f"Saldo atual: {clientesDB.saldo:.2f}")
        else:
            print("Saque não permitivo, verifique o valor digitado, saldo ou limite de saques.")

def ver_extrato():
    print(f"Extrato: \n{clientesDB.extrato}\n")

def ver_saldo():
    print(f"Seu saldo é de: {clientesDB.saldo:.2f}")