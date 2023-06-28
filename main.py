# Yoshi's Bank Software
# Onde o seu dinheiro some em um pulo

menu = """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
=> """

saldo = 0
limite_vlr_saque = 500
extrato = ""
numero_saques = 0
LIMITE_QNT_SAQUES = 3
hist_transacoes = []


def depositar():
    global saldo
    valor = float(input("Digite o valor que deseja depositar:"))
    if valor > 0:
        saldo += valor
        hist_transacoes.append(valor)
        print("Deposito efetuado com sucesso.")
        print("Saldo atual: R$", saldo)

    else:
        print("Não é possível depositar um valor 0 ou negativo.")
        print("Por favor, repita a operação corretamente")


def sacar(aux_saldo, aux_valor_saque, aux_hist_transacoes, aux_limite_vlr_saque, aux_numero_saques, aux_limite_saques):
    if (aux_valor_saque > 0) and (aux_valor_saque < aux_limite_vlr_saque) and (aux_numero_saques < aux_limite_saques):
        if aux_valor_saque <= aux_saldo:
            aux_saldo -= aux_valor_saque
            aux_valor_saque *= -1
            aux_hist_transacoes.append(aux_valor_saque)
            aux_numero_saques += 1
            print("Saque efetuado com sucesso.")
            print("Saldo atual: R$", aux_saldo)
        else:
            print("Saldo insuficiente para realizar o saque.")
            print("Saldo atual: R$", aux_saldo)

    elif aux_valor_saque > aux_limite_vlr_saque:
        print("Valor desejado maior do que o limite diário de R$ 500.00")
        print("Por favor, repita a operação corretamente")

    elif aux_numero_saques >= aux_limite_saques:
        print("Limite de saques diários atingidos")
        print("Por favor, repita a operação no próximo dia útil")

    else:
        print("Não é possível sacar um valor 0 ou negativo.")
        print("Por favor, repita a operação corretamente")
    return aux_saldo, aux_hist_transacoes, aux_numero_saques


def extrato():
    global hist_transacoes, saldo
    print("==================Extrato==================")
    for i in range(0, len(hist_transacoes)):
        format_out = "{:.2f}".format(hist_transacoes[i])
        if hist_transacoes[i] > 0:
            print("Deposito: R$", format_out)
        else:
            print(f"Saque: R$", format_out)
    print("===========================================")
    format_out = "{:.2f}".format(saldo)
    print(f"Saldo atual: R$", format_out)


while True:
    opcao = input(menu)

    if opcao == "d":
        depositar()

    elif opcao == "s":
        valor_saque = float(input("digite o valor que deseja sacar:"))
        sacar(aux_saldo=saldo, aux_valor_saque=valor_saque,
              aux_hist_transacoes=hist_transacoes, aux_limite_vlr_saque=limite_vlr_saque,
              aux_numero_saques=numero_saques, aux_limite_saques=LIMITE_QNT_SAQUES)

    elif opcao == "e":
        extrato()

    elif opcao == "q":
        print("Obrigado por utilizar o Yoshi's Bank!")
        print("Até mais!")
        break
    else:
        print("Opção inválida. Tente novamente!")