""" Conta Bancária
Crie uma classe Conta Bancaria. Toda conta deve começar com um titular e um saldo inicial. 
Crie um método depositar(valor) que some um valor ao saldo da conta. 
Crie um objeto, deposite um valor e imprima o novo saldo."""

class Conta_bancaria:
    def __init__(self, nome: str, saldo: float) -> None:
        self.nome = nome
        self.saldo = saldo

    
correntista = Conta_bancaria("Paulo", 1000.00)

print(correntista.nome)
print(correntista.saldo)
correntista.saldo += 1000.00
print(correntista.saldo)