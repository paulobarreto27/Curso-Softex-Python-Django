# Considere o seguinte código, que contém um erro. Em qual linha ou trecho o erro ocorre, e qual é o tipo de erro?

nome = "João"
idade_txt = input("Digite sua idade: ")
mensagem = f"Olá, meu nome é {nome} e tenho " + idade_txt + " anos."
if idade_txt >= 18:
    print("Você é maior de idade.")

# *a.Linha 4: O erro ocorre ao tentar comparar um texto (idade_txt) com um número (18).
# b.Não há erro no código.
# c.Linha 3: O operador + não pode ser usado com f-strings.
# d.Linha 5: O erro é na função print().
# e.Linha 2: O erro está na função input().