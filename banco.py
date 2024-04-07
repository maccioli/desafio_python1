menu = """

## Bem vindo ao Banco Digital ##

Escolha uma opção:

[d] Depositar
[s] Sacar
[e] Extrato
[v] Saldo
[q] Sair

=> """.strip()

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)


    if opcao == "d":
        valor = float(input(f"Digite o valor a ser depositado: "))
        saldo += valor
        extrato += f"Deposito: R${valor:.2f}\n" 
        print(f"Saldo atual: {saldo:.2f}")


    elif opcao == "s":
        valor = float(input(f"Digite valor a ser sacado(Limite 3 saques/dia e R$500,00/saque): "))

        if saldo >= valor and valor > 0 and valor <= limite and numero_saques <= LIMITE_SAQUES:
            saldo = saldo - valor
            extrato += f"Saque: {valor:.2f}\n"
            print(f"Saldo atual: {saldo:.2f}")

        else:
            print("Saque não permitivo, verifique o valor digitado, saldo ou limite de saques.")


    if opcao == "e":
        print(f"Extrato: \n{extrato}\n")


    if opcao == "v":
        print(f"Seu saldo é de: {saldo:.2f}")

        
    elif opcao == "q":
        print("Obrigado por usar o Banco Digital. Até a próxima!")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")