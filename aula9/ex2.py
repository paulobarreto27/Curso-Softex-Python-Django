lista1 = ["vermelho", "azul", "verde", "amarelo"]
lista2 = ["verde", "roxo", "azul", "preto"]
itens_em_comum = []

for item in lista2:
    if item in lista1:
        itens_em_comum.append(item)

print(f"As cores em comum são {itens_em_comum}")