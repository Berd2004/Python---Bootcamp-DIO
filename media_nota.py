n1 = float(input("Digite a primeira nota: "))

n2 = float(input("Digite a segunda nota: "))



MediaNotas = (n1 + n2) /2

print("A média das notas é: ", MediaNotas)

if (MediaNotas >=6):
    print ("Parabéns, você foi aprovado!")
    
elif (MediaNotas >= 8):
    print ("Parabéns, você foi aprovado com louvor!")
    
else:
    print ("Infelizmente você foi reprovado, estude mais e tente novamente!")
