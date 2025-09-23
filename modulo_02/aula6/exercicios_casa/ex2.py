""" Criando Pessoas Reais
Usando a classe Pessoa que você criou, crie dois objetos:
1. Uma pessoa chamada "João", com 25 anos.
2. Uma pessoa chamada "Maria", com 30 anos. Depois de criá-los, imprima o nome e 
a idade de cada um para confirmar que deu certo."""

class Pessoa:
    def __init__(self, nome: str, idade: int) -> None:
        self.nome = nome
        self.idade = idade

    

# cria um objeto do tipo classe Pessoa
nova_pessoa = Pessoa("João", 25)
nova_pessoa = Pessoa("Maria", 30)

# nome e idade são atributos (variáves) da classe Pessoa
print(nova_pessoa.nome)
print(nova_pessoa.idade)