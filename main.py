# Yoshi's Bank Software
# Onde o seu dinheiro some em um pulo

menu = """
    [1] Criar usuário
    [2] Criar conta
    [3] Deposito
    [4] Saque
    [5] Extrato
    [6] Sair
    [7] Testar funcao
=> """


def main():
    LIMITE_QNT_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    novo_saldo = 0
    limite_vlr_saque = 500
    numero_saques = 0
    hist_transacoes = []
    lista_usuarios = dict()

    while True:
        opcao = input(menu)

        if opcao == "1":
            cpf = int(input("Digite o CPF:").strip())
            lista_usuarios.update(criar_usuario(aux_cpf=cpf, aux_lista_usuarios=lista_usuarios))

        elif opcao == "2":
            cpf = int(input("Digite o CPF:").strip())
            #TODO  TERMINAR FUNÇÃO DE CRIAR CONTA

            """lista_usuarios.update(criar_conta(aux_lista_usuarios=lista_usuarios, aux_agencia=AGENCIA, aux_saldo=saldo, aux_hist_transacoes))"""

        elif opcao == "3":
            valor_deposito = float(input("Digite o valor que deseja depositar:"))
            saldo, valor, hist_transacoes = depositar(saldo, valor_deposito, hist_transacoes)

        elif opcao == "4":
            valor_saque = float(input("digite o valor que deseja sacar:"))
            saldo, hist_transacoes, numero_saques = sacar(aux_saldo=saldo,
                                                          aux_valor_saque=valor_saque,
                                                          aux_hist_transacoes=hist_transacoes,
                                                          aux_limite_vlr_saque=limite_vlr_saque,
                                                          aux_numero_saques=numero_saques,
                                                          aux_lim_saques=LIMITE_QNT_SAQUES)

        elif opcao == "5":
            extrato(saldo, aux_hist_transacoes=hist_transacoes)

        elif opcao == "6":
            print("Obrigado por utilizar o Yoshi's Bank!")
            print("Até mais!")
            break

        elif opcao == "7":
            print(lista_usuarios.items())
        else:
            print("Opção inválida. Tente novamente!")


def depositar(aux_saldo, aux_valor, aux_hist_transacoes, /):
    if aux_valor > 0:
        aux_saldo += aux_valor
        aux_hist_transacoes.append(aux_valor)
        print("Deposito efetuado com sucesso.")
        print("Saldo atual: R$", aux_saldo)

    else:
        print("Não é possível depositar um valor 0 ou negativo.")
        print("Por favor, repita a operação corretamente")

    return aux_saldo, aux_valor, aux_hist_transacoes


def sacar(*, aux_saldo, aux_valor_saque, aux_hist_transacoes, aux_limite_vlr_saque, aux_numero_saques, aux_lim_saques):
    if (aux_valor_saque > 0) and (aux_valor_saque <= aux_limite_vlr_saque) and (aux_numero_saques < aux_lim_saques):
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

    elif aux_numero_saques >= aux_lim_saques:
        print("Limite de saques diários atingidos")
        print("Por favor, repita a operação no próximo dia útil")

    else:
        print("Não é possível sacar um valor 0 ou negativo.")
        print("Por favor, repita a operação corretamente")

    return aux_saldo, aux_hist_transacoes, aux_numero_saques


def extrato(aux_saldo, /, *, aux_hist_transacoes):
    print("==================Extrato==================")
    for i in range(0, len(aux_hist_transacoes)):
        format_out = "{:.2f}".format(aux_hist_transacoes[i])
        if aux_hist_transacoes[i] > 0:
            print("Deposito: R$", format_out)
        else:
            print(f"Saque: R$", format_out)
    print("===========================================")
    format_out = "{:.2f}".format(aux_saldo)
    print(f"Saldo atual: R$", format_out)


def criar_usuario(*, aux_cpf, aux_lista_usuarios):
    if aux_cpf in aux_lista_usuarios:
        print("CPF já cadastrado na base.")
        print("Por favor verifique os dados e tente novamente!")
        return aux_lista_usuarios
    dados = list()
    dados.append(str(input("Digite o Nome:").strip()))
    dados.append(str(input("Digite a data de nascimento no formato XX/XX/XXXX:").strip()))
    dados.append(str(input("Digite o endereço completo:").strip()))
    aux_lista_usuarios.update({aux_cpf: dados})
    print("Usuário cadastrado com sucesso!")

    return aux_lista_usuarios


def criar_conta(*, aux_lista_usuarios, aux_agencia, aux_conta, aux_saldo, aux_hist_transacoes):
    cpf = int(input("Digite o CPF:").strip())
    if cpf not in aux_lista_usuarios:
        print("Usuário não cadastrado na base.")
        print("Por favor realize o cadastro e tente novamente!")
        return
    aux_lista_usuarios[cpf] = {
        "agencia": aux_agencia,
        "conta": aux_conta,
        "saldo": aux_saldo,
        "extrato": aux_hist_transacoes
    }
    aux_conta += 1
    print("Conta criada com sucesso!")
    return aux_lista_usuarios, aux_conta, aux_saldo, aux_hist_transacoes


main()
