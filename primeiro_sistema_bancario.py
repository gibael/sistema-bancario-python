#Meu nome é Afelion e esse é o primeiro Sistema Bancario, deixarei algumas descrições como nota mental para estudo pessoal.

menu = """ 
[a] Depositar
[s] Sacar
[d] Extrato
[f] Sair

=>""" #optei pelo menu no começo por ser o metodo que me foi ensinado a deixar o código limpo

menu_saque = """
Opções de saque:                        
[a] 50 reais
[s] 100 reais
[d] outros valores
[f] sair

=>""" #o menu do saque também

#Variaveis
saldo = 0 
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3 


while True: #codigo de repetição

    opcao = input (menu) #dando valor a "opcao" e execução do prompt do menu

    if opcao == "a": 
        valor = float(input("Qual valor deseja depositar? ")) #ativar "float" no prompt permite guardar dados numéricos com parte decimal (o que vem depois da vírgula)
        
        if valor > 0: #importante o "valor" ser maior que 0, para não ocorrer passar numeros negativos ex: -20
            saldo += valor #o "valor" sendo acrescentado no SALDO
            extrato += f"{valor:.2f}\n" #valor sendo acrescentado no EXTRATO (IMPORTANTE) concatenar com f-String o "valor" formatado(:.2f)
            print(f"Você depositou R$ {valor:.2f}\n") #string mostrada no Terminal para o "cliente"

        else: print("Operação inválida, por favor selecione novamente a operação desejada.")

    elif opcao == "s":
        opcao_saque = input(menu_saque)
        
        saque_excedido = numero_saques >= LIMITE_SAQUES #adicionando limite no saque
        saque50 = 50.00
        saque100 = 100.00
       
        if opcao_saque == "a":

            limite_excedido = saque50 > limite
            saldo_insuficiente = saque50 > saldo

            if saldo_insuficiente: #IMPORTANTE PRIMEIRO VERIFICAR O SALDO E DEIXAR POR ULTIMO O SAQUE, CASO CONTRARIO PODERA SACAR INFINITAMENTE
                print("Saldo insuficiente! escolha outra opção: ")

            elif limite_excedido:
                print("Limite excedido! escolha outra opção: ")

            elif saque_excedido:
                print("Seu saque diário foi excedido! escolha outra opção: ")

            elif saldo > 50:
                saldo -= saque50 #Mudamos "+" para "-" para que seja descontado do saldo
                extrato += f"{saque50:.2f}\n"
                numero_saques += 1 #Sempre que ativar essa opção sera acrescentado 1 ao numero de saque
                print("Você sacou 50 reais, retire o dinheiro na boca do caixa.")
            
            else: 
                print("Saldo Insuficiente! escolha outra opção: ")
        
        elif opcao_saque == "s":
            
            limite_excedido = saque100 > limite
            saldo_insuficiente = saque100 > saldo

            
            if saldo_insuficiente: #IMPORTANTE PRIMEIRO VERIFICAR O SALDO E DEIXAR POR ULTIMO O SAQUE, CASO CONTRARIO PODERA SACAR INFINITAMENTE
                print("Saldo insuficiente! escolha outra opção: ")

            elif limite_excedido:
                print("Limite excedido! escolha outra opção: ")

            elif saque_excedido:
                print("Seu saque diário foi excedido! escolha outra opção: ")

            elif saldo > 100:
                saldo -= saque100 #Mudamos "+" para "-" para que seja descontado do saldo
                extrato += f"{saque100:.2f}\n"
                numero_saques += 1 #Sempre que ativar essa opção sera acrescentado 1 ao numero de saque
                print("Você sacou 100 reais, retire o dinheiro na boca do caixa.")
            
            else: 
                print("Saldo Insuficiente! escolha outra opção: ")
        
        elif opcao_saque == "d":
            valor = float(input("Qual valor deseja sacar?: "))
        
            limite_excedido = valor > limite
            saldo_insuficiente = valor > saldo
            
            if saldo_insuficiente: #IMPORTANTE PRIMEIRO VERIFICAR O SALDO E DEIXAR POR ULTIMO O SAQUE, CASO CONTRARIO PODERA SACAR INFINITAMENTE
                print("Saldo insuficiente! escolha outra opção: ")

            elif limite_excedido:
                print("Limite excedido! escolha outra opção: ")
            

            elif saque_excedido:
                print("Seu saque diário foi excedido! escolha outra opção: ")

            elif valor > 0:
                saldo -= valor #Mudamos "+" para "-" para que seja descontado do saldo
                extrato += f"{valor:.2f}\n"
                numero_saques += 1 #Sempre que ativar essa opção sera acrescentado 1 ao numero de saque
                print(f"Você sacou R$ {valor:.2f}\n")

            
            else: 
                print("Operação inválida, por favor selecione novamente a operação desejada.")

        elif opcao_saque == "f":
            print("Obrigado volte sempre!")
            break 
        
        else: 
            print("Operação inválida, por favor selecione novamente a operação desejada.")
    
    elif opcao == "d":
        print("~~~~~~~~~~~~~~Extrato~~~~~~~~~~~~~~")
        print("Não houve movimentações em sua conta." if not extrato else extrato) #A variavel "extrato" está vazio, então apareceça a msg "Não houve mov..."
        print(f"\nSaldo: R$ {saldo:.2f}")                                          #Quando o "extrato" for preenchido por movimentações, ele mostratará o "extrato"
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    elif opcao == "f":
        print("Obrigado por usar Afelion's Bank")
        break

    else: 
        print("Operação inválida, por favor selecione novamente a operação desejada.")



#FIM. AFELION'S BANK OUT.