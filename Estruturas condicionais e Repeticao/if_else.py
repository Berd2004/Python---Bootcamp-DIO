# IDADE = int(input("Digite sua idade: "))
# NOME = input("Informe seu nome: ")


# if (IDADE > 18):
#     print(f'{NOME}, parabéns!!! aprovado para tirar sua CNH')
    
# else:
#     print("Reprovado para tirar a CNH - idade minima: 18 anos")    

import time
import sys

valor_conta = float(input("informe o valor disponível em conta: "))
opcao = int(input("\n [1] SACAR \n [2] Extrato \n Informe uma opção: "))

if opcao == 1:
    valor_saque = float(input("Informe a quantia para o saque: "))
    if valor_saque > valor_conta:  
        print("Operação inválida! Não é possivel sacar mais do que o valor dispovível em conta. tente novamente!")
    else: 
        calculo_saque = (valor_conta - valor_saque)   
        print("--------------------------------------- \n")
        print(f"Saque Realizado com sucesso!\n valor do seu extrato atualizado é: {calculo_saque}")
      
elif opcao == 2:    #elif - é a combinação de else + if. Testa outra condição, caso a anterior não seja atendida
    print("Exibindo o extrato....\n")
    time.sleep(2)  
    print("extrato") 
    
    
else:               #caso nenhuma condição seja atendida, ele age como exceção
    sys.exit("opção inválida!!!")     
    
    