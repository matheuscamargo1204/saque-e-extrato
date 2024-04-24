menu = """ 
[d] deposito
[s] saque
[e] extrato
[q] sair
"""
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3


while True:
    opcao = input(menu)
    
    if opcao == "d":
       valor = float(input("qual valor deseja depositar?  R$"))
       
       if valor > 0:
           saldo += valor
           extrato += f"deposito de R${valor:.2f}\n"
           
       else:
           print("valor invalido, tente novamente!!")
           
    elif opcao == "s":
        valor = float(input("informe o valor do saque desejado!! R$"))
        
        exedeu_saldo = valor > saldo
        
        exedeu_limite = valor > limite
        
        exedeu_saque = numero_saques >= LIMITE_SAQUES
        
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
            
    elif opcao == "e":
        print('{:=^40}'.format("EXTRATO"))
        print("Não foram realizadas movimentações."if not extrato else extrato)
        print(f"\nSaldo: R${saldo:.2f}")
        print('=' * 40)
        
    elif opcao == "q":
        break
    
    else:
        print("operação invalida, tente novamente!")
        
print("Obrigado pela preferencia!!")