hamburguer = 20.00
cupom_desconto = "dezoff"

while True:
    print(f"Bem vindo ao Galpão Burguer")
    escolha = input(f"Qual lanche você deseja?").lower()
    if escolha == "hamburguer":
        cupom = input("Digite o cumpom de desconto?").lower()
        if cupom == cupom_desconto:
            print(f"O Valor da compra é {hamburguer * 0.90}")
            break
        else:
            print(f"O valor da compra é {hamburguer}")
            break    
    else: 
        print(f"Infelizmente só temos hamburguer")
        

    