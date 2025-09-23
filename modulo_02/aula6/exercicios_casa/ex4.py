""""Molde de um Produto
Crie uma nova classe chamada Produto. Todo produto deve ter nome e preço. Depois, crie duas instâncias:
1. Um "Caderno" que custa 15.50.
2. Uma "Caneta" que custa 3.00. Imprima o nome e o preço de cada produto."""

class Produto:
    def __init__(self, nome: str, preco: float) -> None:
        self.nome = nome
        self.preco = preco

    
produto1 = Produto("Caderno", 15.50)
produto2 = Produto("Caneta", 3.00)

print(produto1.nome)
print(produto1.preco)
print(produto2.nome)
print(produto2.preco)