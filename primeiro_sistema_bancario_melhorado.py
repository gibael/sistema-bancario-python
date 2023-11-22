import textwrap

def menu(): 
    menu_text = """ 
~~~~~~~~~~~~~~ MENU ~~~~~~~~~~~~~~
[a]\tDepositar
[s]\tSacar
[d]\tExtrato
[c]\tNovo Usuário
[z]\tCriar Conta
[x]\tListar Contas
[f]\tSair

=> """
    return input(textwrap.dedent(menu_text))

def menu_saque():
    menu_saque_text = """
Opções de saque:                        
[a]\t50 reais
[s]\t100 reais
[d]\toutros valores
[f]\tsair

=>"""
    return input(textwrap.dedent(menu_saque_text))

def depositar(saldo, valor, extrato): 
    if valor > 0: 
        saldo += valor 
        extrato += f"Depósito:\t{valor:.2f}\n"
        print(f"Você depositou R$ {valor:.2f}\n") 
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")

    return saldo, extrato

def sacar(saldo, valor, extrato, limite, numero_saques, limite_saques): 
    limite_excedido = valor > limite
    saldo_insuficiente = valor > saldo
    saque_excedido = numero_saques >= limite_saques
                
    if saldo_insuficiente: 
        print("Saldo insuficiente! Escolha outra opção: ")

    elif limite_excedido:
        print("Limite excedido! Escolha outra opção: ")
                
    elif saque_excedido:
        print("Seu saque diário foi excedido! Escolha outra opção: ")

    elif valor > 0:
        saldo -= valor 
        extrato += f"Saque:\t{valor:.2f}\n" 
        numero_saques += 1 
        print(f"Você sacou R$ {valor:.2f}\n")

    else: 
        print("Operação inválida, por favor selecione novamente a operação desejada.")

    return saldo, extrato

def exibir_extrato(saldo, extrato):
    print("~~~~~~~~~~~~~~ Extrato ~~~~~~~~~~~~~~")
    print("Não houve movimentações em sua conta." if not extrato else extrato)
    print(f"Saldo: R$ {saldo:.2f}")                                         
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

def novo_usuario(usuarios):
    cpf = float(input("Informe o CPF (somente número): "))
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n Já existe usuário com esse CPF!")
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = float(input("Informe a data de nascimento (dd-mm-aaaa): "))
    endereco = input("Informe o endereço (logradouro, nº - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("Usuário criado com sucesso!")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def nova_conta(agencia, numero_conta, usuarios):
    cpf = float(input("Informe o CPF do usuário: "))
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nConta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\nUsuário não encontrado!")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t {conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    
    saldo = 0 
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "a": 
            valor = float(input("Qual valor deseja depositar? "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            opcao_saque = menu_saque()
            
            if opcao_saque == "a":
                valor_saque = 50.00

            elif opcao_saque == "s":
                valor_saque = 100.00

            elif opcao_saque == "d":
                valor_saque = float(input("Qual valor deseja sacar? "))
            
            elif opcao_saque == "f":
                print("Obrigado por usar Afelion's Bank")
                break 
            
            else: 
                print("Operação inválida, por favor selecione novamente a operação desejada.")

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor_saque,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "d":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "c":
            novo_usuario(usuarios)

        elif opcao == "z":
            numero_conta = len(contas) + 1
            conta = nova_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "x":
            listar_contas(contas)

        elif opcao == "f":
            print("Obrigado por usar Afelion's Bank")
            break

        else: 
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main()
