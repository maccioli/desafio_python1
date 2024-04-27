import clientesDB

def cadastrar(conta_cliente, nome_cliente, nascimento_cliente, cpf_cliente, endereco_cliente, saldo_cliente, extrato_cliente):
        cliente = {"conta": conta_cliente, "nome": nome_cliente, "nascimento": nascimento_cliente, "cpf": cpf_cliente, "endereco": endereco_cliente, "saldo": saldo_cliente, "extrato": extrato_cliente}
        clientesDB.adicionar_cliente(cliente)

def depositar(conta_cliente, valor, tipo):
    for cliente in clientesDB.cliente_banco:
        if cliente['conta'] == conta_cliente:
            saldo_cliente = cliente['saldo']
            saldo_cliente += valor
            cliente['saldo'] = saldo_cliente
            
            transacao = {"tipo": tipo, "valor": valor}
            cliente['extrato'].append(transacao)
            
            clientesDB.salvar_clientes(clientesDB.cliente_banco)
            print(f"\n - Depósito de R${valor:.2f} realizado com sucesso para {cliente['nome']}.\n")

def sacar(conta_cliente, valor, tipo):
    for cliente in clientesDB.cliente_banco:
        if cliente['conta'] == conta_cliente:
            if cliente['saldo'] >= valor and valor > 0 and valor <= clientesDB.limite and clientesDB.numero_saques <= clientesDB.LIMITE_SAQUES:
                saldo_cliente = cliente['saldo']
                saldo_cliente -= valor
                cliente['saldo'] = saldo_cliente

                transacao = {"tipo": tipo, "valor": valor}
                cliente['extrato'].append(transacao)    
                print(f"\n - Saque de {cliente['nome']} no valor de R${valor:.2f} realizado com sucesso.\n")            
            else:
                print("\n - Saque não permitivo, verifique o valor digitado, saldo ou limite de saques.\n")

    clientesDB.salvar_clientes(clientesDB.cliente_banco)

def ver_extrato(conta_cliente):
    for cliente in clientesDB.cliente_banco:
        if cliente['conta'] == conta_cliente:
            print(f"\n{cliente['conta']}\n{cliente['nome']}\nExtrato: \n{cliente['extrato']}\n")

def ver_saldo(conta_cliente):
    for cliente in clientesDB.cliente_banco:
        if cliente['conta'] == conta_cliente:
            print(f"\n - O saldo de {cliente['nome']} é de: {cliente['saldo']:.2f}\n")