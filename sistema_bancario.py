#criar um sistema bancário com saque, depósito e visualização de extrato
#somente um usuário

#usuário escolhe a opção
#MENU

print("Seja bem-vindo ao nosso banco")

saldo = 0
limite_vlr_saque = float(500)
limite_qtd_saque = 3    
extrato = ""
qtd_diaria_saques = 0


while True:
    menu = input("""
                
        O que você deseja fazer?
                
        d) depositar
        s) sacar
        e) ver extrato
        q) sair
                    
    """)

    # SAQUE
    if menu == "s":
        print("SAQUE")
        vlr_saque = float(input("Qual o valor que você quer sacar?  R$"))
        if qtd_diaria_saques >= 3:
            print("Você atingiu o número máximo de saques diários, por favor volte amanhã.")
        elif vlr_saque > 500 or vlr_saque > saldo:
            print("Você não pode efetuar essa transação pois não tem saldo ou está tentando transferir um valor acima do seu limite.")
        else:
            saldo -= vlr_saque
            print(f"Você sacou R${vlr_saque}. O seu saldo restante é de {saldo}")
            extrato += f"* Saque ({vlr_saque})\n"
            qtd_diaria_saques = qtd_diaria_saques + 1
        continue

    # DEPÓSITO
    elif menu == "d":
        print("DEPÓSITO")
        vlr_deposito = int(input("Quanto você quer depositar?"))
        if vlr_deposito < 0:
            print("você não pode depositar um valor negativo")
        else:
            saldo += vlr_deposito
            print(f'Depósito de R${vlr_deposito} feito. Seu novo saldo é: R${saldo}')
            extrato += f"* Depósito de {vlr_deposito} reais\n"
        continue

    # EXTRATO
    elif menu == "e":
        print("===========EXTRATO===========")
        if extrato == "":
            print("Seu extrato está vazio")
        else:
            print(extrato)
            print(f"Saldo atual: R${saldo}")
        continue

    # SAIR
    elif menu == "q":
        print("Obrigado por usar a nossa solução")
        break

    # ENTRADA INVÁLIDA
    else:
        print("Por favor, insira um valor válido.")
