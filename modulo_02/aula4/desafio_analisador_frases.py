""" Desafio - Analisador de Frases"""
""" Crie um programa que recebe uma frase do usuário e faça uma análise completa mostrando:"""
""" - A quantidade de palavras na frase"""
""" - A quantidade de vogais (a, e, i, o, u)"""
""" - A quantidade de consoantes"""
""" Se a frase é um palíndromo"""


def conta_palavras(texto: str) -> int:
    """Conta o número de palavras de um texto"""
    texto_lista = texto.split(" ")
    print(f"Texto em lista {texto_lista}")
    return len(texto_lista)


def conta_vogais(texto: str) -> int:
    """Conta o número de vogais de um texto"""
    vogais = "aeiou"
    contador = 0

    for letra in texto.lower():
        if letra in vogais:
            contador += 1

    return contador


def conta_consoantes(texto: str) -> int:
    """Conta o número de consoantes de um texto"""
    vogais = "aeiou"
    contador = 0

    for letra in texto.lower():
        if (
            letra not in vogais
            and letra != " "
            and not letra.isdigit()
            and letra.isalpha()
        ):
            contador += 1

    return contador

def palindromo(frase: str) -> str:
    """Remove espaços e deixa tudo minúsculo"""
    frase = frase.replace(" ", "").lower()
    """Verifica se é igual ao inverso"""
    if frase == frase[::-1]:
        return "Sim"
    else:
        return "Não"


texto = input("Digite uma frase: ")
total_palavras = conta_palavras(texto)
total_vogais = conta_vogais(texto)
total_consoante = conta_consoantes(texto)
e_palindromo = palindromo(texto)
print(" --- Resumo da Análise --- ")
print(f"Palavras: {total_palavras}")
print(f"Vogais: {total_vogais}")
print(f"Consoantes: {total_consoante}")
print(f"É um palíndromo? {e_palindromo}")


