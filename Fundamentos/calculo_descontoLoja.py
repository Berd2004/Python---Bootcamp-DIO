# Dicionário com os valores de desconto
descontos = {
    "DESCONTO10": 0.10,
    "DESCONTO20": 0.20,
    "SEM_DESCONTO": 0.00
}

# Entrada do usuário
preco = 100
cupom = "DESCONTO10"

# TODO: Aplique o desconto se o cupom for válido:

if cupom == "DESCONTO10":
    desconto_produto = preco * descontos["DESCONTO10"]
    valor_final = preco - desconto_produto
    print(f"{valor_final:.2f}")
elif cupom == "DESCONTO20":
    desconto_produto = preco * descontos["DESCONTO20"]
    valor_final = preco - desconto_produto
    print(f"{valor_final:.2f}")
elif cupom == "SEM_DESCONTO":
    valor_final = preco
    print(f"{valor_final:.2f}")
else:
    print("Cupom inválido.")
    
    
    # Entrada do usuário
preco = 100
cupom = "DESCONTO20"

# TODO: Aplique o desconto se o cupom for válido:

if cupom == "DESCONTO20":
    desconto_produto = preco * descontos["DESCONTO20"]
    valor_final = preco - desconto_produto
    print(f"{valor_final:.2f}")
elif cupom == "DESCONTO20":
    desconto_produto = preco * descontos["DESCONTO20"]
    valor_final = preco - desconto_produto
    print(f"{valor_final:.2f}")
elif cupom == "SEM_DESCONTO":
    valor_final = preco
    print(f"{valor_final:.2f}")
else:
    print("Cupom inválido.")
    

    
    # Entrada do usuário
preco = 100
cupom = "SEM_DESCONTO"

# TODO: Aplique o desconto se o cupom for válido:

if cupom == "SEM_DESCONTO":
    desconto_produto = preco * descontos["SEM_DESCONTO"]
    valor_final = preco - desconto_produto
    print(f"{valor_final:.2f}")
elif cupom == "SEM_DESCONTO":
    desconto_produto = preco * descontos["SEM_DESCONTO"]
    valor_final = preco - desconto_produto
    print(f"{valor_final:.2f}")
elif cupom == "SEM_DESCONTO":
    valor_final = preco
    print(f"{valor_final:.2f}")
else:
    print("Cupom inválido.")
    

