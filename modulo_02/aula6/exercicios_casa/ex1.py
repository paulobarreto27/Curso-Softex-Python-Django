"""Molde de uma Pessoa
Crie uma classe chamada Pessoa. No "registro de nascimento" (__init__), 
toda pessoa deve ter um nome e uma idade."""

class Pessoa:
    def __init__(self, nome: str, idade: int) -> None:
        self.nome = nome
        self.idade = idade


nova_pessoa = Pessoa("Paulo", 47)


print(nova_pessoa.nome)
print(nova_pessoa.idade)

