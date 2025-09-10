# Desafio de Programação: Validação de Triângulo
# Seu objetivo: Escrever um algoritmo em Python que determine se três valores, fornecidos pelo usuário, podem formar um triângulo.

# As Regras do Jogo
# 1- Teste se a entrada de dados é um número.
# 2- Se for um número teste se é positivo
# 3- Para que três lados (lA,lB,lC) formem um triângulo, eles devem obedecer a duas condições importantes:

# A soma: A soma de quaisquer dois lados deve ser maior que o terceiro lado.
# lA<lB+lC
# lB<lA+lC
# lC<lA+lB

# A diferença: O valor absoluto da diferença entre dois lados deve ser menor que o terceiro lado.
# lA>∣lB−lC∣
# lB>∣lA−lC∣
# lC>∣lA−lB∣
# Dica: use o método abs() para ter o valor absoluto de um número.


def validar_numero(valor):
    
    try:
        numero = float(valor)  
        return abs(numero)
    except ValueError:
        print("Entrada inválida. Digite um número.")
        return None

def formar_triangulo(lA, lB, lC):
    
    cond_soma = (lA < lB + lC) and (lB < lA + lC) and (lC < lA + lB)
    cond_dif = (lA > abs(lB - lC)) and (lB > abs(lA - lC)) and (lC > abs(lA - lB))
    return cond_soma and cond_dif

print("=== Validação de Triângulo ===")

lados = []
for i in range(1, 4):
    while True:
        valor = input(f"Digite o lado {i}: ")
        numero = validar_numero(valor)
        if numero is not None:
            lados.append(numero)
            break

lA, lB, lC = lados

if formar_triangulo(lA, lB, lC):
    print(f"Os lados {lA}, {lB}, {lC} FORMAM um triângulo!")
else:
    print(f"Os lados {lA}, {lB}, {lC} NÃO formam um triângulo.")
    
