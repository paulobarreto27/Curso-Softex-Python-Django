usuario = input("Digite seu usuário: ")
senha = input("Digite sua senha: ")
caracteres = len(senha)
if caracteres >=6 and usuario == "admin":
    print("Acesso Válido")
else: 
    print("Login ou senha Inválida")