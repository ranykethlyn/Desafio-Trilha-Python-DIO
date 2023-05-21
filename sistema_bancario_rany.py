# salvar os depositos em uma variavel e exibidos na operação de extrato, tem que constar os 10 depositos
# 3 saques diários limite de 500 cada, limite 1500 por dia, saque armazenado para exibir no extrato

menu = """
MENU

[d] Depositar
[e] Extrato
[s] Sacar
[q] Sair

"""

saldo = 3000
limite_saque = 500
limite_saque_diario = 1500
numero_saques = 0
LIMITE_SAQUES = int(3)
extrato_conta = list()
saldo_float = float(saldo)

while True:
    opcao = input(menu)

    if opcao == "d":
        print("Depósito")
        deposito = int(input("Informe o valor que será depositado: "))
        print("Depósito realizado com sucesso!")
        saldo += deposito
        extrato_conta.insert(0,f"Depósito realizado no valor de R${deposito}")

    elif opcao == "s":
        print("Saque")
        valor_saque = int(input("Informe o valor do saque: "))
        if (valor_saque <= saldo) and (numero_saques < LIMITE_SAQUES) and (valor_saque <= limite_saque):
            print("Retire seu dinheiro na boca do caixa")
            saldo -= valor_saque
            numero_saques += 1
            extrato_conta.insert(0,f"Saque realizado no valor de R${valor_saque}")
        else:
            print("Saque indisponível")
            if valor_saque > saldo:
                print("Saldo insuficiente!")
            elif numero_saques >= LIMITE_SAQUES:
                print("Limite de quantidade de saques diários excedida!")
            else:
                print("Limite de valor de saque diário excedido!")


    elif opcao == "e":
        print("Extrato")
        print(extrato_conta)
        print(f"Saldo atual R${saldo_float}")

    elif opcao == "q":
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada")