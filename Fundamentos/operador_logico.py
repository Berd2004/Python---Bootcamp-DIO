#Operadores lógicos

saldo = 1000
saque = 200
limite = 100

#operador and (e)
print(saldo >= saque and saque <= limite)  # se as 2 expressões (antes e depois do operador and) forem verdadeiras a expressão é verdadeira


##Operador Or (ou)

print(saldo >= saque or saque <= limite) # se 1 das expressões forem verdadeiras então a saída será verdadeira


## Operador not (negação)

saldo = 99
saque = 100

print(not saldo < saque) #o operador "not" sempre vai ser o contrario da condição expressão. Se a condção for true, ele mudara para falso. sempre negando a condição

#Nesse caso a expressão (saldo < saque) é verdadeira (true), porém o not antes da expressão nega essa condição verdadeira, transformando-a em falsa (false)