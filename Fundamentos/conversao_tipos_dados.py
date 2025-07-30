# Converter tipo de dados (int --> float etc...)


# inteiro ---> float
inteiro = 20

inteiro_float = float(inteiro)
print(inteiro_float)

# float ---> inteiro

decimal = "15.7"

float_inteiro = (int(float(decimal)))  #tenho que converter a string primeiro para float (na ordem de dentro pra fora - igual casca de cebola), depois para inteiro. a função int() não aceita string com casa decimal diretamente. 

print(float_inteiro)

# Sttring ---> int e float

preco = "10.50"
idade = "14"

print(float(preco))

print(int(idade))

print(type(int(idade)))


# int ---> string

print(type(str(10))) #str(),é o conversor de string