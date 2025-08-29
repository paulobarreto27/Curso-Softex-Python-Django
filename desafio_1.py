"""

Comércio Padaria
1-0 programa tem que rodar em loop infinito até ser parado
2-Cliente pedir um tipo de pão (Frânces, Doce, Forma, Australiano)
3-Cada pão terá uma quantidade
4-Valor do pão
5-Pedir forma de pagamento (Dinheiro, Cartão)
6-Forma de entrega
7-Dados do cliente (se for entregar)
8-Valor do frete por bairro
9-Nome do atendente
10- Código da entrega


"""
# Nome dos Pães
nome_frances = "frances"
nome_doce = "doce"
nome_forma = "forma"

# Valores dos pães
valor_frances = 0.50
valor_doce = 5.00
valor_forma = 5.99

# Estoque de pães
quantidade_frances = 15
quantidade_doce = 20
quantidade_forma = 18

# Nome da Atendente
nome_atendente = "maria"

# Bairros de Entrega
bairro_barroco = "barroco"
bairro_sao_jose = "sao jose"

# Valores de frete
frete_barroco = 5.00
frete_são_jose = 15.00

# Código de venda
codigo_venda = 98568

while True:
    print(f"Bem vindo a padaria Desespero, sou a atendente {nome_atendente}")
    escolha = input(f"Temos os pães: {nome_frances, nome_doce, nome_forma}. Qual pão você deseja?")
    if escolha == nome_frances:
    quantidade = int(imput("Qual a quantidade?"))
    if quantidade <= quantidade_frances:
        quantidade_frances -= quantidade
        pedido_de_paes = quantidade
        valor_compra = quantidade * valor_frances
        print(f"Seui pedido ficou em R$ {valor_compra}.")
    else: 
        print(f"Infelizmente só tenho {quantidade_frances} pães no momento)")
        break
    forma_retirada = input ("É para retirar ou entregar?").lower()
    if forma_retirada == "entregar":
        bairro_entrega = input(f"Qual o bairro? (1:{bairro_barroco}, 2:{bairro_sao_jose})")
        if bairro_entrega == "1":
            valor_frete = frete_barroco
            print(f"Valor do frete R$ {valor_frete}")
        elif bairro_entrega == "2":
        valor_frete = frete_são_jose
        print(f"Valor do frete R$ {valor_frete}")
        else:
        print("Fora da área de entrega")
        break
    
    elif forma_retirada == "1":
        valor_frete = 0.00
    else:
        break

    dados_cliente = input ("Informe seu nome/; ")
    forma_pagamento = input("Escolha a forma de pagamento (1-Dinheiro, 2-Cartão):")

    if forma_pagamento == "1"
        forma_pagamento = "Dinheiro"
    else forma_pagamento = "Cartão"

    codigo_atual = codigo_venda + 1

    print(f" O valor total de sua compra ")
