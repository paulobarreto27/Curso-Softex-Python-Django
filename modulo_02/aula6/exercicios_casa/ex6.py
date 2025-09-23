"""Lógica no Saque
Na mesma classe ContaBancaria, adicione um método para sacar(valor). 
Este método deve verificar se há saldo suficiente na conta.
● Se houver, ele deve subtrair o valor do saldo e imprimir "Saque realizado com sucesso.".
● Se não houver, ele deve imprimir "Saldo insuficiente." e não alterar o saldo. Teste os dois cenários: 
um saque bem-sucedido e uma tentativa de sacar mais do que tem."""

class Conta_bancaria:
    def __init__(self, nome: str, saldo: float) -> None:
        self.nome = nome
        self.saldo = saldo

    
correntista = Conta_bancaria("Paulo", 1000.00)

def sacar_valor(correntista) -> None:
   
    try:
        valor_a_sacar = float(input("Digite o valor que deseja sacar: "))
        if valor_a_sacar <= 0:
            print("Valor inválido.")
            return

        if valor_a_sacar <= correntista.saldo:
            correntista.saldo -= valor_a_sacar
            print("Saque realizado com sucesso, retire seu valor.")
        else:
            print("Saldo insuficiente")
    except ValueError:
        print("Erro! Valor inválido, digite apenas números.")

sacar_valor(correntista)