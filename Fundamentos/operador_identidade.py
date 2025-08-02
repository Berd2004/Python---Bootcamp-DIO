#Operador identidade - são usados para comparar se dois objetos ocupam a mesma posição na memória

curso = "curso python"
nome_curso = curso
saldo, limite = 200, 200


print(curso is nome_curso) # o operador "is" verifica se os dois objetos são o mesmo objeto na memória  

print(curso is not nome_curso) # is not indica que as variaveis não ocupam a mesma posição na memória

print(saldo is limite)
