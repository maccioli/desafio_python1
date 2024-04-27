import operacoes
import validacao
import tabela_clientes
from colorama import Fore, Style

menu = """

## Bem vindo ao Banco Digital ##

Escolha uma opção:

[c] Cadastrar cliente
[l] Listar clientes
[d] Depositar
[s] Sacar
[e] Extrato
[v] Saldo
[q] Sair

=> """.strip()

while True:

    opcao = input(menu)

    if opcao == "c":
        conta_cliente = validacao.adicionar_nova_conta()
        nome_cliente = input(f"- Digite o nome do cliente: ")
        nascimento_cliente = input("- Digite a data de nascimento (DDMMAAAA): ")
        cpf_cliente = input("- Digite o CPF (apenas números): ")
        validacao.verifica_cpf_existente(cpf_cliente)
        endereco_cliente = input("- Digite o endereço: ")
        saldo_cliente = 0
        extrato_cliente = []
        operacoes.cadastrar(conta_cliente, nome_cliente, nascimento_cliente, cpf_cliente, endereco_cliente, saldo_cliente, extrato_cliente)

    elif opcao == "l":
        print(f"\n")
        tabela_clientes.print_tabela(tabela_clientes.titulo, tabela_clientes.colunas, tabela_clientes.lista)
        print(f"\n")

    elif opcao == "d":
        tipo = "deposito"
        conta_cliente = int(input(f"- Digite a conta para depósito: "))

        if validacao.localiza_conta_cliente(conta_cliente, tipo) == True:
            valor = float(input(f"- Digite o valor a ser depositado: "))
            operacoes.depositar(conta_cliente, valor, tipo)
        else:
            print(f"{Fore.YELLOW}- Reinicie a operação\n {Style.RESET_ALL}")

    elif opcao == "s":
        tipo = "saque"
        conta_cliente = int(input(f"- Digite a conta para saque: "))
        if validacao.localiza_conta_cliente(conta_cliente, tipo) == True:
            valor = float(input(f"\n - Digite valor a ser sacado(Limite 3 saques/dia e R$500,00/saque): "))
            operacoes.sacar(conta_cliente, valor, tipo)
        else:
            print(f"{Fore.YELLOW}- Reinicie a operação\n {Style.RESET_ALL}")

    elif opcao == "e":
        tipo = 'extrato'
        conta_cliente = int(input(f"- Digite a conta: "))
        if validacao.localiza_conta_cliente(conta_cliente, tipo) == True:
            operacoes.ver_extrato(conta_cliente)
        else:
            print(f"{Fore.YELLOW}- Reinicie a operação\n {Style.RESET_ALL}")

    elif opcao == "v":
        tipo = 'saldo'
        conta_cliente = int(input(f"- Digite a conta: "))
        if validacao.localiza_conta_cliente(conta_cliente, tipo) == True:
            operacoes.ver_saldo(conta_cliente)
        else:
            print(f"{Fore.YELLOW}- Reinicie a operação\n {Style.RESET_ALL}")
        
    elif opcao == "q":
        print("\nObrigado por usar o Banco Digital. Até a próxima!\n")
        break

    else:
        print("\nOperação inválida, por favor selecione novamente a operação desejada.\n")