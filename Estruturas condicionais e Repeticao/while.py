

#* COMANDO WHILE


entrada = 1

while entrada != 0:    #! Executa enquanto a condição for atendida (não tem um número fixo de repetições, é variado - diferente do for que é fixo!)
    opcao = int(input("[2] Sacar \n [1] Extrato \n [0] Sair"))
    
    if opcao == 2:
        print("Sacando...")
    
    elif opcao == 1:
        print("Exibindo o extrato....")
        
    elif opcao == 0:   #? Nesse caso, se a condição foi atendida , ela irá executar o break, encerrando, portanto o loop
        print("Encerrando transação....")
        break;        #! é o comando que para o laço quando determinada condição é alcançada