menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[v] Saldo
[q] Sair

=> """

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
        print(f"Saldo atual: {saldo}")

    elif opcao == "s":
        valor = float(input(f"Digite valor a ser sacado(Limite R$500,00): "))

        if saldo >= valor and valor > 0:
            saldo = saldo - valor
            print(f"Saldo atual: {saldo}")

        else:
            print("Valor não permitivo.")

    if opcao == "v":
        print(f"Seu saldo é de: {saldo}")

        
    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")