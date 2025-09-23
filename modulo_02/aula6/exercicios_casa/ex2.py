""" Criando Pessoas Reais
Usando a classe Pessoa que você criou, crie dois objetos:
1. Uma pessoa chamada "João", com 25 anos.
2. Uma pessoa chamada "Maria", com 30 anos. Depois de criá-los, imprima o nome e 
a idade de cada um para confirmar que deu certo."""

class Pessoa:
    def __init__(self, nome: str, idade: int) -> None:
        self.nome = nome
        self.idade = idade

    
nova_pessoa1 = Pessoa("João", 25)
nova_pessoa2 = Pessoa("Maria", 30)

print(nova_pessoa1.nome)
print(nova_pessoa1.idade)
print(nova_pessoa2.nome)
print(nova_pessoa2.idade)