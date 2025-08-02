## Operadores de associação - são usados para verificar se um objeto está contido em outro objeto, como listas, tuplas, strings, etc.

curso = "curso Python"
frutas = ["maça", "banana", "laranja", "abacate"]

print("Python" in curso)  # verifica se a string "Python" está contida na variável curso

print("abacate" not in frutas)  # verifica se "abacate" não está na lista de frutas

if ("maça" and "banana" in frutas):
    print("Maça e banana estão presentes na lista de frutas!")
    
else:

    print("Não estão")