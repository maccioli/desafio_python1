import operacoes

menu = """

## Bem vindo ao Banco Digital ##

Escolha uma opção:

[c] Cadastrar cliente
[d] Depositar
[s] Sacar
[e] Extrato
[v] Saldo
[q] Sair

=> """.strip()

while True:

    opcao = input(menu)

    if opcao == "c":
        nome_cliente = input(f"Digite o nome do cliente: ")
        nascimento_cliente = input("Digite a data de nascimento (DDMMAAAA): ")
        cpf_cliente = input("Digite o CPF (apenas números): ")
        endereco_cliente = input("Digite o endereço: ")
        cliente = {"nome": nome_cliente, "nascimento": nascimento_cliente, "cpf": cpf_cliente, "endereco": endereco_cliente}
        operacoes.clientesDB.adicionar_cliente(cliente)


    if opcao == "d":
        valor = float(input(f"Digite o valor a ser depositado: "))
        operacoes.depositar(valor)


    elif opcao == "s":
        valor = float(input(f"Digite valor a ser sacado(Limite 3 saques/dia e R$500,00/saque): "))
        operacoes.sacar(valor)

    if opcao == "e":
        operacoes.ver_extrato()

    if opcao == "v":
        operacoes.ver_saldo()
        
    elif opcao == "q":
        print("Obrigado por usar o Banco Digital. Até a próxima!")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")