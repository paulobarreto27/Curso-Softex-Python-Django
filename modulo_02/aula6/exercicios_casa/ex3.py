"""Ensinando a se Apresentar
Adicione um método (uma "ação") à sua classe Pessoa chamado apresentar. Esse método deve imprimir uma frase como: 
"Olá, meu nome é [nome] e eu tenho [idade] anos." Chame esse método para os objetos "João" e "Maria"."""

class Pessoa:
    def __init__(self, nome: str, idade: int) -> None:
        self.nome = nome
        self.idade = idade

    def apresentar(self) -> None:
        print(f"Olá, meu nome é {self.nome} e eu tenho {self.idade} anos")


nova_pessoa1 = Pessoa("João", 25)
nova_pessoa2 = Pessoa("Maria", 30)

nova_pessoa1.apresentar()
nova_pessoa2.apresentar()
