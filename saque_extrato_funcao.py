def menu():
    menu= """ 
    [d] deposito
    [s] saque
    [e] extrato
    [nc] nova conta
    [nu] novo usuario
    [lc] lista de contasd
    [q] sair
    """
    return input(menu)

def deposito(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"deposito de R${valor:.2f}\n"
                
    else:
        print("valor invalido, tente novamente!!")
        
    return(saldo, extrato)

def saque(*,saldo, valor, extrato,limite, numero_saques, limite_saques):
    
    exedeu_saldo = valor > saldo
            
    exedeu_limite = valor > limite
            
    exedeu_saque = numero_saques >= limite_saques
            
    if exedeu_saldo:
        print("saldo exedido!! tente novamente!")
            
    elif exedeu_limite:
        print("limite exedido! tente novamente!")
                
    elif exedeu_saque:
        print("limite de saques diarios exedido!")
                
    elif valor > 0:
        saldo -= valor
        extrato += f"saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print(f"saque realizado com sucesso!")
                
    else:
        print("valor invalido! tente novamente!")
    return(saldo, extrato)

def exibir_extrato(saldo,/,*,extrato):
    
    print('{:=^40}'.format("EXTRATO"))
    print("Não foram realizadas movimentações."if not extrato else extrato)
    print(f"\nSaldo: R${saldo:.2f}")
    print('=' * 40)

def criar_usuario(usuarios):
    cpf = input("informe o cpf (somente numeros!)")
    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        print("esse usuario ja existe!!")
        return
    nome = input("insira o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
    
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    
    print("usuario criado com sucesso!!")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:{conta['agencia']}
            C/C:{conta['numero_conta']}
            Titular:{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(linha)
def main():
    
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []
    LIMITE_SAQUES = 3
    AGENCIA ="0033"


    while True:
        opcao = menu()
        
        if opcao == "d":
            valor = float(input("qual valor deseja depositar?  R$"))
            saldo, extrato = deposito(saldo, valor, extrato)        
            
        elif opcao == "s":
            valor = float(input("informe o valor do saque desejado!! R$"))
            saldo, extrato = saque(saldo=saldo, valor=valor, extrato=extrato,limite=limite, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES)
                          
        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)
            
        elif opcao == "nu":
            criar_usuario(usuarios)
        
        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)
        elif opcao == "lc":
            listar_contas(contas)    
        elif opcao == "q":
            break
        
        else:
            print("operação invalida, tente novamente!")
            
    print("Obrigado pela preferencia!!")

main()