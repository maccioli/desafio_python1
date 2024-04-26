import operacoes
import validacao

menu = """

## Bem vindo ao Banco Digital ##

Escolha uma opção:

[t] teste
[l] Listar clientes
[c] Cadastrar cliente
[d] Depositar
[s] Sacar
[e] Extrato
[v] Saldo
[q] Sair

=> """.strip()

while True:

    opcao = input(menu)

    if opcao =="t":
        print(validacao.adicionar_nova_conta())

    if opcao =="l":
        validacao.listar_clientes();

    if opcao == "c":
        conta_cliente = validacao.adicionar_nova_conta()
        nome_cliente = input(f"Digite o nome do cliente: ")
        nascimento_cliente = input("Digite a data de nascimento (DDMMAAAA): ")
        cpf_cliente = input("Digite o CPF (apenas números): ")
        validacao.verifica_cpf_existente(cpf_cliente)
        endereco_cliente = input("Digite o endereço: ")
        saldo_cliente = 0
        extrato_cliente = []
        operacoes.cadastrar(conta_cliente, nome_cliente, nascimento_cliente, cpf_cliente, endereco_cliente, saldo_cliente, extrato_cliente)


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