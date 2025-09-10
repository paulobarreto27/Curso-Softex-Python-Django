palavra = input ("Digite uma palavra: ")
letra = input ("Digite uma letra: ")

if letra in palavra:
    print(f"O {letra} está na palavra")
else:
    print(f"O {letra} não está na palavra")
