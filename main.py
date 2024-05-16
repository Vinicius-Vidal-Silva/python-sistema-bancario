#EXTRATO: Listar todos depósitos e saques e exibir no final o saldo da conta. Formato do dinheiro como R$ XXXX.XX

################################ SISTEMA BANCÁRIO ########################################
#variáveis e constantes
saldo = 10000
deposito = 0
numero_deposito = 0
limite = 500
numero_saque = 0
LIMITE_SAQUE = 3
sair = True
continuar = True
lista_saque = []
lista_deposito = []
menu = """
1 - Deposito
2 - Saque
3 - Extrato
4 - Sair
"""

print("Bem vindo ao banco SouMaisVoce\nO que gostaria de fazer? ")

while sair:
    print(menu)
    opcao = input("Selecione a opcao desejada: ")
    ### realização do depósito e suas funcionalidades
    if opcao == "1":
        while continuar:
            deposito = input("Por favor, entre com o valor do deposito: ")
            deposito_num = int(deposito)
            if deposito_num < 0:
                print("Valor de deposito invalido. Tente novamente!")
            else:
                saldo = saldo + deposito_num
                numero_deposito = numero_deposito + 1
                lista_deposito.append(deposito_num)
                print("Deposito realizado com sucesso!\n")
            try:    
                print("1 - Novo deposito\n2 - Voltar ao menu inicial")
                escolha = input("Escolha a opcao desejada: ")
                escolha_num = int(escolha) #tranformando a entrada em número
                if escolha_num == 2:
                    continuar = False
                elif escolha_num == 1:
                    continuar = True
                else:
                    print("Opcao invalida!")
            except ValueError:
                print("Por favor insíra um número")
        print(f"Saldo atual: R$ {saldo}")
    ##### Realização do saque e condições
    elif opcao == "2":
        for i in range(4):
            controle2 = True
            while controle2:
                if i == LIMITE_SAQUE:
                    print("Limite diario de saques atingido. Tente novamente amanha!")
                    break
                saque = input("Informe a quantidade que deseja sacar: ")
                saque_num = int(saque)
                if saque_num <= 0:
                    print("Valor invalido. Tente novamente!")
                elif saque_num > saldo:
                    print("Saque não realizado.\nMotivo: Valor maior do que saldo disponivel.")
                elif saque_num > 500:
                    print("Saque nao relizado.\nMotivo: Valor maximo ultrapassado.")
                else:
                    saldo = saldo - saque_num
                    numero_saque = numero_saque + 1
                    lista_saque.append(saque_num)
                    print("Saque realizado com sucesso!")
                    controle2 = False
            try:    
                print("1 - Novo saque\n2 - Voltar ao menu inicial")
                escolha = input("Escolha a opcao desejada: ")
                escolha_num = int(escolha) #tranformando a entrada em número
                if escolha_num == 2:
                    break
                elif escolha_num == 1:
                    continue
                else:
                    print("Opcao invalida!")
            except ValueError:
                print("Por favor insíra um número")
        print(f"Saldo atual: R$ {saldo}")
    #EXTRATO e suas funcionalidades
    elif opcao == "3":
        print("**************************************************************************\n")
        print("***********************************EXTRATO********************************\n")
        print(f"Foram realizados: {numero_deposito} deposito(s) no(s) valor(es) de:")
        for dep in lista_deposito:
            print(f"Valor do deposito: R$ {dep}")
        print("\n")
        print(f"Foram realizados: {numero_saque} saque(s) no(s) valor(es) de:")
        for saq in lista_saque:
            print(f"Valor do saque: R$ {saq}")
        print("\n")
        print(f"O saldo atual e de: R$ {saldo}\n")
        print("**************************************************************************")
        print("**************************************************************************\n")
    ##### Sair do menu/programa
    elif opcao == "4":
        controle_saida = True
        while controle_saida:
            print("Tem certeza que deseja sair?\n1 - NAO\n2 - SIM")
            confirmacao = input("Entre com a opcao desejada: ")
            confirmacao_number = int(confirmacao)
            if confirmacao_number == 1:
                sair = True
                controle_saida = False
            elif confirmacao_number == 2:
                print("Saindo...")
                controle_saida = False
                sair = False
            else:
                print("opcao invalida!")
                controle_saida = True
    else:
        print("opcao invalida!")
