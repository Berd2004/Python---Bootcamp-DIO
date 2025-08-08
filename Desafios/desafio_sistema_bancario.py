import time

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3


while True:
    opcao = input("Digite a operação que deseja realizar: \n [d] Depositar \n [s] Sacar \n [e] Extrato \n [q] Sair \n \n ---->")

    
    if opcao == "d":
        deposito = float(input("Digite o valor que deseja depositar: "))
        saldo += deposito
        extrato += f"Depósito: R$ {deposito:.2f}\n"
        
    
    elif opcao == "s":
        saque = float(input("Digite o valor do saque: "))
        
        excedeu_saques = numero_saques >= LIMITE_SAQUES
        
        if saque > limite :
            print("Seu valor excede o limite de R$500. Tente Novamente!")
            
        elif excedeu_saques:
            print("Seu limite de 3 saques diários foi excedido") 
               
        elif saque > saldo:
            print("Não é possivel sacar mais do que o seu saldo!")    
                  
        elif saque > 0:
            saldo -= saque
            numero_saques += 1
            extrato += f"Saque: R$ {saque:.2f}\n"
            
        else:
            print("Valor inválido para saque!")    
            
    elif opcao == "e":
        
        print("-----------------Extrato-------------------- \n")
        
        if not extrato:
            print("Não foram realizadas movimentações.")
        else:
            print(extrato) 
            
        print(f"O seu saldo é: {saldo:.2f} \n") 
        print(f"Você realizou {numero_saques} saques")
        print("--------------------------------------------")
        
    elif opcao == "q":
        print("-----------------Extrato-------------------- \n")
        if not extrato:
            print("Não foram realizadas movimentações.")
            
        else:
            print(extrato)    
        print(f"O seu saldo é: {saldo:.2f} \n reais") 
        print(f"Você realizou {numero_saques} saques")
        print("--------------------------------------------")
        
        break;
    
    
    else:
        print("opção inválida")
    
    
    





