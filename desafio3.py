menu = """

[c] Criar usuário
[n] Criar conta
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

usuarios = []

contas = []

def criar_usuario(usuarios):
    nome = input("Informe o nome: ")
    data_nascimento = input("Informe a data de nascimento (dd/mm/yyyy): ")
    cpf = input("Informe o CPF (somente números): ")
    endereco = input("Informe o endereço (logradouro, número - bairro - cidade/estado): ")

    # Verificando se o CPF já está cadastrado
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            print("CPF já cadastrado.")
            return usuarios

    # Criando novo usuário
    novo_usuario = {
        'nome': nome,
        'data_nascimento': data_nascimento,
        'cpf': cpf,
        'endereco': endereco
    }

    # Adicionar novo usuário à lista
    usuarios.append(novo_usuario)
    print("Usuário cadastrado com sucesso.")
    return usuarios

def criar_conta(contas, usuarios):
    agencia = input("Informe a agência: ")
    numero_conta = input("Informe o número da conta: ")
    cpf_usuario = input("Informe o CPF do usuário (somente números): ")

    # verificando se o usuário existe
    usuario = None
    for u in usuarios:
        if u['cpf'] == cpf_usuario:
            usuario = u
            break

    if usuario is None:
        print("Usuário não encontrado.")
        return contas

    # Criar nova conta
    nova_conta = {
        'agencia': agencia,
        'numero_conta': numero_conta,
        'usuario': usuario
    }

    # Adicionar conta a lista
    contas.append(nova_conta)
    print("Conta criada com sucesso.")
    return contas

def depositar(saldo, extrato):
    valor = float(input("Informe o valor do depósito: "))

    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato

def sacar(saldo, extrato, numero_saques, limite, LIMITE_SAQUES):
    valor = float(input("Informe o valor do saque: "))

    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato, numero_saques

def exibir_extrato(saldo, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

while True:
    opcao = input(menu)

    if opcao == "d":
        saldo, extrato = depositar(saldo, extrato)

    elif opcao == "s":
        saldo, extrato, numero_saques = sacar(saldo, extrato, numero_saques, limite, LIMITE_SAQUES)

    elif opcao == "e":
        exibir_extrato(saldo, extrato)

    elif opcao == "c":
        criar_usuario(usuarios)

    elif opcao == "n":
        criar_conta(contas, usuarios)

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
